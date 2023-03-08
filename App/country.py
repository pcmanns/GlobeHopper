#Define all functions related to Countries API

from flask import Flask, request, jsonify
import Services
#Converted a list to dict
def getCountries():
    results = Services.all_countries()
    data = []
    for row in results:
        data.append({
            "CountryId": row[0],
            "Name": row[1],
            "Population":row[2],
            "Continent":row[3]
        })

    return jsonify(data)

def create_country(data):
    Services.create_country(data)
    return jsonify({'message':'Data inseted successfully'})