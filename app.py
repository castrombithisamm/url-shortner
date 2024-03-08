from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/') # http:// 
def home():
    return render_template("home.html")

@app.route('/your-url') # http://localhost:5000/about  
def your_url():
    return render_template("your_url.html")
