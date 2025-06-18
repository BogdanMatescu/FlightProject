import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    API_EditRow = "https://api.sheety.co/2c53948f0e1180c3d9457b9047f4a08e/flightDealsBogdan/prices/[Object ID]"


    def updateLine(id, iataCode:str):
        body = {
            "price": {
                "iataCode": iataCode,
            }
        }
        response = requests.put(url=f"https://api.sheety.co/2c53948f0e1180c3d9457b9047f4a08e/flightDealsBogdan/prices/{id}",json=body )
        response.raise_for_status() 

    def deleteLine(id):
        body = {
            "price": {
                "iataCode": "",
            }
        } 
        response = requests.put(url=f"https://api.sheety.co/2c53948f0e1180c3d9457b9047f4a08e/flightDealsBogdan/prices/{id}",json=body ) 
        response.raise_for_status()