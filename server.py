import os

import numpy as np
from tensorflow import keras
import tensorflow as tf
import flask 
from flask import Flask
from flask import request
from flask_cors import CORS


# local imports 
from utils.cache_data import cache
from utils.tokenizer import tokenize_inputs
from model.model import get_model

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
CORS(app)

model = keras.models.load_model('./model/checkpoints/my_model')
# np.testing.assert_allclose(model, outputs)

@app.route('/infer', methods=["POST"])
# @cache
def inference():
    """return the prediction of the model"""

    sents = request.get_json(force=True)['sents']

    vecs = tokenize_inputs(sents)
    results = model(vecs)

    result = dict()
    result['pred'] = [str(sample.numpy()[0]) for sample in results]
    
    response = flask.Response()
    response.headers.add("Access-Control-Allow-Origin", "*")

    print(result)

    return result

if __name__ == "__main__":
    app.run(debug=True, port=port)