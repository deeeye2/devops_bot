from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Backend service URL
backend_url = 'http://devops-bot-backend-service:5000/api'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {
            'username': request.form['username'],
            'password': request.form['password']
        }
        response = requests.post(f'{backend_url}/login', json=data)
        if response.status_code == 200:
            return redirect('/dashboard')
        else:
            return response.json()['message']
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'username': request.form['username'],
            'password': request.form['password']
        }
        response = requests.post(f'{backend_url}/register', json=data)
        if response.status_code == 201:
            return redirect('/login')
        else:
            return response.json()['message']
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



