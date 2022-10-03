from flask import*
import sqlite3

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add")
def add():
    return render_template("save.html")
@app.route("/save",methods=["POST","GET"])
def save():
    msg="msg"
    if request.method =="POST":
        try:
            name=request.form["name"]
            age=int(request.form["age"])
            with sqlite3.connect(r"C:\Users\ELCOT\PycharmProjects\trining\flask_db\stu10.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into talent (name,age) values (?,?)",
                            (name,age))
                con.commit()
                msg = "student successfully Added"
        except:
            con.rollback()
            msg="canot add student list"
        finally:
            return render_template("sucess.html", msg=msg)
@app.route("/view")
def view():
    con = sqlite3.connect(r"C:\Users\ELCOT\PycharmProjects\trining\flask_db\stu10.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from talent")
    rows = cur.fetchall()
    print(rows)
    return render_template("view.html", rows=rows)


if __name__=="__main__":
    app.run(debug=True)
