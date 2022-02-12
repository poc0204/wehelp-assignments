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
        return redirect("member")
    else:
        return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    password = request.form["password"]
    username = request.form["username"]
    password = request.form["password"]
    connection = link_mysql()
    cursor = connection.cursor()
    sql = " select username from member where username = '{}' ; ".format(username)
    cursor.execute(sql)
    all_username = cursor.fetchall()
    if all_username == []:
        sql = " insert into member (name ,username ,password) values ('{}' ,'{}' ,'{}');".format(name,username,password)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()    
        return redirect("/")
    error_message = "帳號已經被註冊"
    return redirect(url_for("error",message=error_message))



@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    connection = link_mysql()
    cursor = connection.cursor()
    sql = " select username from member where username = '{}' ; ".format(username)
    cursor.execute(sql)
    all_username = cursor.fetchall()
    sql = " select password from member where password = '{}' ; ".format(password)
    cursor.execute(sql)
    all_password = cursor.fetchall()
    cursor.close()
    connection.close()
    print(all_username)
    print("password",all_password)
    if all_username == [] or all_password == []:
        error_message = "帳號、密碼輸入錯誤"
        return redirect(url_for("error",message=error_message))

    session['username'] = username
    return redirect("member")


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
    else:
        return redirect("/")
        


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
