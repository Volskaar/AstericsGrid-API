from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Test default route by returning JSON object
@app.route('/', methods=['GET'])
def index():
    return jsonify({'name': 'max', 'email': 'max@mustermann.com'})

# POST route with body returning sent content
@app.route('/', methods=['POST'])
def return_content():
    data = json.loads(request.data)
    return jsonify(data)

# not implemented routes
@app.route('/', methods=['PUT'])
def put_not_implemented():
    return "<p>not implemented</p>"

@app.route('/', methods=['DELETE'])
def delete_not_implemented():
    return "<p>not implemented</p>"