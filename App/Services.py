#Define all services for accessing database for country and city

from flask import Flask, request, jsonify
import conn


def all_countries():
    #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()
    
    #Excecute SQL
    mycursor.execute("SELECT * FROM globehopper.country")
    results = mycursor.fetchall()
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    return results