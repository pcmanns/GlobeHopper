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

def create_country(data):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid=data["CountryId"]
    name=data["Name"]
    populatiion=data["Population"]
    continent=data["Continent"]
    
    mysql="INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values=(countryid,name,populatiion,continent)
    mycursor.execute(mysql,values)
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    
def update_country(country_id,data):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid=country_id
    name=data["Name"]
    populatiion=data["Population"]
    continent=data["Continent"]
    
    mysql="UPDATE Country SET  Name=%s, Population=%s, Continent=%s WHERE CountryId=%s"
    values=(name,populatiion,continent,countryid)
    mycursor.execute(mysql,values)
    
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    
def delete_country(country_id):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    mysql="DELETE FROM Country WHERE CountryId=%s"
    values=(country_id)
    mycursor.execute(mysql,values)
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()