import mysql.connector




datalist = []
def database(nome,prod,idd):
  datarow = (nome,prod,idd)
  datalist.append(datarow)

def inserdata():
  mydb = mysql.connector.connect(
  host="localhost",
  user="diogo",
  password="379226",
  database="pydatabase"
  )
  mycursor = mydb.cursor()
  sql = "INSERT INTO databasesolar (fornecedor, produto,nfserie) VALUES (%s, %s,%s)"
  mycursor.executemany(sql,datalist)
  mydb.commit()
  print(mycursor.rowcount, "was inserted.") 

  

    








