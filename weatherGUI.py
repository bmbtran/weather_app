from tkinter import *
import requests
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("480x480")
root.configure(bg='lightblue')
root.resizable(0,0)
root.title("Weather App")
 
 
# Format the time zone
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    api_key = "68583ac468a15c2214b022fbde82e997"  #API Key
 
    # Get the city name
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # Decode json file
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 
    # check to ensure status code is succesfull
    if weather_info['cod'] == 200:
        kelvin = 273 
 
    #Storing the fetched values of weather of a city
 
        temp = int(weather_info['main']['temp'] - kelvin)   #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
    # Format the weather data output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nWind Speed: {wind_speed}\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   # Insert the weather data into GUI
 
 
 
# UI
 
 
city_head= Label(root, text = 'Enter City Name', bg='lightyellow', font = 'Helvetica 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Helvetica 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Helvetica 10", bg='lightgreen', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", bg='lightyellow', font = 'Helvetica 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()
