from flask import Flask, redirect, url_for, render_template,request,session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'usertest' 


@app.route("/")
def home():
    account = session.get('account')
    if account == 'test' :
        return redirect(url_for('member'))
    if account != 'test' :
        return render_template("week4index.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
    user = "test"
    account = request.form["account"]
    account_password = request.form["account_password"]
    if account == user and account_password == user :
        session['account'] = account
        return redirect("/member")
    if account == "" or account_password =="" :
        error_message = "請輸入帳號、密碼"
        return redirect(url_for("error",message=error_message))
    if account != user or  account_password != user :
        error_message = "帳號、密碼輸入錯誤"
        return redirect(url_for("error",message=error_message))

@app.route("/error/")
def error():
    message = request.args.get("message") 
    return render_template("week4error.html",error_message={}).format(message)


@app.route("/member")
def member():
    account = session.get('account')
    user = "test"
    if account == user :
        return render_template("week4member.html")
    if account != user :
        return redirect(url_for('home'))


@app.route("/signout")
def signout():
   
    session.pop('account', None)
    return  redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True,port=3000,threaded=True)
