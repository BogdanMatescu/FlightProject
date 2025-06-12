import flight_search
import requests
import json

class FlightData(flight_search.FlightSearch):
    
    def __init__(self, originalLocation, destinationLocation, departureDate, adults):
        super().__init__()
        self.originalLocation = originalLocation 
        self.destinationLocation = destinationLocation 
        self.departureDate = departureDate
        self.adults = adults
        
        
    def request_for_flight_price(self):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = { 
            "originLocationCode":self.originalLocation,
            "destinationLocationCode":self.destinationLocation, 
            "departureDate":self.departureDate,
            "adults":self.adults
        }
        token = { 
                 "Authorization": f"Bearer {self.token}"
                 }
        
        response = requests.get(url, params=params, headers=token)
        response.raise_for_status()
        with open("raspuns_amadeus.json", "w") as f:
            json.dump(response.json(),f,indent=2)        
        final_report = response.json()
        return final_report
    
    def find_cheapes_flight (self, json_file):
        for i in range (len(json_file["data"])):
            print(json_file["data"][i]["price"]["total"])

        