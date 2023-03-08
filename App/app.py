#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country
import city

app = Flask(__name__)

#GET Api
@app.get('/countries')
def get_all_countries():
    return country.get_countries()

#Create POST API
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

#GET Api
@app.get('/cities')
def get_all_city():
    return city.get_cities

#Create POST API
@app.post('/cities')
def create_city():
    data = request.json
    return city.create_city(data)

@app.put('/cities/<country_id>')
def update_city(city_id):
    data = request.json
    return city.update_city(city_id,data)

@app.delete('/cities/<country_id>')
def delete_city(city_id):
    return city.delete_city(city_id)



#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)