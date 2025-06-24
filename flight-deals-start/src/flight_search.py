import requests

TOKEN_URL = ****
CLIENT_ID = ******
CLIENT_SECRET = *****

class FilghtError(Exception):
    pass


class FlightSearch:
        
    def __init__(self):
        self.api_key = CLIENT_ID
        self.api_secret = CLIENT_SECRET
        self.token = self.getNewToken()
    
    #This class is responsible for talking to the Flight Search API.
    def findIataCodeByCity (self, city):
        url_city = "https://test.api.amadeus.com/v1/reference-data/locations" 
        params = { 
            "keyword" : city,
            "subType": "CITY"
        }
        headers = {
             "Authorization": f"Bearer {self.token}"
        }
        request_iatcode = requests.get(url_city,params=params,headers=headers,verify=False)
        iataCode_formated = request_iatcode.json()["data"][0]["iataCode"]
        return iataCode_formated

    def getNewToken(self) : 
        
        data_payload = { 
                        "grant_type": "client_credentials", 
                        "client_id": CLIENT_ID, 
                        "client_secret": CLIENT_SECRET
        } 
        headers = {
    "Content-Type": "application/x-www-form-urlencoded"
        } 
        response = requests.post(TOKEN_URL, data = data_payload, headers= headers, verify=False) 
        response.raise_for_status()
        return response.json()['access_token'] 
    
    def getIataCodeBasedOnTheCity(self,city, dict_code):
        for loc in dict_code:
            if loc["city"] == city:
                return loc["iataCode"]
        else:
            print(f"Orasul {city} nu se afla in lista noastra de aeroporturi") 
            raise FilghtError("Te rog sa alegi un alt oras")
        