import _pickle as pickle
import sys
import json
from sklearn.feature_extraction.text import TfidfVectorizer

from flask import Flask, request
from flask_restful import reqparse
from flask_cors import CORS


def predict(headline):
    try:
        f = open('trained_model', 'rb')
        clf = pickle.load(f)
        f = open('vectorizer', 'rb')
        vectorizer = pickle.load(f)
        print("inside predict")
        return clf.predict_proba(vectorizer.transform(headline))[0][1]
    except IOError:
        print("Model not present, run train.py first")


app = Flask(__name__)
CORS(app)
parser = reqparse.RequestParser()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/', methods=['POST'])
def getX():
    data = request.get_json()
    t = data['titles']
    response = ""
    print(t)
    for element in t:
        x = (int(predict([element])*100))
        response = response+" "+str(x)
    print(response)
    # if(x > 70):
    #     response['msg'] = 'clickbait'
    # else:
    #     response['msg'] = 'not-clickbait'
    return response


if __name__ == "__main__":
    app.run(debug=True)
