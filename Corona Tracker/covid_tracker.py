from cProfile import label
import tkinter as tk
import requests
import datetime


def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_class = str(json_data["cases"])
    total_death = str(json_data["deaths"])
    today_cases = str(json_data["todayCases"])
    today_death = str(json_data["todayDeaths"])
    today_recovered = str(json_data["todayRecovered"])
    updated_at = json_data["updated"]
    date = datetime.datetime.fromtimestamp(updated_at / 1e3)
    label1.config(
        text="Total Cases: "
        + total_class
        + "\n"
        + "Total Deaths: "
        + total_death
        + "\n"
        + "Today deaths: "
        + today_death
        + "\n"
        + "Today Recorded: "
        + today_recovered
    )
    label2.config(text=date)


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("CovidTracker App")

f = ("poppins", 15, "bold")

button = tk.Button(canvas, font=f, text="Load", command=getCovidData)
button.pack()

label1 = tk.Label(canvas, font=f)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

getCovidData()
canvas.mainloop()
