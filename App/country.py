#Define all functions related to Countries API

from flask import Flask, request, jsonify
import Services

def getCountries():
    results = Services.allCountries()

    return jsonify(results)