import tkinter as tk
from weatherdata import get_weather
from datetime import datetime
import requests




api_key = "" #Get a free api key from https://openweathermap.org/current
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=Sydney"
response = requests.get(complete_url)
weatherdata = response.json()


desc, location, celcius, temp_max, temp_min, feels_like = get_weather(weatherdata)

def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 22
        else "evening"
        if 18 <= h <= 22
        else "evening"
    )

segment = get_part_of_day(datetime.now().hour)


root = tk.Tk()


root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())
root.configure(bg="")



l = tk.Label(text='', font=("Helvetica", 40))

z = tk.Label(text=f'\n\n\n{location}', font=("Helvetica", 60))

a = tk.Label(text=f'Feels like {int(feels_like)}°', font=("Helvetica", 20))

l.config(text=f'\n\n{int(celcius)}°', fg='black', background="light blue")



t = tk.Label(text=f'Good {segment}, \nIt is {desc}.\n Todays temperatures will reach a max of {int(temp_max)}° and a low of {int(temp_min)}°.', font=("Helvetica", 20), background='light blue')

def rainy_cloudy():
    root.configure(bg="#191b43")
    l.config(background="#191b43", fg="gold")
    t.config(background="#191b43", fg="gold")
    a.config(background="#191b43", fg="light yellow")
    z.config(fg="white", background="#191b43")

def cloudy():
    root.configure(bg="light grey")
    l.config(background="light grey")
    t.config(background="light grey")
    a.config(fg="light yellow", background="light grey")
    z.config(fg="white", background="light grey")

def clear():
    root.configure(bg="light blue")
    l.config(background="light blue")
    t.config(background="light blue")
    a.config(fg="light yellow", background="light blue")
    z.config(fg="white", background="light blue")
    

if "cloudy" in desc:
    cloudy()
elif "rainy" or "rain" in desc:
    rainy_cloudy()
else:
    clear()

z.pack()
l.pack()
a.pack()
t.pack(expand=True)







root.mainloop()
