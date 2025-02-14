from flask import Flask, render_template
from mysqlPython import createConnection
from dbservice import formatter
#print(__name__)
app =Flask(__name__)

@app.route("/aks")
def main():
    conn = createConnection()
    cursor=conn.cursor()
    cursor.execute("select * from customer_table")
    data = cursor.fetchall()
    result=formatter(cursor=cursor,data=data)
    return result

    #return render_template("index.html")

if __name__== "__main__" :
    app.run(debug = True)
    