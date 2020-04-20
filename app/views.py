from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("main-program.html")

@app.route("/about")
def about():
    return render_template("about-program.html")
    return "<h1 style='color: red'>Tentang program</h1>"
