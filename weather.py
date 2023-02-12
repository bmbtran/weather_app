import requests

API_KEY = "68583ac468a15c2214b022fbde82e997"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)
print(response)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273, 2)
    print(data)
    print(weather)
    print(temperature)
else:
    print('An error has occured')
