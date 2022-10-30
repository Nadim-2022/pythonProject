"""""
1. Write a program that fetches and prints out a random Chuck Norris joke for the user.
Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
"""
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

"""""
2. Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program
that asks the user for the name of a municipality and then prints out the corresponding weather condition description text 
and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive
the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.
"""
import requests
import json
keyword = input("Enter keyword: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={keyword}&appid=b7157b235660aa160ba7b57fbfd3c4e2"
response = requests.get(request).json()

#print(json.dumps(response, indent=2))

weather = response["weather"][0]["description"]
temp = response["main"]["temp"]

print(f"City : {(response['name'])}\nCurrent wheather condition : {weather}\ncurrent temperature : {int(temp/10)}°C")