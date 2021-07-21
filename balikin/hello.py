from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#def hello_world():
 #   return "<p>Hello, World! Deploy nich...</p>"

#@app.route("/works")
#def it_works():
 #   return "IT Works! nyehehe"
def index():
    return render_template('index.html')
