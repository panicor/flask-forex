from flask import Flask, redirect, session, render_template, jsonify, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from converter import Converter
# import ssl 
# import certifi from urllib.request 
# import urlopen

app = Flask(__name__)

app.config["SECRET_KEY"] = "hey"
app.debug = True

# Make Flask errors be real errors, not HTML pages with error info
#app.config['TESTING'] = True

toolbar = DebugToolbarExtension(app)

# This is a bit of hack, but don't use Flask DebugToolbar
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/converted", methods=["POST"])
def convert():

    # r = requests.get('http://127.0.0.1:5000/converted', verify = False)

    to_curr = request.form["to_curr"].upper()
    from_curr = request.form["from_curr"].upper()
    amount = request.form["amount"]

    c = Converter(to_curr, from_curr, amount)

    new_amt = c.converted()

    # if c.get_currency_data(to_curr):
    #     new_amount = converted(to_curr, from_curr, amount)

    return render_template("converted.html", new_amt=new_amt, amount=amount, to_curr=to_curr, from_curr=from_curr)






