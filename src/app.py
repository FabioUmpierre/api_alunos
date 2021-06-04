# save this as app.py
from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/goodbye")
def goodbye():
    return "goodbye"

@app.route('/alunos')
def alunos():
    alunos = [{
        "nome": "fabio"
    }]
    return json.dumps(alunos)
