#Define all functions related to Countries API

from flask import Flask, request, jsonify
import Services
#Converted a list to dict

def get_cities():
    results = Services.all_cities()
    data = []
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

def create_city(data):
    Services.create_city(data)
    return jsonify({'message':'Data inseted successfully'})


def update_city(city_id,data):
    Services.update_city(city_id,data)
    return jsonify({'message':'Data update successfully'})


def delete_city(city_id):
    Services.delete_city(city_id)
    return jsonify({'message':'City_id '+city_id+' delete successfully'})