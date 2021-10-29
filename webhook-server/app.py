from flask import Flask, request, jsonify, render_template, make_response
import os
# import dialogflow
import requests
import json
import random
# import pusher
import numpy as np
from DB import DB

app = Flask(__name__)
db = DB()

@app.route('/')
def index():
    return "HELLO"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    tag = data['fulfillmentInfo']['tag']
    print(tag)
    if tag == 'randomWelcome':
        names = ['Trâm', 'Nhật', 'Đức', 'Đạt', 'Ngoan']
        #name = db.query()['name']
        return make_response(jsonify({"sessionInfo": {"parameters": {
            "is_true": True,# bool(random.getrandbits(1)),
            "name": np.random.choice(names)
            }}}))
    print(data)
    return make_response(jsonify({"sessionInfo": {"parameters": {"in_hours": True}}}))

# run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
