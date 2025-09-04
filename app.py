from flask import Flask, render_template, request, jsonify
import re
import random
import string

app = Flask(__name__)

# Fonction pour tester la force du mot de passe
def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1
    return score

# Fonction pour générer un mot de passe fort
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    pwd = request.json.get('password')
    score = password_strength(pwd)
    return jsonify({'score': score})

@app.route('/generate')
def generate():
    pwd = generate_password()
    return jsonify({'password': pwd})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
