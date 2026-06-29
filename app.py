import os, requests, sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_ID = os.environ.get("PHONE_NUMBER_ID")
TU_NUMERO = os.environ.get("TU_NUMERO")
VERIFY_TOKEN = "UCV_FLEX_2025"

def init_db():
    conn = sqlite3.connect("data.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS pedidos
                    (id INTEGER PRIMARY KEY, cliente TEXT, tel TEXT, total REAL, estado TEXT, fecha TEXT)""")
    conn.commit()
    conn.close()
init_db()

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    return "ok", 200

@app.route("/")
def home(): return jsonify({"status": "ok"})

if __name__ == "__main__": app.run(host="0.0.0.0", port=10000)
