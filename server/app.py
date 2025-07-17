from flask import Flask, request, url_for, redirect, render_template
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb+srv://nihalmotukuri:6gSkQW3gXw111k6L@flask-cluster.eftmwx7.mongodb.net/?retryWrites=true&w=majority&appName=flask-cluster')
db = client['crud-db']
registered_users = db['registered_users']

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registered_users.insert_one({ 'username': username, 'password': password })
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    print(auth)
    if not auth or not auth['username'] or not auth['password']:
        return {'msg': 'Missing credentials'}, 401

    username = auth['username']
    print("username:",username)

    password = auth['password']
    print("password:",password)
    user = registered_users.find_one({"username":username})
    if user:
        if user["password"] == password:
            return {'msg': 'Login Successful', 'response': 'ok'}, 200
    elif not user:
        return {'msg': 'User not found'}, 404
    else:
        return {'msg': 'Invalid credentials'}, 401

if __name__ == '__main__':
    app.run(debug=True)