import flask
from flask import request
from flask_cors import CORS
from controller import analizarEntrada,Regreso

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

 
@app.route('/', methods=['GET'])
def home():
    #print(content['code'])
    response = flask.jsonify({"mensaje":"gerardo puto"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    #analizarEntrada(response.mensaje)
    return response
    
@app.route('/', methods=['POST'])
def compilar():
    content = request.get_json()
    #contenido = content.code
    #print(content['code'])
    ret:Regreso = analizarEntrada(content['code'])
    #print(ret.errores)
    response = flask.jsonify({"consola":ret.consola,"errores":ret.errores,"ast":ret.ast})
    #print(ret.ast)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
app.run()