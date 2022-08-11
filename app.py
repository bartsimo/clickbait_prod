from os import path
import sqlite3

from flask import Flask, flash, redirect, render_template, url_for, request, session
from flask_session import Session

import joblib

# Configure SQLite such that column names are always shown:
# https://stackoverflow.com/questions/5924149/how-to-configure-sqlite-to-display-headers-by-default


# Configure application
app = Flask(__name__)

# To make app work both locally and on pythonanywhere without fiddling on the paths
ROOT = path.dirname(path.realpath(__file__))

'''
Flask boiler plate
'''

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Load own model and CountVectorizer

clickbait_model = open("clickbait_model.pkl", "rb")
clf = joblib.load(clickbait_model)

cv_vocab = open("cv_vocab.pkl", "rb")
cv = joblib.load(cv_vocab)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

'''
End boiler plate 
'''

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    # In order to initialize db connection in the same thread as call to /predict:
    # AND avoid potentially ernoeous db setting in case of multi-use:
    # https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
    with sqlite3.connect(path.join(ROOT, "clickbait.db")) as db:
        if request.method == 'POST':
            message = request.form.get("message")
            data = [message]

            ###################Problem here##################
            #https://stackoverflow.com/questions/70461730/my-naive-bayes-classifier-works-for-my-model-but-will-not-accept-user-input-on-m
            #https://stackoverflow.com/questions/58020251/how-to-save-classifier-in-sklearn-with-countvectorizer-and-tfidftransformer
            #Works now

            vect = cv.transform(data).toarray()
            my_prediction = clf.predict(vect)

            db.execute("INSERT INTO entries (headline, prediction) VALUES(?, ?)", (message, int(my_prediction[0])))

        return render_template('result.html', prediction = my_prediction, message = message)

@app.route("/about")
def about():
    return render_template("about.html")