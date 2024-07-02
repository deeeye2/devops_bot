from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = requests.post('http://devops-bot-backend-service:5000/login', json={'username': username, 'password': password})
    if response.status_code == 200:
        return redirect(url_for('welcome'))
    return 'Invalid Credentials'

@app.route('/welcome')
def welcome():
    return 'Welcome to DevOps Bot'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

