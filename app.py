from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/') # http:// 
def home():
    return render_template("home.html")

@app.route('/your-url', methods=['GET', 'POST']) # http://localhost:5000/about  
def your_url():
    if request.method == 'POST':
        return render_template("your_url.html", code = request.form['code']) 
    else:
        return 'This is not valid'
    # return render_template("your_url.html", code = request.args['code'])
