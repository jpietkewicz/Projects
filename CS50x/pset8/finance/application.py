import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


    # stocks = db.execute("select symbol, sum(num_shares) as sum from transactions group by num_shares having sum > 0")
    # numShares = []
    # for stock in stocks:
    #     numShares.append({stock["symbol"], stock["sum"]})


    # cash = db.execute("select cash from users where id = :id", id=session["user_id"])
    # cash = float(cash[0]["cash"])

    #return render_template("index.html", stocks=stocks, numShares=numShares, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stockInfo = lookup(request.form.get("symbol"))

        if not stockInfo:
            return apology("invalid symbol", 400)

        if int(request.form.get("shares")) <= 0:
            return apology("invalid number of shares", 400)

        price = int(request.form.get("shares")) * float(stockInfo["price"])

        cash = db.execute("select cash from users where id = :id", id=session["user_id"])

        if price > float(cash[0]["cash"]):
            return apology("not enough money", 400)
        else:
            cash = float(cash[0]["cash"]) - price
            # insert transaction into transactions
            db.execute("insert into transactions (user_id, symbol, num_shares, amount) values (:id, :symbol, :shares, :amount)",
                          id=session["user_id"], symbol=stockInfo["symbol"], shares=int(request.form.get("shares")), amount=price)

            # insert cash - price into users
            db.execute("update users set cash = :cash where id = :id", cash=cash, id=session["user_id"])

            return redirect("/")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("select symbol, num_shares, amount from transactions where user_id = :id", id=session["user_id"])

    return render_template("history.html", history=history)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        stockInfo = lookup(request.form.get("symbol"))

        if not stockInfo:
            return apology("invalid symbol", 400)

        # convert price to usd format
        stockInfo["price"] = usd(stockInfo["price"])

        return render_template("quoted.html", stockInfo=stockInfo)
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":
        # ensure username submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # ensure password submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # ensure passwords match
        elif request.form.get("password") != request.form.get("password2"):
            return apology("passwords do not match", 403)

        # check if username is in database
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) != 0:
            return apology("username taken", 403)


        # hash password
        hashedPassword = generate_password_hash(request.form.get("password"))

        # insert user into database
        db.execute("insert into users (username, hash) values (:username, :hash)",
                          username=request.form.get("username"), hash=hashedPassword)

        return redirect("/login")

    # method == GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")

    # if request.method == "POST":
    #     symbol = request.form.get("symbol")
    #     shares = int(request.form.get("shares"))

    #     # look up current price
    #     stockInfo = lookup(symbol)
    #     if not stockInfo:
    #         return apology("invalid symbol", 400)
    #     # if no holding of that stock
    #     stocks_held = db.execute("select symbol from transactions group by symbol having sum(num_shares) > 0")
    #     # if stockInfo["symbol"] not in set(stocks_held["symbol"]):
    #     #     return apology("no stock owned")


    #     shares_held = db.execute("select sum(num_shares) from transactions group by symbol having symbol = :symbol", symbol=symbol)
    #     if shares_held[0]['sum(num_shares)'] < shares:
    #         # sell all shares held of that stock
    #         db.execute("insert into transactions (user_id, symbol, num_shares, amount) values (:id, :symbol, :num_shares, :amount)",
    #                     id=session["user_id"], symbol=symbol, num_shares=-shares_held["sum(num_shares)"], amount=stockInfo["price"]*shares_held["sum(num_shares)"])
    #         db.execute("update users set cash = :cash where id = :id", cash=stockInfo["price"] * shares_held["sum(num_shares)"], id=session["user_id"])
    #         return redirect("/")


    # else:
    #     return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
