#!/usr/bin/env python3
"""TLG Cohort | Vconstant
    File managing routing and functionality for the website"""

from crypt import methods
from flask import Flask, render_template, redirect, request, session, flash
import requests
import os
from flask_sqlalchemy import SQLAlchemy
import forms
from models import User, FoodItem
from __init__ import app, db
from flask_bcrypt import Bcrypt
from datetime import date


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
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session:
        return redirect('/')

    login_user = User.query.get(session['users_id'])
    name = login_user.fname

    form5 = forms.ChooseDateForm()
    date_input = form5.date_selected.data
    print(date_input)

    date_selected = False

    if(date_input):
        date_selected = date_input
        print("the input ran")
        print(date_selected)
    else:
        date_selected = date.today()
        print("todays date ran")

   
   
    food_log = daily_food_log(date_selected)
    
    return render_template('dashboard.html', name=name, 
    userFoodList=food_log[0], 
    totals=food_log[1], form5=form5)

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
        session['users_id'] = login_user.id
        
        if(bcrypt.check_password_hash(login_user.password, password)):
            todays_date = date.today()
            return redirect(f'/dashboard/{todays_date}')      

    return render_template('login.html', form3=form3)  

#Logout functionality
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#Detailed Food Info Page
@app.route('/view/<food>')
def foodDetail(food):

    form4 = forms.AddFoodForm()

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


    return render_template("detailedView.html", data=data, form4=form4)

@app.route('/addedFood/<food>', methods=['GET', 'POST'])
def addFood(food):

    form4 = forms.AddFoodForm()
    print(food)
    date_logged =form4.date.data

    result = apiCall(food)
    print(result)


    data = {
    
            'Name': result[0]['food_name'],
            'Protein':round(result[0]['full_nutrients'][0]['value'], 2) ,
            'Fat':round(result[0]['full_nutrients'][1]['value'], 2),
            'Carbohydrate': round(result[0]['full_nutrients'][2]['value'], 2),
            'Calorie': round(result[0]['full_nutrients'][4]['value'], 2),
            'date_logged':date_logged,
            'user_id': session['users_id']

        }

    addedfood = FoodItem(data['Name'], data['Calorie'], data['Carbohydrate'], data['Protein'], data['Fat'],data['date_logged'], data['user_id'])
    db.session.add(addedfood)
    db.session.commit()


    return redirect('/dashboard')


#Deleting food from food log
@app.route('/delete/<food>', methods=['GET', 'POST'])
def delete_food(food):
    food_to_delete = FoodItem.query.get(food)
    db.session.delete(food_to_delete)
    db.session.commit()
    
    return redirect('/dashboard')

# Daily log function returns food log by selected date

def daily_food_log(date_selected):

    userFoodList = FoodItem.query.join(User.foodList).filter(User.id==session['users_id'],
    FoodItem.date_logged==date_selected).all()
    sumCalorie = []
    sumCarb = []
    sumPro = []
    sumFat = []

    for fooditem in userFoodList:
        sumCalorie.append(fooditem.calorie)
        sumCarb.append(fooditem.carbs)
        sumPro.append(fooditem.protein)
        sumFat.append(fooditem.fat)

   

    # Adding the totals
    totals = ['Total', round(sum(sumCalorie),2), round(sum(sumCarb),2), round(sum(sumPro),2), round(sum(sumFat),2), '']
  
    daily_log = [userFoodList, totals]

    return daily_log

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


    