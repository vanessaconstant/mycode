#!/usr/bin/env python3

""" FoodLoop Web Application | VConstant
    File handles all the forms for the application"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateField, PasswordField)
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """Form allos users to search for food"""
    food = StringField()
    submit = SubmitField('Search')

class UserForm(FlaskForm):
    """For allows users to register for an account"""
    fname = StringField("First Name: ", validators=[DataRequired()])
    lname = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    """ Form allows users to login to the application if they are already registered """
    email = StringField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddFoodForm(FlaskForm):
    """Form allows users to add food by date"""
    date = DateField("Date: ", validators=[DataRequired()])
    submit = SubmitField('Add Food')

class ChooseDateForm(FlaskForm):
    """Form allows users to filter their daily food log by date"""
    date_selected = DateField("Date: ", validators=[DataRequired()])
    submit = SubmitField('Search')
    