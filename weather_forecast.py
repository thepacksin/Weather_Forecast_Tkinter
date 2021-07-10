from tkinter import *
import requests
import json

App=Tk()
App.title('Weather Forecast')
App.geometry("300x30")
App.configure(background="blue")

url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key='cf2c4cf5c98e45a47635fbe7266bc6f6'
name=str(input().rstrip())
city=name

try:
	api_request=requests.get(url.format(city,api_key))
	api = json.loads(api_request.content)
except:
	api="Error..."

api_city=api['name']
api_weather=api['weather'][0]['main']
api_temperature="{:.0f}".format(api['main']['temp']-273.15)
api_country=api['sys']['country']

temp=(api_country,
	api_city,
	api_weather,
	api_temperature)



label=Label(App,text=temp,font=("Helvetica",20),background="lightblue")
label.pack()

App.mainloop()