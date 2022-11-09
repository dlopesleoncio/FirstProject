import mysql.connector
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True



datalist = []
def database(nome,prod,idd):
  datarow = (nome,prod,idd)
  datalist.append(datarow)


mydb = mysql.connector.connect(
host="localhost",
user="diogo",
password="379226",
database="pydatabase"
)

def inserdata():
  mycursor = mydb.cursor()
  sql = "INSERT INTO databasesolar (fornecedor, produto,nfserie) VALUES (%s, %s,%s)"
  mycursor.executemany(sql,datalist)
  mydb.commit()
  print(mycursor.rowcount, "was inserted.")

@app.route("/",methods=['GET', 'POST'])
def index():
  name = request.form.get("name")
  mycursor = mydb.cursor()
  mycursor.execute("SELECT fornecedor FROM databasesolar WHERE fornecedor LIKE '%WEG%'")
  #mycursor.execute("SELECT fornecedor FROM databasesolar WHERE fornecedor LIKE '%WEG%'",(name,))

  myresult = mycursor.fetchall()
  return render_template("index.html",dados=myresult,name1=name)


if __name__ == __name__:
  app.debug=True
  app.run(host = '0.0.0.0',port=5000)

    








