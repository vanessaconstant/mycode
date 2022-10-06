
from crypt import methods
from unittest import result
from flask import Flask, render_template, redirect, request, session, flash
import requests
import os
from flask_sqlalchemy import SQLAlchemy
import forms
from models import User
from __init__ import app, db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()



@app.before_first_request
def create_tables():
    db.create_all()


#ROUTES
# Index Page route
@app.route('/')
def index():

    return render_template('index.html')


# Dashboard Page
@app.route('/dashboard')
def dashboard():


    return render_template('dashboard.html')

# Search Page
@app.route('/searchPage')
def searchPage():
    form = forms.SearchForm()

    return render_template('searchPage.html', form=form)

#Search functionality calling API and giving results
@app.route('/search', methods=['GET','POST'])
def search():

    form = forms.SearchForm()

    if form.validate_on_submit():
        food = form.food.data
        print(food)
        form.food.data = ''

    #calling api function
    result = apiCall(food)

    #crate empty list to capture all 10 results
    resultList = []
   
    #print(result)
    for i in range(0,10):
        
        data = {
            'Name': result[i]['food_name'],
            'Serving Unit':f"{result[i]['serving_qty']} {result[i]['serving_unit']}",
            'Protein':round(result[i]['full_nutrients'][0]['value'], 2) ,
            'Fat':round(result[i]['full_nutrients'][1]['value'], 2),
            'Carbohydrate': round(result[i]['full_nutrients'][2]['value'], 2),
            'Calorie':round(result[i]['full_nutrients'][4]['value'], 2)

        }
        
        resultList.append(data)
     
    
    results = resultList
       
    return render_template('searchPage.html', results=results, form=form, food= food)

#Registration page
@app.route('/register', methods=['GET','POST'])
def register():
    
    
    form2 = forms.UserForm()
    fname = form2.fname.data
    print(fname)

    if form2.validate_on_submit():
        
        new_user = User(form2.fname.data, form2.lname.data,form2.password.data, form2.email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', form2=form2)   

#Login Page 
@app.route('/login', methods=['GET','POST'])
def login():

    form3 = forms.LoginForm()
    email = form3.email.data
    password = form3.password.data

    if form3.validate_on_submit():
        login_user= User.query.filter_by(email=email).first()
        print(login_user.id)
        if(bcrypt.check_password_hash(login_user.password, password)):
            print('password match')
            return redirect('/dashboard')      

    return render_template('login.html', form3=form3)  



#Detailed Food Info Page
@app.route('/view/<food>')
def foodDetail(food):

    result = apiCall(food)
    print(result)

    data = {
            'Name': result[0]['food_name'],
            'Serving Unit':f"{result[0]['serving_qty']} {result[0]['serving_unit']}",
            'photo': result[0]['photo']['thumb'],
            'Protein':round(result[0]['full_nutrients'][0]['value'], 2) ,
            'Fat':round(result[0]['full_nutrients'][1]['value'], 2),
            'Carbohydrate': round(result[0]['full_nutrients'][2]['value'], 2),
            'Calorie': round(result[0]['full_nutrients'][4]['value'], 2)

        }


    return render_template("detailedView.html", data=data)


#creating apicall function for reusability
def apiCall(food):
    base_url = "https://trackapi.nutritionix.com/v2/search/instant"
    key = "DEMO_KEY"
    headers = {
        "x-app-id": "fc9be373",
        "x-app-key": "46777694be6e90aec315f750629c276b",
        "Content-Type": "application/json",
        "x-remote-user-id": "0"
    }
    params = {
        "query": food,
        "detailed": "true"
    }

    response = requests.get(base_url, headers=headers, params=params)

   #converting result to a json file. 
    result = response.json()['common']

    return result  



if __name__ == '__main__':
    app.run(debug=True)


    