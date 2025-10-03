# Build flask mon-app

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/transactions")
def transactions():
    # App B queries App A
    users = requests.get("http://app-a:5000/users").json()
    return jsonify({"transactions": f"Transactions linked to {users}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
