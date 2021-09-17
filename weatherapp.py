from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Weather App')
root.geometry('600x100')

# create zip function
def zipLookup():
#     zip.get()
#     zipLabel = Label(root,text=zip.get())
#     zipLabel().grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=3C0238C1-ECBA-479B-8B1B-9248A4B28CCE")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        #conditionals for color
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        my_label= Label(root, text= city + " Air Quality "+ str(quality) + " "+ category, font=("Helvetica", 20),background = weather_color)
        my_label.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = "Error..."

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=30252&distance=25&API_KEY=3C0238C1-ECBA-479B-8B1B-9248A4B28CCE


zip = Entry(root)
zip.grid(row=0,column=0, stick=W+E+N+S)
submit = Button(root,text="Lookup Zipcode",command=zipLookup)
submit.grid(row=0,column=1, stick=W+E+N+S)



root.mainloop()