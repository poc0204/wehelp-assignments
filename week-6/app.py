import mysql.connector
from mysql.connector import Error
from flask import Flask ,redirect,url_for ,render_template , request , session 
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "usertest"

@app.route("/")
def index():
    username = session.get('username')
    if username != None:
        return render_template("member.html")
    else:
        return render_template("index.html")
        
@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    password = request.form["password"]
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    connection = link_mysql()
    cursor = connection.cursor()
    sql = " select username from member ; "
    cursor.execute(sql)
    all_username = cursor.fetchall()
    for i in range(len(all_username)):
        if username == data_clean(all_username[i],1) and password == data_clean(all_username[i],1) :
            error_message = "帳號已經被註冊"
            return redirect(url_for("error",message=error_message))

    sql = " insert into member (name ,username ,password) values ('{}' ,'{}' ,'{}');".format(name,username,password)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    connection = link_mysql()
    cursor = connection.cursor()
    sql = " select username from member ; "
    cursor.execute(sql)
    all_username = cursor.fetchall()
    sql = " select password from member ; "
    cursor.execute(sql)
    all_password = cursor.fetchall()
    for i in range(len(all_username)):
        if username == data_clean(all_username[i],1) and password == data_clean(all_password[i],1) :
            session['username'] = username
            return redirect("member")

    cursor.close()
    connection.close()
    error_message = "帳號、密碼輸入錯誤"
    return redirect(url_for("error",message=error_message))


@app.route("/member")
def member():
    username = session.get('username')
    if username != None:
        connection = link_mysql()
        cursor = connection.cursor()
        sql = " select name from member where username= '{}'".format(username)
        cursor.execute(sql)
        name = cursor.fetchone()
        cursor.close()
        connection.close()
        return render_template("member.html",name=data_clean(name,1))
        


@app.route("/error/")
def error():
    message = request.args.get("message") 
    return render_template("error.html",error_message={}).format(message)


@app.route("/singout",methods=["GET"])
def singout():
    session.clear()
    return  redirect(url_for('index'))

def data_clean(data,method):
    if method ==0 :
        data=data.split(",")
        return data
    else:
        string =""
        for i in data:
            string=string+i+','
        return string[:-1]

def link_mysql():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            database = 'website',
            user = 'root',
            password = 'mysql'
        )
        
    except Error as e:
        print('database error :',e)
    return connection
if __name__=="__main__":
    app.run(debug=True,port=3000,threaded=True)
