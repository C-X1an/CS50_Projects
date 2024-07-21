import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio = db.execute("SELECT * FROM buy_history WHERE user_id = ?", session["user_id"])
    if not portfolio:
        return render_template("index.html", zipped_list=None)
    else:
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        total_balance = cash
        current_price = []
        for stock in portfolio:
            current_price.append(lookup(stock["symbol"])["price"])
            total_balance += (lookup(stock["symbol"])["price"] * stock["quantity"])
        zipped_list = zip(portfolio, current_price)
        return render_template("index.html", zipped_list=zipped_list, cash=round(cash, 2), total_balance=total_balance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        portfolio = db.execute("SELECT * FROM buy_history WHERE user_id = ?", session["user_id"])
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if symbol == None or lookup(symbol) == None:
            return apology("Invalid Symbol", 400)
        if not shares.isdigit() or int(shares) < 0:
            return apology("Invalid amount of shares", 400)
        cost = lookup(symbol)["price"] * int(shares)
        balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if cost > balance:
            return apology("Insufficient balance", 400)
        else:
            check_symbols = []
            for stock in portfolio:
                check_symbols.append(stock["symbol"])
            if symbol in check_symbols:
                for stock in portfolio:
                    if symbol == stock["symbol"]:
                        db.execute("UPDATE buy_history SET time = datetime('now'), quantity = ? WHERE user_id = ? AND symbol = ?",
                                   (int(shares) + stock["quantity"]), session["user_id"], symbol)
            else:
                db.execute("INSERT INTO buy_history (user_id, symbol, price, time, quantity) VALUES (?, ?, ?, datetime('now'), ?)",
                           session["user_id"], symbol, lookup(symbol)["price"], shares)
            db.execute("INSERT INTO transaction_history (user_id, symbol, price, time, quantity) VALUES (?, ?, ?, datetime('now'), ?)",
                       session["user_id"], symbol, lookup(symbol)["price"], shares)
            new_balance = balance - cost
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, session["user_id"])
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transaction_history = db.execute("SELECT * FROM transaction_history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", transaction_history=transaction_history)


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
        symbol = request.form.get("symbol")
        valuations = lookup(symbol)
        if valuations == None:
            return apology("Invalid symbol", 400)
        return render_template("quoted.html", valuations=valuations)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        digit = 0
        symbol = 0
        input_name = request.form.get("username")
        input_password = request.form.get("password")
        for letter in input_password:
            if letter.isdigit():
                digit += 1
            if not letter.isalpha() and not letter.isdigit():
                symbol += 1
        if digit == 0 or symbol == 0:
            return apology("Password should have at least 1 number and 1 symbol", 400)
        input_confirmation = request.form.get("confirmation")
        if not input_name or db.execute("SELECT username FROM users WHERE username = ?", input_name):
            return apology("Invalid Username", 400)
        if not input_password or input_password != input_confirmation:
            return apology("Password does not match", 400)
        if len(input_password) < 8:
            return apology("Password should contain at least 8 letters", 400)
        hash_password = generate_password_hash(input_password)
        db.execute("INSERT INTO users (username, hash) VALUES (? ,?)", input_name, hash_password)
        id = db.execute("SELECT id FROM users WHERE username = ?", input_name)[0]["id"]
        session["user_id"] = id
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        portfolio = db.execute("SELECT * FROM buy_history WHERE user_id = ?", session["user_id"])
        symbol_sell = request.form.get("symbol")
        quantity_sell = request.form.get("shares")
        if not symbol_sell or symbol_sell not in portfolio[0]["symbol"]:
            return apology("Invalid Stock", 400)
        for stock in portfolio:
            if symbol_sell == stock["symbol"]:
                if int(quantity_sell) > stock["quantity"]:
                    return apology("Insufficient stock", 400)
        if not quantity_sell.isdigit() or int(quantity_sell) < 0:
            return apology("Invalid Amount", 400)
        else:
            original_quantity = int(db.execute("SELECT quantity FROM buy_history WHERE symbol = ? AND user_id = ?",
                                    symbol_sell, session["user_id"])[0]["quantity"])
            if original_quantity - int(quantity_sell) == 0:
                db.execute("DELETE FROM buy_history WHERE symbol = ?", symbol_sell)
            db.execute("UPDATE buy_history SET quantity = ? WHERE symbol = ? AND user_id = ?",
                       original_quantity - int(quantity_sell), symbol_sell, session["user_id"])
            current_price = lookup(symbol_sell)["price"]
            db.execute("INSERT INTO sell_history (user_id, symbol, price, time, quantity) VALUES (?, ?, ?, datetime('now'), ?)",
                       session["user_id"], symbol_sell, lookup(symbol_sell)["price"], quantity_sell)
            db.execute("INSERT INTO transaction_history (user_id, symbol, price, time, quantity) VALUES (?, ?, ?, datetime('now'), ?)",
                       session["user_id"], symbol_sell, lookup(symbol_sell)["price"], int(quantity_sell) * -1)
            initial_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
            db.execute("UPDATE users SET cash = ?", initial_cash + (current_price * int(quantity_sell)))
            return redirect("/")
    else:
        portfolio = db.execute("SELECT * FROM buy_history WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", portfolio=portfolio)


@app.route("/change-password", methods=["POST", "GET"])
@login_required
def change_password():
    if request.method == "POST":
        old_password = request.form.get("original_password")
        updated_password = request.form.get("new_password")
        check_password = request.form.get("confirm_password")
        for letter in updated_password:
            if letter.isdigit():
                digit += 1
            if not letter.isalpha() and not letter.isdigit():
                symbol += 1
        if digit == 0 or symbol == 0:
            return apology("Password should have at least 1 number and 1 symbol", 403)
        hash_password = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"]
        if check_password_hash(hash_password, old_password):
            if updated_password == check_password:
                db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(updated_password), session["user_id"])
                return redirect("/")
            else:
                return apology("New password does not match", 403)
        return apology("Old Password Error", 403)
    else:
        return render_template("change-password.html")


@app.route("/top_up", methods=["GET", "POST"])
@login_required
def top_up():
    if request.method == "POST":
        amount = request.form.get("amount")
        if not amount.isdigit():
            return apology("Amount must be a number", 403)
        current_balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_balance + float(amount), session["user_id"])
        return redirect("/")
    else:
        return render_template("top_up.html")
