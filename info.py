# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:28:31 2020

@author: USER
"""

import sqlite3
import sys
connection = sqlite3.connect("login.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,sex TEXT NOT NULL,age INTEGER NOT NULL,weight INTEGER NOT NULL,height INTEGER NOT NULL,password TEXT NOT NULL)")
connection.commit()

query=input('Welcome\nEnter "Log in" if you already have an account,else enter "Register". ')
if query=="Register":
    while True:
        name=input("Enter your username. ")
        n=cursor.execute('SELECT name FROM login').fetchone()
        n=str(n).strip("('',)'")
        if n==name:
            print('That username already exists,try another one!')
            continue
        else:
            while True:
                email=input("Enter your email. ")
                m=cursor.execute('SELECT email FROM login').fetchone()
                m=str(m).strip("('',)'")
                if m == email:
                    print('That email is already in our database,enter another one!')
                    continue
                else:
                    while True:
                          sex=input("Enter your sex. ")
                          age=input("Enter your age. ")
                          height=input("Enter your height. ")
                          weight=input("Enter your weight. ")
                          password=input("Enter your password. ")
                          rpassword=input("Enter your password again. ")
                          if password ==rpassword:
                                 cursor.execute('INSERT INTO login VALUES(?,?,?,?,?,?,?,?)',
                                            (None, name, email, sex, age, weight, height, password))
                                 connection.commit()
                                 print('You are now registered.')
                                 sys.exit()

                          else:
                              print('Password does not match')
                              continue
                   

elif query=="Log in":
    while True:
        name = input("Enter your username. ")
        password=input("Enter your password. ")
        n=cursor.execute("SELECT name from login WHERE name='"+name+"'").fetchone()
        n = str(n).strip("('',)'")
        if n==name:
            pw = cursor.execute("SELECT password from login WHERE password='" + password + "'").fetchone()
            pw = str(pw).strip("('',)'")
            if pw==password:
                print('You are now logged in.')
                exec(open(r"talk.py").read())
                break
            else:
                print('Wrong password.')
        else:
            print('Wrong username.')
else:
    print('Incorrect input.Run script again. ')
connection.close()
