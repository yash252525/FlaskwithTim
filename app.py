import random
from flask import Flask, redirect, url_for, render_template, request, session, flash
import datetime
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "dasfaweoiwrwenfwerjjiokkjkbhbuvtycv"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def test():
    if "username" in session:
        return render_template("child.html", dashboard_user=session["username"])
    return render_template("child.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if not request.form["nm"]:
            flash("Please enter a username to continue.", "error")
            return render_template("login.html")  # ✅ Correct template
        session.permanent = True
        user = request.form["nm"]
        session["username"] = user
        flash(f"Welcome, {user}!", "success")
        return render_template("child.html", dashboard_user=user)
    else:
        if "username" in session:
            return redirect(url_for("test"))
        return render_template("login.html")

@app.route("/test/<usr>")
def user(usr):
    return render_template("child.html", dashboard_user=usr)

@app.route("/logout")
def logout():
    if "username" in session:
        user = session["username"]
        flash(f"{user}, you have been logged out!", "info")  # ✅ Flash message added
        session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
