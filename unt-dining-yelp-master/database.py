from flask import Flask, request, jsonify
from datetime import datetime, timedelta #for the date and time 
import sqlite3

web = Flask(__name__)

@web.route('/')
def HelloWorld():
    return "Hello World!"

if __name__ == '__main__':
    web.run(debug=True)