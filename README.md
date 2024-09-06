ISS Tracker
# About
This program tracks the International Space Station (ISS) and sends an email notification when it is overhead and it's nighttime at your location.

# How it Works
The program uses the following APIs:

- Open Notify API to get the current position of the ISS
- Sunrise-Sunset API to get the sunrise and sunset times for your location
- It checks every 60 seconds if the ISS is overhead (within a 5-degree radius of your location) and if it's nighttime. If both conditions are true, it sends an email notification to the specified email address.

# Configuration
To use this program, you need to:

- Replace MY_LAT and MY_LNG with your latitude and longitude
- Replace MY_EMAIL and MY_PASSWORD with your email address and password
- Running the Program
- Simply run the program using Python (e.g. python iss_tracker.py). The program will run indefinitely, checking for ISS overhead and nighttime every 60 seconds.
# Note
Make sure to allow less secure apps in your Google account settings if you're using Gmail.
Be aware that this program uses your email password in plain text, so use a secure password and consider using a throwaway email account.
