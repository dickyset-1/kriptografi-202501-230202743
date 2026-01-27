import hashlib
import json
import sqlite3
import random
from time import time
from datetime import datetime
from flask import Flask, jsonify, request, render_template, session, redirect, url_for

# =====================
# FLASK SETUP
# =====================

app = Flask(__name__)
app.secret_key = 'sheepcoin-secret-key-metamask' # Secret key
DB = 'sheepcoin.db'

# =====================
# KONFIGURASI GAME
# =====================
MINING_DIFFICULTY = 4 
BASE_REWARD = 1 / (100 * MINING_DIFFICULTY) 

# =====================
# DATABASE INIT
# =====================

def get_db():
    return sqlite3.connect(DB)

def init_db():
    db = get_db()
    c = db.cursor()

    # Users Table (Diubah untuk Metamask)
    # Kita hanya butuh wallet address. Username opsional.
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        wallet TEXT PRIMARY KEY,
        username TEXT
    )
    """)

    # Blocks
    c.execute("""
    CREATE TABLE IF NOT EXISTS blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idx INTEGER,
        timestamp REAL,
        proof INTEGER,
        previous_hash TEXT
    )
    """)

    # Transactions
    c.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        block_idx INTEGER,
        sender TEXT,
        recipient TEXT,
        amount REAL
    )
    """)

    # Genesis block
    c.execute("SELECT COUNT(*) FROM blocks")
    if c.fetchone()[0] == 0:
        c.execute(
            "INSERT INTO blocks (idx, timestamp, proof, previous_hash) VALUES (1, ?, 100, '1')",
            (time(),)
        )

    db.commit()
    db.close()


# =====================
# BLOCKCHAIN LOGIC
# =====================

def hash_block(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def last_block():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT idx, timestamp, proof, previous_hash FROM blocks ORDER BY idx DESC LIMIT 1")
    row = c.fetchone()
    db.close()
    return {
        'index': row[0],
        'timestamp': row[1],
        'proof': row[2],
        'previous_hash': row[3]
    }

def proof_of_work(last_proof):
    proof = 0
    target_str = "0" * MINING_DIFFICULTY
    while not hashlib.sha256(f'{last_proof}{proof}'.encode()).hexdigest().startswith(target_str):
        proof += 1
    return proof

def current_wallet():
    return session.get('wallet')

# =====================
# ROUTES
# =====================

@app.route('/')
def dashboard():
    if not current_wallet():
        return redirect(url_for('login'))
    return render_template('index.html')


# ---------- AUTH (METAMASK) ----------

@app.route('/login')
def login():
    # Halaman login sekarang hanya tombol "Connect Wallet"
    if current_wallet():
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/auth/metamask', methods=['POST'])
def auth_metamask():
    data = request.get_json()
    wallet_address = data.get('address')
    
    if not wallet_address:
        return jsonify({'error': 'No address provided'}), 400
    
    # Simpan ke DB jika user baru
    db = get_db()
    c = db.cursor()
    c.execute("INSERT OR IGNORE INTO users (wallet, username) VALUES (?, ?)", (wallet_address, 'Miner'))
    db.commit()
    db.close()
    
    # Set Session
    session['wallet'] = wallet_address
    session['username'] = f"{wallet_address[:6]}...{wallet_address[-4:]}"
    
    return jsonify({'status': 'success', 'redirect': url_for('dashboard')})

@app.route('/register')
def register():
    # Di Web3, register tidak diperlukan, redirect ke login
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ---------- API ----------

@app.route('/wallet')
def wallet():
    wallet_id = current_wallet()
    # Gunakan format pendek untuk display username
    username = session.get('username', wallet_id[:8] if wallet_id else 'Guest')
    
    if not wallet_id:
        return jsonify({'error': 'unauthorized'}), 401

    db = get_db()
    c = db.cursor()

    # Hitung Saldo Total
    c.execute("""
        SELECT 
        SUM(CASE WHEN recipient=? THEN amount ELSE 0 END) -
        SUM(CASE WHEN sender=? THEN amount ELSE 0 END)
        FROM transactions
    """, (wallet_id, wallet_id))
    balance = c.fetchone()[0] or 0

    # Hitung Mining Hari Ini
    start_of_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    
    c.execute("""
        SELECT SUM(t.amount)
        FROM transactions t
        JOIN blocks b ON t.block_idx = b.idx
        WHERE t.recipient = ? 
        AND t.sender = '0' 
        AND b.timestamp >= ?
    """, (wallet_id, start_of_day))
    
    mined_today = c.fetchone()[0] or 0

    db.close()

    return jsonify({
        'node_id': wallet_id, 
        'balance': balance,
        'username': username,
        'mined_today': mined_today
    })


@app.route('/mine')
def mine():
    wallet_id = current_wallet()
    if not wallet_id:
        return jsonify({'error': 'unauthorized'}), 401

    last = last_block()
    proof = proof_of_work(last['proof'])
    new_index = last['index'] + 1

    volatility = random.uniform(0.8, 1.2)
    final_reward = BASE_REWARD * volatility
    
    is_lucky = False
    if random.random() < 0.05: 
        final_reward = final_reward * 5
        is_lucky = True

    final_reward = round(final_reward, 6)

    db = get_db()
    c = db.cursor()

    c.execute(
        "INSERT INTO blocks (idx, timestamp, proof, previous_hash) VALUES (?, ?, ?, ?)",
        (new_index, time(), proof, hash_block(last))
    )

    # Reward dikirim ke Wallet Address Metamask
    c.execute(
        "INSERT INTO transactions (block_idx, sender, recipient, amount) VALUES (?, '0', ?, ?)",
        (new_index, wallet_id, final_reward)
    )

    db.commit()
    db.close()

    msg = '🔥 SUPER BLOCK (JACKPOT)!' if is_lucky else 'Block Ditemukan!'

    return jsonify({
        'message': msg, 
        'index': new_index,
        'reward': final_reward
    })


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    wallet = current_wallet()
    data = request.get_json()

    # Validasi Sender harus sama dengan session (Keamanan dasar)
    # Dalam implementasi Full Web3, ini harus divalidasi dengan signature.
    if wallet.lower() != data['sender'].lower():
        return jsonify({'error': 'invalid sender'}), 403

    db = get_db()
    c = db.cursor()

    c.execute("SELECT idx FROM blocks ORDER BY idx DESC LIMIT 1")
    block_idx = c.fetchone()[0]

    c.execute(
        "INSERT INTO transactions (block_idx, sender, recipient, amount) VALUES (?, ?, ?, ?)",
        (block_idx, data['sender'], data['recipient'], data['amount'])
    )

    db.commit()
    db.close()

    return jsonify({'message': 'Transaksi ditambahkan'}), 201


@app.route('/chain')
def chain():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT idx, timestamp, proof, previous_hash FROM blocks ORDER BY idx DESC LIMIT 10")
    blocks = []

    for b in c.fetchall():
        c.execute("SELECT sender, recipient, amount FROM transactions WHERE block_idx=?", (b[0],))
        txs = [{'sender': t[0], 'recipient': t[1], 'amount': t[2]} for t in c.fetchall()]
        blocks.append({
            'index': b[0],
            'timestamp': b[1],
            'proof': b[2],
            'previous_hash': b[3],
            'transactions': txs
        })

    db.close()
    return jsonify({'chain': blocks})


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)