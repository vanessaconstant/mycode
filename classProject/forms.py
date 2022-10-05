from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):

    food = StringField()
    submit = SubmitField('Search')

class UserForm(FlaskForm):
    fname = StringField("First Name: ", validators=[DataRequired()])
    lname = StringField("Last Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    
    email = StringField("Email: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField('Submit')