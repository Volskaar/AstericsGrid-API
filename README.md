# AstericsGrid-API
German Grammar Correction API for the AstericsGrid Project

----------------------------------------------------------

### Preparations:
1. create new .venv <br>
2. clone repo into .venv
3. activate .venv

### Install Ddpendencies:
pip install -r requirements.txt

### Include spacy model:
python -m spacy download de_core_news_sm

### Run:
flask --app main run

### How to test:
#### Via provided CURL-script
run the test.curl.bat file in the commandline

#### Via browser:
access http:127.0.0.1:5000

#### With software e.g. Postman:
1. set request type (POST)
2. fill request body (TEXT)
3. send Request
