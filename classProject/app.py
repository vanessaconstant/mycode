
from crypt import methods
from flask import Flask, render_template, redirect, request, session
import requests

app = Flask(__name__)



@app.route('/')
def index():
    
    return render_template('index.html', name=name )

@app.route('/searchPage')
def searchPage():

    return render_template('searchPage.html')


@app.route('/search', methods=['GET','POST'])
def search():

    
    food = request.form['food']


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
    print(result)
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
       
    return render_template('searchPage.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)


    # {{form.hidden_tag()}}
    #               {{form.ingr.label}} {{form.ingr}}
    #               {{form.submit()}}