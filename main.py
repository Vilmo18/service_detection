import random
from flask import Flask
import json
# importation de la bibliothèque
import requests
import pickle
import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import pandas as pd
import requests
import random as rd
from bson.json_util import dumps


app = Flask(__name__)
CORS(app)
mongo_db = PyMongo(app, uri='mongodb://127.0.0.1:27017/minfopra')
db = mongo_db.db


@app.route('/detection/update')
def transaction():

    model = pickle.load(open("model.pkl", "rb"))
    prediction = model.predict([0, 0, 0, 0])
    print(prediction)


# récupération du contenu à l'aide de la méthode get()
"""r = requests.get("https://jsonplaceholder.typicode.com/posts")

app=Flask(__name__)
@app.route("/test", methods=["GET"])
def test_get():
    return r.json()[random.randint(0,20)]

@app.route('/enregistrement',methods=['POST'])
def enregistrement():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    print("lancement")"""
