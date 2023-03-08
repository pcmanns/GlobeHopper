#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country

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


#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)