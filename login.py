from flask import Flask, render_template, request
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
@app.route("/")

def main():
    return render_template(r"login.html")

@app.route("/login", methods = ["POST"])
def login():
    usrn = request.form['username']
    pwd = request.form['password']
    print(usrn, pwd)
    connection = sqlite3.connect(currentdirectory + "\\login.db")
    cur = connection.cursor()
    found = 0
    for row in cur.execute("SELECT username, password from userlogin"):
        userid = row[0]
        password = row[1]
        print(userid, password)
        if userid == usrn and password == pwd:
            found = 1
            break
    if found==1:
        return render_template(r"profile.html")


@app.route("/register", methods = ["POST"])
def register():
    usrn = request.form['newusername']
    pwd = request.form['newpassword']
    eml = request.form['newemail']
    print(usrn, pwd, eml)
    connection = sqlite3.connect(currentdirectory + "\\login.db")
    cur = connection.cursor()
    found = 0
    for row in cur.execute("SELECT username, password, email from userlogin"):
        userid = row[0]
        password = row[1]
        email = row[2]
        if userid == usrn:
            if password == pwd and email==eml:
                return render_template(r"login.html")
        else:
            cur.execute("INSERT INTO userlogin(username, password, email) values (?,?,?)", (usrn,pwd,eml))
            render_template(r"profile.html")

if __name__ == "__main__":
    app.run()