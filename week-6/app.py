import mysql.connector
from mysql.connector import Error
from flask import Flask ,redirect,url_for ,render_template , request , session 
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "usertest"

@app.route("/")
def index():
    name = session.get('name')
    if name != None:
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
    
    sql = " select name ,username , password  from member where username = '{}' ; ".format(username)
    cursor.execute(sql)
    all_username = cursor.fetchall()
    cursor.close()
    connection.close()

    if all_username == [] or all_username[0][2] != password :
        error_message = "帳號、密碼輸入錯誤"
        return redirect(url_for("error",message=error_message))

    name = all_username[0][0]
    session['name'] = name
    return redirect("member")


@app.route("/member")
def member():
    name = session.get('name')
    if name != None:
       return render_template("member.html",name=name)
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
    elif data == None:
        return None    
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
