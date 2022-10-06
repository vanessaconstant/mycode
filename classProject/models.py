from datetime import datetime, date
from enum import unique
from flask import Flask
from __init__ import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable = False)
    lname = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), unique= True)
    date_added = db.Column(db.DateTime, default= datetime.utcnow)
    foodList = db.relationship('FoodItem', backref='fooditem', lazy='dynamic')

    def __init__(self, fname, lname, password, email):
        self.fname = fname
        self.lname = lname
        self.password = bcrypt.generate_password_hash(password)
        self.email = email


    def __repr__(self):
        return f"User's name is {self.fname} {self.lname}"
    
    

class FoodItem(db.Model):
    __tablename__ = 'fooditems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calorie = db.Column(db.Float)
    carbs = db.Column(db.Float)
    protein = db.Column(db.Float)
    fat = db.Column(db.Float)
    date_logged = db.Column(db.Date)
    date_added = db.Column(db.DateTime, default= datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, calorie, carbs, protein, fat, date_logged, user_id):
        
        self.name = name
        self.calorie = calorie
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.date_logged = date_logged
        self.user_id = user_id

    def __repr__(self):
        return f"{self.name}"