from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = requests.post('http://devops-bot-backend-service:5000/login', json={'username': username, 'password': password})
        if response.status_code == 200:
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = requests.post('http://devops-bot-backend-service:5000/register', json={'username': username, 'password': password})
        if response.status_code == 200:
            return redirect(url_for('login'))
        else:
            return 'Registration Failed'
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

