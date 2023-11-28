import requests

api_key = '210cbef66f175b64953b53ba0c41642c'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature in K: {temp} K')
    print(f'Temperature in C: {temp-273.15} C')
    print(f'Temperature in F: {(temp-273.15)*9/5 +32} F')
    print(f'Weather description: {desc}')
else:
    print('Error fetching weather data')