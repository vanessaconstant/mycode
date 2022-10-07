#!/usr/bin/env python3
""" FoodLoop Web Application | VConstant
    File handles all the forms for the application"""

from datetime import date
from flask import Flask, render_template, redirect, session, flash
import requests
from flask_sqlalchemy import SQLAlchemy
import forms
from models import User, FoodItem
from __init__ import app, db
from flask_bcrypt import Bcrypt

#This call initializes the object that will be hashing the passwords
bcrypt = Bcrypt()

@app.before_first_request
def create_tables():
    """This function initializes the database"""
    db.create_all()

#ROUTES
# Index Page route
@app.route('/')
def index():  
    """This function routes to the index page"""
    return render_template('index.html')

# Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """This function routes to the index page"""
    if not session:
        return redirect('/')

    #grabbing the name to welcome the user
    login_user = User.query.get(session['users_id'])
    name = login_user.fname

    #This form let's the user filter their food log by date
    form5 = forms.ChooseDateForm()
    date_input = form5.date_selected.data
    
    #initializes date selected 
    ##then sets date to current date if user did not select a date yet
    #filters to the selected date once users uses the form
    date_selected = False

    if(date_input):
        date_selected = date_input
        print(date_selected)
    else:
        date_selected = date.today()
        print("todays date ran")

    #displays date in a user friendly format
    display_date = date_selected.strftime("%A %B %d %Y")
    
    #calls the function that filters the logs by date
    food_log = daily_food_log(date_selected)
    
    return render_template('dashboard.html', name=name, 
    user_food_list=food_log[0], 
    totals=food_log[1], form5=form5, display_date=display_date)

# Search Page
@app.route('/searchPage')
def search_page():
    """This function routes to the search page"""

    form = forms.SearchForm()

    return render_template('searchPage.html', form=form)

#Search functionality calling API and giving results
@app.route('/search', methods=['GET','POST'])
def search():
    """This function allows the user to search for foods"""
    form = forms.SearchForm()

    if form.validate_on_submit():
        food = form.food.data
        form.food.data = ''

    #calling api function
    result = api_call(food)

    #crate empty list to capture all 10 results
    result_list = []
   
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
        
        result_list.append(data)
       
    return render_template('searchPage.html', result_list=result_list, form=form, food= food)

#Registration page
@app.route('/register', methods=['GET','POST'])
def register():
    """This function allows the user to register for an account"""
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
    """This function logs the user in."""

    #This is the login form grabs the email and password
    form3 = forms.LoginForm()
    email = form3.email.data
    password = form3.password.data

    if form3.validate_on_submit():
        #if user enters wrong username or password they will get error message
        #they will be redirected to login page again.
        if User.query.filter_by(email=email).first() is None:
            flash('Please enter a valid user name and password.', 'login')
            return redirect('/login')
        login_user= User.query.filter_by(email=email).first()
        session['users_id'] = login_user.id
        
        #passwords are hashed 
        #this method is checking the inputed password matches
        #the stored hashed password
        if(bcrypt.check_password_hash(login_user.password, password)):
            return redirect('/dashboard')
        else:
            flash('Please enter a valid user name and password.', 'login')      

    return render_template('login.html', form3=form3)  

#Logout functionality
@app.route('/logout')
def logout():
    """This function logs out the user by clear the session"""
    session.clear()
    return redirect('/')

#Detailed Food Info Page
@app.route('/view/<food>')
def food_detail(food):
    """ This function routes the user 
        to a more detailed view page"""

    #form to log the food to a specific date
    form4 = forms.AddFoodForm()

    #api call for that food that was selected in the search page
    result = api_call(food)
   
   #formatting the data received from the api call into a dictionary
   #only grabbing the first item.
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
def add_food(food):
    """This function adds the food to the food log"""
   
    #generates the form
    form4 = forms.AddFoodForm()
    date_logged =form4.date.data

    #api call to grab the food chosen to store it in the db
    result = api_call(food)
   
    #formating the data received from the api call
    data = {
    
            'Name': result[0]['food_name'],
            'Protein':round(result[0]['full_nutrients'][0]['value'], 2) ,
            'Fat':round(result[0]['full_nutrients'][1]['value'], 2),
            'Carbohydrate': round(result[0]['full_nutrients'][2]['value'], 2),
            'Calorie': round(result[0]['full_nutrients'][4]['value'], 2),
            'date_logged':date_logged,
            'user_id': session['users_id']

        }

    #addingt the food to the data base
    added_food = FoodItem(data['Name'], data['Calorie'], data['Carbohydrate'], data['Protein'], data['Fat'],data['date_logged'], data['user_id'])
    db.session.add(added_food)
    db.session.commit()

    return redirect('/dashboard')


#Deleting food from food log
@app.route('/delete/<food>', methods=['GET', 'POST'])
def delete_food(food):
    """This function deletes food from the food log
        and removes it from the db"""
    food_to_delete = FoodItem.query.get(food)
    db.session.delete(food_to_delete)
    db.session.commit()
    
    return redirect('/dashboard')

# Daily log function returns food log by selected date

def daily_food_log(date_selected):
    """This function returns the food log by selected date"""

    user_food_list = FoodItem.query.join(User.foodList).filter(User.id==session['users_id'],
    FoodItem.date_logged==date_selected).all()
    sum_calorie = []
    sum_carb = []
    sum_pro = []
    sum_fat = []

    for food_item in user_food_list:
        sum_calorie.append(food_item.calorie)
        sum_carb.append(food_item.carbs)
        sum_pro.append(food_item.protein)
        sum_fat.append(food_item.fat)

    # Adding the totals
    totals = ['Total', round(sum(sum_calorie),2), round(sum(sum_carb),2), round(sum(sum_pro),2), round(sum(sum_fat),2), '']
  
    daily_log = [user_food_list, totals]

    return daily_log

#creating apicall function for reusability
def api_call(food):
    """This function calls the api"""
    base_url = "https://trackapi.nutritionix.com/v2/search/instant"

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


    