#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "success",
        "repository": "jie913125-cmyk/docker.git",
        "message": "Python service deployed via CI/CD",
        "port": 8080
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
