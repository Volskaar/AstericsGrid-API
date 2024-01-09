from flask import Flask, request
import service_language_tool
import service_duden_api
import service_spacy_rules
import service_json_handler

##################################################################

app = Flask(__name__)

##################################################################

# not implemented routes

@app.route('/', methods=['GET'])
def get_not_implemented():
    return "", 501

# not implemented routes
@app.route('/', methods=['PUT'])
def put_not_implemented():
    return "", 501

# not implemented routes
@app.route('/', methods=['DELETE'])
def delete_not_implemented():
    return "", 501

##################################################################

# POST route handling request body

@app.route('/', methods=['POST'])
def run_python_language_tool():
    # access and decode data in request body
    data = str(request.data.decode('UTF-8'))

    # handle request data in service
    output = service_language_tool.handle_request(data)

    # return corrected string in response
    return output, 200

##################################################################

# POST route testing/employing duden correction

@app.route('/duden', methods=['POST'])
def run_duden_api_check():
    text = str(request.data.decode('UTF-8'))
    output = service_duden_api.duden_api_request(text)
    return output, 200

##################################################################

# POST route employing spacy analyzer and rule based correction
# with TEXT based input/output

@app.route('/spacy', methods=['POST'])
def run_spacy_grammar_check():
    text = str(request.data.decode('UTF-8'))
    output = service_spacy_rules.rule_based_correction(text)
    return output, 200

##################################################################

# POST route emplyoing spacy analyzer and rule based correction 
# with JSON based input/output

@app.route('/spacy2', methods=['POST'])
def run_spacy_grammar_check():
    text = service_json_handler.json_to_string(request.data.decode('UTF-8'))
    corrected_text = service_spacy_rules.rule_based_correction(text)
    output = service_json_handler.string_to_json(corrected_text)
    return output, 200