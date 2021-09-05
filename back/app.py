import flask
from flask import request
from flask_cors import CORS
from controller import analizarEntrada,Regreso

app = flask.Flask(__name__)
CORS(app)
#app.config["DEBUG"] = True

 
@app.route('/', methods=['GET'])
def home():
    response = flask.jsonify({"mensaje":"gerardo puto"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/', methods=['POST'])
def compilar():
    content = request.get_json()
    ret:Regreso = analizarEntrada(content['code'])

    response = flask.jsonify({"consola":ret.consola,"errores":ret.errores,"ast":ret.ast})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
#app.run()