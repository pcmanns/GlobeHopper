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


#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)