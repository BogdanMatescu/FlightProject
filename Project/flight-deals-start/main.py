#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
from datetime import datetime
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

API_ENDPOINT = "https://api.sheety.co/2c53948f0e1180c3d9457b9047f4a08e/flightDealsBogdan/prices"

response = requests.get(url=API_ENDPOINT)
sheet_data = response.json()["prices"]



for i in range (len(sheet_data)) : 
    print(sheet_data[i]['iataCode'])
    if sheet_data[i]['iataCode'] == "":
        print(f"Pentru orasul {sheet_data[i]['city']}")
        object1 = FlightSearch() 
        new_iata_code = object1.findIataCodeByCity(sheet_data[i]['city'], sheet_data[i])
        DataManager.updateLine(sheet_data[i]["id"], new_iata_code) 
        #DataManager.deleteLine(sheet_data[i]['id'])

depaerture = input ("Plecati de pe aeroportul: ")
destination = input ("Destinatia este in orasul: ")
data_decolarii = input ("Data decolarii este (singurul format de timp acceptat este: yyyy-mm-dd): ")
current_date = datetime.now()
format_date = current_date.strftime("%Y-%m-%d")   
print(f"Data de astazi este {format_date}")
numarul_personae = int(input ("Numarul de persoane pentru care se face oferta este: "))

departure_iataCode = FlightSearch().getIataCodeBasedOnTheCity(depaerture, sheet_data)
arrival_iataCode = FlightSearch().getIataCodeBasedOnTheCity(destination, sheet_data)


flight_for_object1 = FlightData(departure_iataCode,arrival_iataCode,data_decolarii,numarul_personae)

flight_for_object1.find_cheapes_flight(flight_for_object1.request_for_flight_price())