logo = """

________                          
__  ___/_____________ ___________ 
_____ \___  __ \  __ `/  ___/  _ \
____/ /__  /_/ / /_/ // /__ /  __/
/____/ _  .___/\__,_/ \___/ \___/ 
       /_/                        
       
"""
print(logo)

import requests
from datetime import datetime
import smtplib
import time
from dateutil import parser  # New import for time parsing

MY_EMAIL = "mkamilleo2004@gmail.com"
MY_PASSWORD = "your_password_here"

# Your location
MY_LAT = 33.6844  # Replace with your latitude
MY_LNG = 73.0479  # Replace with your longitude


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def iss_overhead():
    iss_latitude, iss_longitude = get_iss_position()
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]

    # Parse sunrise and sunset times correctly
    sunrise = parser.parse(data["sunrise"])
    sunset = parser.parse(data["sunset"])

    # Current time in UTC
    time_now = datetime.utcnow()

    # Check if it's nighttime
    return time_now >= sunset or time_now <= sunrise


while True:
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
            )
    time.sleep(60)  # Check every 60 seconds
