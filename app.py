import requests

api_key = '99999f5fe42029bc4bea2be46b101327'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")
if weather_data.json() ['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print (f"The weather in {user_input} is looking like: {weather}")
    print (f"The temperature in {user_input} is looking like: {temp}°F")