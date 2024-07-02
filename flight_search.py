import requests
from datetime import datetime
import os
import urllib3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token/"

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    


    def _get_new_token(self):
        TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body, verify=False)

        print("Request URL:", TOKEN_ENDPOINT)
        print("Request Headers:", response.request.headers)
        print("Request Body:", response.request.body)
        print("Response Status Code:", response.status_code)
        print("Response JSON:")
        try:
            response_json = response.json()
            print(response_json)
        except ValueError:
            print("Response is not in JSON format")
            print(response.text)
            return None

        if response.status_code != 200:
            print("Failed to get token. Response:")
            print(response_json)
            return None

        if 'access_token' not in response_json:
            print("No access token found in response.")
            return None

        token = response_json["access_token"]
        expires_in = response_json["expires_in"]

        print(f"Your token is {token}")
        print(f"Your token expires in {expires_in} seconds")
        return token
    
    

    def get_destination_code(self, city_name):

        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query,
            verify=False
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
    
    def get_destination_code(self, city):
        DESTINATION_ENDPOINT = f"https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword={city}&page[limit]=1"
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(DESTINATION_ENDPOINT, headers=headers, verify=False)
        print(f"Status code {response.status_code}. Airport IATA:")
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                return data["data"][0]["iataCode"]
            else:
                print(f"No airport code found for {city}.")
                return "Not Found"
        else:
            print(f"Failed to get destination code for {city}.")
            return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
    
        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        # nonStop must be "true" or "false" string. Python booleans won't work
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
            verify=False
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()'''



# Suppress only the single InsecureRequestWarning from urllib3 needed for development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body, verify=False)

        print("Request URL:", TOKEN_ENDPOINT)
        print("Request Headers:", response.request.headers)
        print("Request Body:", response.request.body)
        print("Response Status Code:", response.status_code)
        print("Response JSON:")
        try:
            response_json = response.json()
            print(response_json)
        except ValueError:
            print("Response is not in JSON format")
            print(response.text)
            return None

        if response.status_code != 200:
            print("Failed to get token. Response:")
            print(response_json)
            return None

        if 'access_token' not in response_json:
            print("No access token found in response.")
            return None

        token = response_json["access_token"]
        expires_in = response_json["expires_in"]

        print(f"Your token is {token}")
        print(f"Your token expires in {expires_in} seconds")
        return token

    def get_destination_code(self, city):
        DESTINATION_ENDPOINT = f"https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword={city}&page[limit]=1"
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(DESTINATION_ENDPOINT, headers=headers, verify=False)
        print(f"Status code {response.status_code}. Airport IATA:")
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                return data["data"][0]["iataCode"]
            else:
                print(f"No airport code found for {city}.")
                return "Not Found"
        else:
            print(f"Failed to get destination code for {city}.")
            return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
            verify=False
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()