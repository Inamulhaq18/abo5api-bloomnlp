import os
from flask import Flask,jsonify,request
import time
from threading import Thread
from textgeneration import *

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to textgeneration API contact +966592012861"

@app.route('/generate')
def return_status():
    """Return first the response and tie the my_task to a thread"""
    productname = (request.args.get('productname'))
    if len(productname)>0:
        Thread(target = my_task,args=(productname,)).start()
    if len(productname)==0:
        return jsonify(str("No name"))
    productname=""
    return jsonify(str(responsea))

@app.route('/generateinstant')
def return_status():
    """Return first the response and tie the my_task to a thread"""
    productname = (request.args.get('productname'))
    if len(productname)>0:
        my_task(productname)
    if len(productname)==0:
        return jsonify(str("No name"))
    productname=""
    return jsonify(str("Images detected"))


def my_task(productname):
    print("rurl Before:  "+productname)
    responsea=generate(productname)
    print("rurl After:  "+productname)
    print("_________________________")
    print(responsea)
    return (responsea)
