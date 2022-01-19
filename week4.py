from cgitb import text
from datetime import date
from email import message
import re
from wsgiref.util import request_uri
from flask import Flask, redirect, url_for, render_template,request,session
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("week4index.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
    user = "test"
    account = request.form["account"]
    account_password = request.form["account_password"]
    if account == user and account_password == user :
        return redirect("/member")
    if account == "" or account_password =="" :
        error_message = "請輸入帳號、密碼"
        return redirect(url_for("error",error=error_message))
    if account != user or  account_password != user :
        error_message = "帳號、密碼輸入錯誤"
        return redirect(url_for("error",error=error_message))

@app.route("/error/message<error>")
def error(error):
    return render_template("week4error.html",error_message=error)


@app.route("/member")
def memnber():
    return render_template("week4member.html")



@app.route("/signout", methods=["POST","GET"])
def signout():
    account = request.form['account']
    return account

if __name__=="__main__":
    app.run(debug=True,port=3000,threaded=True)