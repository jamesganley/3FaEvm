#!/usr/bin/env python
import tkinter as tk
import MySQLdb
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

db = MySQLdb.connect(host="localhost",user="jgan",passwd="1234",db="EVM")
cur = db.cursor()

reader = SimpleMFRC522()

try:
    Token, text = reader.read()
    Token = str(Token)

    print(Token)
    print(text)
    #cur.execute("Select Name FROM test WHERE Rfid = (%s)",(Token))
    #for row in cur.fetchall():
        #Math = (row[0])
    if Token == '935539098035':
        print("welcome James")
    else:
        print("Welcome Bob")
finally:
    GPIO.cleanup()