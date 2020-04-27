import pyowm
import tkinter
import os
import time
import xlsxwriter
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from weatherfunctions import *
from emailservice import *
from database import *




# ---------------------------------------------------------------------------- #
# The prerequisite loop to getting the forecast data
# ---------------------------------------------------------------------------- #
def weather_choice(api_key):
    Terminator = False
    city = input("Please enter the city you would like to get the weather for: ")
    ccode = input("Please enter the country code: ")
    while not Terminator:
        print("Viewing the current and future forecasts for {}".format(city +","+ccode))
        print("")
        forecast_loop(api_key,city,ccode)
        Terminator = True
# ----------------------------------------------------------------------------- #
# The main loop for getting the weather forecast
# ----------------------------------------------------------------------------- #
def forecast_loop(api_key,city,ccode):
    hours_passed = 3
    days = 1
    forecastobj = api_key.three_hours_forecast(city + ", " + ccode)
    forecast = forecastobj.get_forecast()
    for weather in forecast:
        utctime = weather.get_reference_time()
        date = datetime.utcfromtimestamp(utctime).strftime('%d %B %Y')
        time = datetime.utcfromtimestamp(utctime).strftime('%H:%M:%S')

        print("Day {} in the 5 day forecast".format(days))
        print ("Date: {}".format(date))
        print("# --------------------------------------------------------------- #\n")
        print("The following forecast for {}, goes as follows: \n".format(time))
        temperature(weather)
        humidity(weather)
        cloudcov(weather)
        windspeed(weather)
        sky_status(weather)
        print("\n# --------------------------------------------------------------- #\n")
        choice = input("\nWould you like to view the weather forcast for the next 3 hours? (Y/N): ")
        if choice == "Y":
            os.system("cls")
            hours_passed += 3
            if hours_passed >= 24:
                hours_passed = 3
                days += 1
            continue
        elif choice == "N":
            os.system("cls")
            break
        else:
            raise ValueError("Invalid input")

# --------------------------------------------------------------------------- #
# The main loop for gettting sending email alerts
# --------------------------------------------------------------------------- #

def email_choice(api_key,server,email_address,password,sheet_name):
    email_terminator = False
    city_text = "Enter the name of the city in which you would like to notify the workers of the weather change: "
    city = input(city_text)
    ccode = input("Enter the country code for the city: ")
    forecastobj = api_key.three_hours_forecast(city + ", " + ccode)
    forecast = forecastobj.get_forecast()
    os.system("cls")
    while not email_terminator:
        print("# -----------------Email Alert System------------------------ #")
        print("1) Send an schedule change alert to notify workers that it will rain")
        print("2) Send an alert to workers that there will be no schedule change")
        print("3) Send an alert to IT workers that it will rain")
        print("X) Exit the email application")
        print("")
        choice = input("Please select an option: ")
        if choice == '1':
            rain_schedule_change(server,forecast,DB_sheet,email_address,password,city)
            print("Alert Sent")
            email_terminator = True
        elif choice == '2':
            sunny_alert(server,forecast,DB_sheet,email_address,password,city)
            print("Alert Sent")
            email_terminator = True
        elif choice == '3':
            weather_alert_IT(server,forecast,DB_sheet,email_address,password)
            print("Alert sent")
            email_terminator = True




#------------------------------------------------------------------------------#
# The main driver function
#------------------------------------------------------------------------------#


def main():
    #The api_key for getting weather data
    key = input("Enter your Open Weather API key")
    api_key = pyowm.OWM(key)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    os.system("cls")
    print("# -----------Krace Gennedy Weather Forecast and Email Service login-------- #\n")
    email_address = input("Enter your email address: ")
    while True:
        if is_empty(email_address):
            email_address = input("Please enter a valid email address: ")
            continue
        else:
            break
   
    password = input("Enter your email address password: ")
    #DB_sheet = None
    os.system("cls")
    server.ehlo()
    exitWindow = False
    # Creating a database if it hasn't been created already
    if not os.path.isfile('WorkerDB.xlsm'):
        print("A database currently does not exist")
        print("Creating the database")
        make_database()
        make_xlsm_wb()
    file = openpyxl.load_workbook('WorkerDB.xlsm',read_only=False,keep_vba=True)
    global DB_sheet
    DB_sheet = file['Sheet1']
    while not exitWindow:
        print("# --------------------------------------------------------------- #")
        print(" ")
        print("Welcome to the Krace Gennedy Weather forecast and Email service")
        print("1) Weather foreast")
        print("2) Send an email alert")
        print("3) Populate the database")
        print("X) Exit the application")
        print(" ")
        print("# --------------------------------------------------------------- #")
        choice = input("Please select an option: ")
        if choice == "1":
            os.system("cls")
            weather_choice(api_key)
        elif choice == "2":
            os.system("cls")
            email_choice(api_key,server,email_address,password,DB_sheet)
        elif choice == "3":
            os.system("cls")
            make_entry(DB_sheet)
            file.save('WorkerDB.xlsm')
        if choice == "X":
            exitWindow = True
#------------------------------------------------------------------------------#






main()
