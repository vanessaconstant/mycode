
from crypt import methods
from flask import Flask, render_template, redirect, request, session
import requests
import os
from flask_sqlalchemy import SQLAlchemy
import forms
from models import user




app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is a secret'

#DATABASE
# setting up the database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)


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
        form.food.data = ''

    #Setting up API call
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
    
    #empty list to capture all 10 results
    resultList = []
   
    #print(result)
    for i in range(0,10):
        
        data = {
            'Name': result[i]['food_name'],
            'Serving Unit':f"{result[i]['serving_qty']} {result[i]['serving_unit']}",
            'Protein':result[i]['full_nutrients'][0]['value'] ,
            'Fat':result[i]['full_nutrients'][1]['value'],
            'Carbohydrate': result[i]['full_nutrients'][2]['value'],
            'Calorie': result[i]['full_nutrients'][4]['value']

        }
        
        resultList.append(data)
     
    
    results = resultList
       
    return render_template('searchPage.html', results=results, form=form, food= food)

@app.route('/register', methods=['GET','POST'])
def register():
    db.create_all()
    form2 = forms.UserForm()

    if form2.validate_on_submit():
        new_user = user.User(form2.fname.data, form2.lname.data, form2.email.data)

        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form2)   


if __name__ == '__main__':
    app.run(debug=True)


    