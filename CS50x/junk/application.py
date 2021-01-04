from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///inventory.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return redirect("/")
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        if not request.form.get("sku"):
            return render_template("add.html")

    # return render_template("add.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    return render_template("delete.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    return render_template("order.html")