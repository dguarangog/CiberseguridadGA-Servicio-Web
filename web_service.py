import json
import mongodb
from flask import Flask, Response, request
from mongodb import MongoDriver
from bson import json_util
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h2>Hola Mundo!</h2>"

@app.route('/ws_datos', methods=['GET'])
def get_ws_datos():
    mongodb = MongoDriver()
    datos = mongodb.consulta_record(username="REGISTROS")
    response = json_util.dumps(datos)
    return Response(response, mimetype="application/json")
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)