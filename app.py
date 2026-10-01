import os
import threading
import time
from flask import Flask
from datetime import datetime
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return """🤖 Pikachu Protection Bot is running!
    
    ⚡ Status: Online
    💎 Version: 3.0.0
    👑 Owner: Crazy Boy
    """

@app.route('/health')
def health():
    return "OK"

@app.route('/status')
def status():
    return {
        "status": "online",
        "bot": "Pikachu Protection",
        "version": "3.0.0",
        "owner": "Crazy Boy"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
