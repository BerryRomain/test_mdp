from flask import Flask, render_template, request, jsonify
import re
import random
import string

app = Flask(__name__)

def password_strength(password):
    score = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    score = sum(criteria.values())
    return score, criteria

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    pwd = request.json.get('password')
    score, criteria = password_strength(pwd)
    return jsonify({"score": score, "criteria": criteria})

@app.route('/generate')
def generate():
    pwd = generate_password()
    return jsonify({"password": pwd})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
