#Define all services for accessing database for country and city

from flask import Flask, request, jsonify
import conn

def get_country(continent):
    #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()
    
    #Excecute SQL
    mycursor.execute("SELECT * FROM globehopper.country WHERE Continent =%s",[continent])
    results = mycursor.fetchall()
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    return results


def get_country_captital(country_name):
    #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()
    
    #Excecute SQL
    mycursor.execute("SELECT * FROM city WHERE Capital = 1 and countryId=(select countryId FROM country WHERE Name=%s);",[country_name])
    results = mycursor.fetchall()
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    return results

#Country CRUD
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

    name=data["Name"]
    populatiion=data["Population"]
    continent=data["Continent"]
    
    mysql="INSERT INTO Country (Name, Population, Continent) VALUES (%s, %s, %s)"
    values=(name,populatiion,continent)
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

    countryid=[country_id]
    mysql="DELETE FROM Country WHERE CountryId=%s"
    values=(countryid)
    mycursor.execute(mysql,values)
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()




#City CURD
def all_cities():
    #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()
    
    #Excecute SQL
    mycursor.execute("SELECT * FROM globehopper.city")
    results = mycursor.fetchall()
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    return results


def create_city(data):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    name=data["Name"]
    countyid=data["CountryId"]
    capital=data["Capital"]
    firstlandmark=data["FirstLandmark"]
    secondlandmark=data["SecondLandmark"]
    thirdlandmark=data["ThirdLandmark"]
    
    mysql="INSERT INTO City (Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES(%s, %s, %s, %s, %s, %s)"
    values=(name,countyid,capital,firstlandmark,secondlandmark,thirdlandmark)
    mycursor.execute(mysql,values)
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    
def update_city(city_id,data):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid=city_id
    name=data["Name"]
    countyid=data["CountryId"]
    capital=data["Capital"]
    firstlandmark=data["FirstLandmark"]
    secondlandmark=data["SecondLandmark"]
    thirdlandmark=data["ThirdLandmark"]
    
    mysql="UPDATE city SET Name=%s, CountryId=%s, Capital=%s, FirstLandmark=%s, SecondLandmark=%s, ThirdLandmark=%s WHERE cityId=%s"
    values=(name,countyid,capital,firstlandmark,secondlandmark,thirdlandmark,cityid)
    
    mycursor.execute(mysql,values)
    
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()
    
def delete_city(city_id):
     #Open Connections
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid=[city_id]
    mysql="DELETE FROM city WHERE cityId=%s"
    values=(cityid)
    mycursor.execute(mysql,values)
    
    #Close Connections
    mycursor.close()
    conn.myconn.close()