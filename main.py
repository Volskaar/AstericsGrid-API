from flask import Flask, jsonify, request
import service

##################################################################
##################################################################

app = Flask(__name__)

##################################################################
##################################################################

# Test default route by returning JSON object
@app.route('/', methods=['GET'])
def index():
    return "", 200
    
##################################################################
##################################################################

# not implemented routes
@app.route('/', methods=['PUT'])
def put_not_implemented():
    return "", 501

@app.route('/', methods=['DELETE'])
def delete_not_implemented():
    return "", 501

##################################################################
##################################################################

# POST route handling request body
@app.route('/', methods=['POST'])
def return_content():
    # access and decode data in request body
    data = str(request.data.decode('UTF-8'))

    # handle request data in service
    output = service.handle_request(data)

    # return corrected string in response
    return output
