#!/usr/bin/python3


import mysql.connector
import random

conn = mysql.connector.connect(host="localhost",user="root",password="", database="test")
cursor = conn.cursor()

cursor.execute("""

  
CREATE TABLE IF NOT EXISTS utilisateur (
   id INT PRIMARY  KEY NOT NULL,
  nom VARCHAR(100),
  prenom VARCHAR(100),
  email VARCHAR(255),
  date_naissance date,
  pays VARCHAR(255),
  ville VARCHAR(255),
  code_postal VARCHAR(5)
);
""")
names = ["Mike", "Ess", "Kali", "Ali", "Ahmed","Change","Pedro", "Nabil", "Ashraf", "Léon", "Romain", "Pierre"]
firstnames = ["EST", "POUDRE", "KEVIN", "GENA", "ALLA", "ALAIN"]
emails = ["llll@mmmm.com", "fgdfgdf.rterter.com", "zerzerzer@hrtpytyrt.com"]
pays = ["France", "TOKYO", "USA"]
citys = ["Paris", "CAIRE", "NEW YORK"]
postalcodes = ["97001", "75018"]
i = 0
while i !=5000:
    i = i + 1
    user = (i, random.choice(names), random.choice(firstnames), random.choice(emails), "2010-01-01", random.choice(pays), random.choice(citys),random.choice(postalcodes))
    cursor.execute("""INSERT INTO utilisateur (id,nom, prenom, email, date_naissance, pays, ville, code_postal) VALUES(%s,%s, %s, %s, %s, %s, %s, %s)""", user)

conn.commit()
print (conn)
conn.close()
