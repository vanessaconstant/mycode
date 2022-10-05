from datetime import datetime
from enum import unique
from flask import Flask
from __init__ import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable = False)
    lname = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), unique= True)
    date_added = db.Column(db.DateTime, default= datetime.utcnow)

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __repr__(self):
        return f"User's name is {self.fname} {self.lname}"

    

