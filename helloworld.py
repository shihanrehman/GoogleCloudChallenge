
from flask import Flask, jsonify
import os
app = Flask(__name__)
@app.route("/nxchallenge/astarisborn")
def hello():
    return jsonify(
        response='Hello World!'
        )
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)