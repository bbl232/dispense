from flask import Flask, request
from dispense.users import User
import json
import hashlib, uuid
app = Flask(__name__)

invalid = '{"status": "error", "message": "Invalid endpoint"}', 410

@app.route('/')
def index():
    return invalid 

@app.route('/api/users')
def users():
    return User.get()

@app.route('/api/user',methods=["POST"])
def new_user():
    try:
      data = json.loads(request.data)
    except json.JSONDecodeError as err:
      return '{"status": "error", "message": "JSON ERROR => '+str(err)+'"}', 400

    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512((data['password'] + salt).encode('utf-8')).hexdigest()
    data['password'] = hashed_password
    newUser = User(data['name'], data['password'], salt, data['email'], data['typeOf'])

    return newUser.save()

@app.route('/api/user/<name>')
def user(name):
    if request.method == "GET":
      return User.get(name)
    if request.method == "PUT":
      return User.update(name)
    if request.method == "DELETE":
      return User.delete(name)
