
from crypt import methods
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
    print(response.json()['foods'])
    for i in range(0,2):
        data = {
            'name': result[i]['description'],
            'Nutrients':result[i]['foodNutrients'][i]

        }
        print("New Ingredient start here")
        print(result[i]['description'])
        print(result[i]['foodNutrients'][i])
        print("hello")
        
    return render_template('dashboard.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)