import pyowm
import tkinter
import os
import time
import xlsxwriter
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from emailservice import *
from database import *

#------------------------------------------------------------------------------#
# Function for storing the weather for day 2 in the forecast
# -----------------------------------------------------------------------------#
def tomorrow_weather(forecast):
    hours_passed = 3
    status_lst = []
    for weather in forecast:
        if hours_passed < 48:
            status_lst.append(weather.get_status())
            hours_passed += 3
    return status_lst
#------------------------------------------------------------------------------#
# Function for checking if the weather for day 2 in the forecast is clear
# -----------------------------------------------------------------------------#
def is_clear(forecast):
    not_clear_weathers = ['Rain','Snow','Thunderstorm','Drizzle']
    return not_clear_weathers in tomorrow_weather(forecast)
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Weather forecast functions
# -----------------------------------------------------------------------------#
def temperature(weatherobj):
    temperature = weatherobj.get_temperature('celsius')['temp']
    print("The temperature is expected to be {}°C".format(temperature))

def humidity(weatherobj):
    humid = weatherobj.get_humidity()
    print("It is expected that there will be {}% humidty in the area".format(humid))

def cloudcov(weatherobj):
    cloud = weatherobj.get_clouds()
    print("It is expected for there to be {}% cloud coverage".format(cloud))

def windspeed(weatherobj):
    wind = weatherobj.get_wind()['speed']
    print("It is expected for the wind to reach speeds up to {} m/s".format(wind))

def sky_status(weatherobj):
    cloud_stat = weatherobj.get_detailed_status()
    if cloud_stat == "clear sky" or cloud_stat == "few clouds":
        print("It is also expected for there to be a {}".format(cloud_stat))
    elif cloud_stat == "scattered clouds" or "broken clouds":
        print("It is expected for there to be {}".format(cloud_stat))
    elif cloud_stat == "shower rain" or "rain" or "light rain":
        print("Remember to bring an umbrella as it is expected that there will be \
        some {}".format(cloud_stat))
    else:
        print("The detailed weather report for the sky: ")
# ----------------------------------------------------------------------------------
