#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
import city

app = Flask(__name__)



#COUNTRY CRUD
@app.get('/countries')
def get_all_countries():
    return country.get_countries()

@app.get('/countries/<continent>')
def get_country(continent):
    return country.get_country(continent)

@app.get('/countries/<country_name>/1')
def get_capital_country(country_name):
    return country.get_captital(country_name)

@app.post('/countries')
def create_county():
    data = request.json
    return country.create_country(data)

@app.put('/countries/<country_id>')
def update_country(country_id):
    data = request.json
    return country.update_country(country_id,data)

@app.delete('/countries/<country_id>')
def delete_country(country_id):
    return country.delete_country(country_id)




#CITY CRUD
@app.get('/cities')
def get_all_city():
    return city.get_cities()

@app.post('/cities')
def create_city():
    data = request.json
    return city.create_city(data)

@app.put('/cities/<city_id>')
def update_city(city_id):
    data = request.json
    return city.update_city(city_id,data)

@app.delete('/cities/<city_id>')
def delete_city(city_id):
    return city.delete_city(city_id)



#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)