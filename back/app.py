import flask
from flask import request
from flask_cors import CORS
import controller

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

 
@app.route('/', methods=['GET'])
def home():
    #print(content['code'])
    response = flask.jsonify({"mensaje":"gerardo puto"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    controller.analizarEntrada(response.mensaje)
    return response
    
@app.route('/', methods=['POST'])
def compilar():
    content = request.get_json()
    #contenido = content.code
    #print(content['code'])
    response = flask.jsonify({"mensaje":content['code']})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
app.run()