#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
from datetime import datetime
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager 
from flask import Flask, jsonify, render_template, request,session,redirect, url_for
import json
import database_api

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = 'cheie_secreta'



current_date = datetime.now()
format_date = current_date.strftime("%Y-%m-%d")   
print(f"Data de astazi este {format_date}")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data",methods=["GET", "POST"])
def get_data():
    departure = session.get('departure')
    arrival = session.get("arrival") 
    data_decolarii = session.get("data_decolarii")
    nr_persoane = session.get("nr_persoane")
    departure_code = FlightSearch().findIataCodeByCity(departure)
    arrival_code = FlightSearch().findIataCodeByCity(arrival) 
    flightObject = FlightData(departure_code, arrival_code, data_decolarii, nr_persoane) 
    flight_prices_file =flightObject.request_for_flight_price() 
    the_cheapest_flight = flightObject.find_cheapes_flight(flight_prices_file)
    
    #save the data for SQL DataBase 
    cabin = flight_prices_file["data"][0]["travelerPricings"][0]["fareDetailsBySegment"][0]["cabin"]  
    session["cabin"] = cabin
    price = flight_prices_file["data"][0]["price"]["total"] 
    session["price"] = price
    return render_template("data.html", flightObject = the_cheapest_flight[0], cabinType = the_cheapest_flight[1], departure = departure[0], arrival = arrival[0])

@app.route("/save_entry", methods=["POST"])
def save_entry():
    departure = session.get('departure')
    arrival = session.get("arrival") 
    cabin = session.get('cabin')
    price = session.get('price')
    database_entry = database_api.database_api()
    database_entry.add_new_entry(departure[0], arrival[0], price, cabin)
    return redirect(url_for('get_data'))

@app.route("/all_entrys", methods=["POST"])
def show_all_entrys(): 
    database_obj = database_api.database_api()
    all_entrys = database_obj.show_database_inputs() 
    print("Asta")
    print(all_entrys)
    return render_template("all_entrys.html", obj = all_entrys)
    
    
@app.route("/all_flights",methods=["POST"])
def get_all_flights():
    session["departure"] =  request.form['departure'],
    session["arrival"] = request.form['arrival'],
    session["data_decolarii"] = request.form['data_decolarii'], 
    session["nr_persoane"] = request.form['nr_persoane']
    flight = { 
              "departure": request.form['departure'],
              "arrival":request.form['arrival'],
              "data_decolarii":request.form['data_decolarii'], 
              "nr_persoane":request.form['nr_persoane']
              }
    departure_code = FlightSearch().findIataCodeByCity(flight["departure"])
    arrival_code = FlightSearch().findIataCodeByCity(flight["arrival"]) 
    flightObject = FlightData(departure_code, arrival_code, flight["data_decolarii"], flight["nr_persoane"]) 
    flight_prices_file =flightObject.request_for_flight_price() 
    list_flies = flightObject.format_flights(flight_prices_file)
    return render_template("all_flights.html", list_flights = list_flies)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000,debug=True) 
    
    