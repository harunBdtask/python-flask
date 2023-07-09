from flask import Blueprint, jsonify
import redis
import json
from config.configurations import Config
test = Blueprint('test', __name__)
# redis connection
r = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, password=Config.REDIS_PASSWORD)
@test.route('/test')
def testing():
    mylist = r.keys('*')
    return str(mylist)
@test.route('/redis')
def set_get():
    mylist = ['value1', 'value2', 'value3']
    r.set('mykey', json.dumps(mylist))
    res = r.get('mykey')
    return str(res)
# Simple Route
@test.route('/hi')
def home():
    return 'Hello, W!'
# Example route for returning a JSON response
@test.route('/users')
def get_users():
    users = [
        {
            'id': 1,
            'name': 'Alice',
            'email': 'alice@example.com'
        },
        {
            'id': 2,
            'name': 'Bob',
            'email': 'bob@example.com'
        }
    ]
    return jsonify(users)

