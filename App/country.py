#Define all functions related to Countries API

from flask import Flask, request, jsonify
import Services

def getCountries():
    results = Services.all_countries()

    return jsonify(results)