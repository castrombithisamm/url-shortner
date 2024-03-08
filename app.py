from flask import Flask

app = Flask(__name__)

@app.route('/') # http:// 
def home():
    return 'Hello, Flgggggggggggasgg!'

@app.route('/about') # http://localhost:5000/about  
def about():
    return 'This is a URL Shortener sejjjjrviddddce'
