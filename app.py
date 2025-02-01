import random
from time import strftime
import time
from flask import Flask,redirect,url_for,render_template,request
import random
import datetime

app = Flask(__name__)



@app.route("/")
def test():
    return render_template("child.html", dashboard_user=username)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        #return redirect(url_for("user",usr=username))
        return render_template("child.html", dashboard_user=username)
    else:
        return render_template("login.html")

@app.route("/test/<usr>")
def user(usr):

     return render_template("child.html", dashboard_user=usr)




# @app.route("/<name>")
# def home(name):
#     number = random.randint(1,1000)
#     var1 = datetime.datetime.now()
#     now = var1.strftime("%Y-%m-%d %H:%M:%S")
#     return render_template("index.html",content=name,randomint=number,datetimenow=now,name_list=['yash','raj','ravi','kavi'])
#
#




# @app.route("/<name>")
# def user(name):
#     return f"hello {name}!"
#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user",name="Yash"))

if __name__ == "__main__":
    app.run(debug=True)