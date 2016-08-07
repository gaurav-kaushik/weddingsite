#!/usr/bin/env python 
"""
These are handlers that deal with browser requests. 
This is how Python talks to your webpage. 
Each view is mapped to at least one request URL.
"""
from flask import Flask as Flask, jsonify as FlaskJSONify, render_template as FlaskRender,request as FlaskRequest
app = Flask(__name__)

# This should render the mainpage on the browser
@app.route('/')
def index():
    return FlaskRender('index.html')

@app.route('/about')
def about():
    return FlaskRender('about.html')

# run Flask in debug mode
if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')