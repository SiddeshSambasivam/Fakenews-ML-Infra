import os

import flask 
from flask import Flask
from flask import request

# local imports 

app = Flask(__name__)
port = int(os.environ.get("PORT", 6000))

@app.route('/infer')
def inference():
    """return the prediction of the model"""

    args = request.args.to_dict() # list of all the arguments
    result = dict()

    return result

if __name__ == "__main__":
    app.run(debug=True, port=port)