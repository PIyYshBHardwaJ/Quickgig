import os


from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
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
db = SQL("sqlite:///quickgig.db")


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
    # return redirect("/")
    return render_template("home.html")

@app.route("/publish", methods=["GET", "POST"])
@login_required
def publish():
    """post job"""
    # User reached route via POST (submitting the register form)
    if request.method == "POST":

        #ensure title was submitted
        title = request.form.get("title")

        #ensure desc. was submitted
        description = request.form.get("description")

        #ensure budget was submitted
        budget = request.form.get("budget")

        #ensure deadline was submitted
        deadline = request.form.get("deadline")

        #ensure email was submitted
        email = request.form.get("email")

        # Insert details into the database
        try:
            db.execute("""INSERT INTO job (user_id, title, description, budget, deadline, email) VALUES (:user_id, :title, :description, :budget, :deadline, :email)""",
                   user_id=session["user_id"], title=title, description=description, budget=budget, deadline=deadline, email=email)
            # db.commit()  # Ensure the transaction is committed to the database
        except Exception as e:
            return f"An error occurred while inserting data: {e}"

        # redirect to pojects posted page
        return redirect("/posted")
    else:
        return render_template("publish.html")

@app.route("/posted")
@login_required
def posted():
    """Show projects posted"""
    rows = db.execute("SELECT title, description, budget, deadline, email FROM job WHERE user_id = :user_id", user_id=session["user_id"])
    return render_template("posted.html", rows=rows)

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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")#/home

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

@app.route("/Hire", methods=["GET", "POST"])
@login_required
def Hire():
    """Show and Delete profile"""
    if request.method == "POST":
        print("Delete route accessed")
        print("User ID:", session["user_id"])
        result = db.execute("DELETE FROM job WHERE user_id = ?", (session["user_id"],))
        return render_template("Hire.html")

    rows = db.execute("SELECT name, bio, experience, email FROM people")
    return render_template("Hire.html", rows=rows)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (submitting the register form)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # save username and password hash in variables
        username = request.form.get("username")

        # Example login logic
        hash = generate_password_hash(request.form.get("password"))

        # Query database to ensure username isn't already taken
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=username)
        if len(rows) != 0:
            return apology("username is already taken", 400)

        # insert username and hash into database
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                   username=username, hash=hash)

        # redirect to login page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/earn", methods=["GET", "POST"])
@login_required
def earn():
    if request.method == "POST":
        result = db.execute("DELETE FROM people WHERE user_id = ?", (session["user_id"],))
        return render_template("earn.html")

    print("Earn route accessed")
    rows = db.execute("SELECT title, description, budget, deadline, email FROM job")
    print(rows)
    return render_template("earn.html", rows=rows)

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Create Profile"""
    # User reached route via POST (submitting the register form)
    if request.method == "POST":

        #ensure title was submitted
        name = request.form.get("name")

        #ensure desc. was submitted
        bio = request.form.get("bio")

        #ensure budget was submitted
        experience = request.form.get("experience")


        #ensure email was submitted
        email = request.form.get("email")

        # Insert details into the database
        existing_user = db.execute("SELECT * FROM people WHERE user_id = :user_id", user_id=session["user_id"])
        if existing_user:
            return "User already exists."
        else:
            try:
                db.execute("""INSERT INTO people (user_id, name , bio,  experience, email) VALUES (:user_id, :name, :bio, :experience, :email)""",
                   user_id=session["user_id"], name=name, bio=bio, experience=experience, email=email)
            except Exception as e:
                return f"An error occurred while inserting data: {e}"
        # redirect to pojects posted page
        print(session["user_id"], name, bio, experience, email)
        return redirect("/profile")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("create.html")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Show and Delete profile"""
    rows = db.execute("SELECT name, bio, experience, email FROM people WHERE user_id = :user_id", user_id=session["user_id"])
    return render_template("profile.html", rows=rows)
