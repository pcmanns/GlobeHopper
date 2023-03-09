#Define all functions related to Countries API

from flask import Flask, request, jsonify
import Services
#Converted a list to dict
def get_countries():
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

def get_country(continent):
    results = Services.get_country(continent)
    data = []
    for row in results:
        data.append({
            "CountryId": row[0],
            "Name": row[1],
            "Population":row[2],
            "Continent":row[3]
        })

    return jsonify(data)

def get_captital(country_name):
    results = Services.get_country_captital(country_name)
    data=[]
    for row in results:
        data.append({
            "CityId":row[0],
            "Name":row[1],
            "CountryId":row[2],
            "Capital":row[3],
            "FirstLandmark":row[4],
            "SecondLandmark":row[5],
            "ThirdLandmark":row[6]
        })

    return jsonify(data)


def create_country(data):
    Services.create_country(data)
    return jsonify({'message':'Data inseted successfully'})


def update_country(country_id,data):
    Services.update_country(country_id,data)
    return jsonify({'message':'Data update successfully'})

def delete_country(country_id):
    Services.delete_country(country_id)
    return jsonify({'message':'Country_id '+country_id+' deleted successfully'})
 