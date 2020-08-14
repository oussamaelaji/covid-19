import tkinter as tk
from tkinter import ttk, messagebox
import requests
import socket
import os


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return 1
    except OSError:
        return 0


def show_entry_fields():
    try:
        if(is_connected()):
            country = e1.get()
            request = requests.get(
                f"https://disease.sh/v3/covid-19/countries/{country.lower()}")
            country = request.json()['country']

            def operation(items):
                return "+" if request.json()[items] != 0 else ""
            print(
                f"https://disease.sh/v3/covid-19/countries/{country.capitalize()}")
            window = tk.Tk()
            window.title(f"Covid-19 {country}")
            window.geometry('300x160')
            lbl = ttk.Label(
                window, text=f"New cases today : {operation('todayCases')}{request.json()['todayCases']:,d}")
            lbl.pack()
            lbl2 = ttk.Label(
                window, text=f"New recovered today : {operation('todayRecovered')}{request.json()['todayRecovered']:,d}")
            lbl2.pack()
            lbl3 = ttk.Label(
                window, text=f"New death today : {operation('todayDeaths')}{request.json()['todayDeaths']:,d}")
            lbl3.pack()
            lbl4 = ttk.Label(
                window, text=f"Total Cases : {request.json()['cases']:,d}")
            lbl4.pack()
            lbl5 = ttk.Label(
                window, text=f"Total Recovered : {request.json()['recovered']:,d}")
            lbl5.pack()
            lbl6 = ttk.Label(
                window, text=f"Total Death : {request.json()['deaths']:,d}")
            lbl6.pack()
            lbl7 = ttk.Label(
                window, text=f"Active Cases : {request.json()['active']:,d}")
            lbl7.pack()
            lbl8 = ttk.Label(
                window, text=f"Critical cases : {request.json()['critical']:,d}")
            lbl8.pack()
            master.destroy()
        else:
            messagebox.showerror(
                "Error", "An error occurred in the internet connection")
    except:
        messagebox.showerror(
            "Error", "An error occurred getting the information. Check Your Country")


master = tk.Tk()
master.title("Covid-19")
master.geometry('230x85')
tk.Label(master, text="Country", font='Helvetica 10 bold').pack()
e1 = tk.Entry(master)
e1.pack()
tk.Button(master, text='Show', command=show_entry_fields).pack()
l1 = tk.Label(master, text="Coded By EL-AJI Oussama")
l1.pack()
tk.mainloop()
