#!/usr/bin/python3

import mysql.connector
import random

db=mysql.connector.connect (host="localhost", user="root", password="")
cursor=db.cursor()

cursor.execute("""
CREATE TABLE vivisteur (
  id INT PRIMARY KEY NOT NULL ,
  nom VARCHAR (100),
  prenom VARCHAR (100),
  age VARCHAR (100)
);
""")
db.commit