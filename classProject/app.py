
from crypt import methods
from unittest import result
from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    name = "jose"
    return render_template('index.html', name=name )

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/search', methods=['POST'])
def search():

    ingr = "orange"
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY"
    key = "DEMO_KEY"
    headers = {
        "Authorization": key
    }
    params = {
        "query": ingr
    }

    response = requests.get(base_url, params=params)

    result = response.json()['foods']
    resultList = []
   
    for i in range(0,10):
        data = {
            'Name': result[i]['description'],
            'Protein':result[i]['foodNutrients'][0]['value'],
            'Fat':result[i]['foodNutrients'][1]['value'],
            'Carbohydrate': result[i]['foodNutrients'][2]['value'],
            'Calorie': result[i]['foodNutrients'][3]['value']

        }
        type(resultList)
        resultList.append(data)
        print(resultList)
        print(result[0]['foodNutrients'][0]['value'])
        # protein, fat, carbs, calories
        print("New Ingredient start here")
    print(resultList)
    results = resultList
        # print(result[i]['foodNutrients'][i])
        # print("hello")
        
    return render_template('dashboard.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)