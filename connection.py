import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="indes"
  )
except:
  print("\033[31m[ COULDN'T CONNECT TO THE DATABASE ]\033[0m")