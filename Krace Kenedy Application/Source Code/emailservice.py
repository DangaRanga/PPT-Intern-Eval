import xlsxwriter

import smtplib
from email.mime.text import MIMEText
from database import *
from weatherfunctions import *
from validatorfunctions import *

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
# ----------------------------------------------------------------------------- #

#------------------------------------------------------------------------------#
# Function to send an alert when the skys are clear
# -----------------------------------------------------------------------------#

def sunny_alert(server,forecast,sheet_name,senderemail,password,location):
    mailing_list = mailing_list_loc(sheet_name,location)
    if is_clear(forecast):
        subject = "Sunny Day - No Schedule Change"
        message = "It is expected for there to be clear skys tomorrow, you are scheduled for 8 hours tomorrow"
        msg = "Subject: {}\n\n{}".format(subject,message)
        server.login(senderemail,password)
        server.sendmail(senderemail,mailing_list,msg)
    else:
        print("It is currently not sunny, please select a different alert")
# -----------------------------------------------------------------------------#
# Function to send an email alert when it is expected for there to be rain
# -----------------------------------------------------------------------------#
def rain_schedule_change(server,forecast,sheet_name,senderemail,password,location):
    mailing_list = mailing_list_loc(sheet_name,location)
    if not is_clear(forecast):
        subject = "Rainy Day - Schedule Change"
        message = "It's expected for there to be some rain tomorrow, your new schedule will be 4 hours"
        msg = 'Subject: {}\n\n {}'.format(subject,message)
        server.login(senderemail,password)
        server.sendmail(senderemail,mailing_list,msg)


#------------------------------------------------------------------------------#
# Function to alert the IT workers if ther will be rain
# -----------------------------------------------------------------------------#
def weather_alert_IT(server,forecast,sheet_name,senderemail,password):
    email_dict = role_email_dict(sheet_name) #This makes a dictionary with the IT roles
    mailing_list = []
    for email in email_dict.values():
        mailing_list.append(email)
    if "shower rain" or "rain" or "light rain"  or "thunderstorm " in forecast:
        server.login(senderemail,password)
        subject = "Rainy Day Alert"
        message = "It's expected for there to be some rain, its best not to hit the streets this week"
        msg = 'Subject: {}\n\n {}'.format(subject,message)
        server.sendmail(senderemail,mailing_list,msg)


def send_individual_email(server,your_email,password,reciever_email):
    subject = input("Enter the subject of the email you would like to send ")
    message = input("Please type the body of the email")
    msg = 'Subject: {}\n\n {}'.format(subject,message)
    server.sendmail(your_email,reciever_email,msg)

def send_mass_email(server,your_email,password,mailing_list):
    subject = input("Enter the subject of the email you would like to send ")
    message = input("Please type the body of the email")
    msg = 'Subject: {}\n\n {}'.format(subject,message)
    server.sendmail(your_email,mailing_list,msg)

# ---------------------------------------------------------------------------- #
