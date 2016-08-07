"""
This script should be in your 'app' dir. 
Create the object 'Flask' as app. 
Then we invoke views.py in app dir.
"""
from flask import Flask
app = Flask(__name__)
from app import views
