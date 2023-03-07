#Starting point of our WebApp - main
#pip install Flask

from flask import Flask, request, jsonify
import country

app = Flask(__name__)

#read Api
@app.get('/countries')
def getAllCountries():
    return countries.getCountries()


#Execute on the terminal
if __name__ == '__main__':
    app.run()