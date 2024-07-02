import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self.prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self._authorization = HTTPBasicAuth(self._user, self._password)

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint,auth=self._authorization)
        
        # Debugging prints
        print("Status Code:", response.status_code)
        print("Response JSON:")
        try:
            data = response.json()
            print(data)
        except ValueError:
            print("Response is not in JSON format")
            print(response.text)
            return []

        if response.status_code == 200:
            try:
                self.customer_data = data["users"]
            except KeyError:
                print("Key 'users' not found in response data")
                self.customer_data = []
        else:
            print(f"Failed to get customer emails. Status Code: {response.status_code}")
            self.customer_data = []

        return self.customer_data