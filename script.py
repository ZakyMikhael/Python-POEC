#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector, random

conn = mysql.connector.connect(host="localhost",user="root",password="", database="test")
cursor = conn.cursor(buffered=True)

def initTables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS groupe
        (
           id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
           nom VARCHAR(100)
        );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateur
    (
       id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
       nom VARCHAR(100),
       prenom VARCHAR(100),
       email VARCHAR(255),
       date_naissance DATE,
       pays VARCHAR(255),
       ville VARCHAR(255),
       code_postal VARCHAR(5),
       telephone VARCHAR(30)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateur_groupe (
        id int(11) PRIMARY KEY AUTO_INCREMENT, 
        utilisateur_id int NOT NULL, 
        groupe_id int NOT NULL, 
        FOREIGN KEY(utilisateur_id) REFERENCES utilisateur(id), 
        FOREIGN KEY(groupe_id) REFERENCES groupe(id)
      );
    """)

    cursor.execute("""SET FOREIGN_KEY_CHECKS=0""")
    cursor.execute("""TRUNCATE TABLE groupe""")
    cursor.execute("""TRUNCATE TABLE utilisateur""")
    cursor.execute("""TRUNCATE TABLE utilisateur_groupe""")
    cursor.execute("""SET FOREIGN_KEY_CHECKS=1""")
    return cursor

cursor = initTables(cursor)
groupeNames = ["Les fous", "Les maîtres de la chèvre", "Les chats", "les chiens", "Batman", "Superman", "Green Lanterne", "Flash"]

for name in groupeNames:
    list = (name,)
    cursor.execute("""INSERT INTO groupe (nom) VALUES (%s)""", list)

conn.commit()

names = ["Adam", "Alex", "Alexandre", "Alexis", "Anthony", "Antoine", "Benjamin", "Cédric"]
firstnames = ["Laurence", "Laurie", "Léa", "Léanne", "Maélie", "Maéva", "Maika"]
emails = ["laurence@email.fr", "laurie@email.fr", "lea@email.fr", "leanne@email.fr", "maelie@email.fr", "maeva@email.fr", "maika@email.fr"]
pays = ["France", "USA", "Canada"]
citys = ["Paris", "Tokyo", "New York", "Berlin"]
postalCodes = [75001, 75002, 75003, 65464, 65465, 88888]

i = 0
while i != 100:
    i = i + 1
    user = (random.choice(names),
            random.choice(firstnames),
            random.choice(emails),
            "2010-01-01",
            random.choice(pays),
            random.choice(citys),
            random.choice(postalCodes),
            random.randint(1111111111, 9999999999)
    )

    cursor.execute("""INSERT INTO utilisateur (nom, prenom, email, date_naissance, pays, ville, code_postal, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", user)
    for looping in range(1, random.randint(1, 5)):
        us_gr = [i, looping]
        cursor.execute("""INSERT INTO utilisateur_groupe (utilisateur_id, groupe_id) VALUES (%s, %s)""", us_gr)

conn.commit()
conn.close()