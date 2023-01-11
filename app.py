import requests

api_key = '99999f5fe42029bc4bea2be46b101327'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")
#(this is the API call from OpenWeather)
print (weather_data.status_code)