import requests,time
from datetime import datetime

import smtplib

MY_LAT = 46.729721 # Your latitude
MY_LONG = -117.181831 # Your longitude


#---------------------------------------- Objectives --------------------------------------
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



# ------------------------------------- Solution -----------------------------------------




def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


#Your position is within +5 or -5 degrees of the ISS position.
hr_right_now = datetime.now().hour


def is_within_distance(position:tuple):
    lat,lng = position
    lat_diff,lng_diff = MY_LAT - lat, MY_LONG - lat
    return True if (-5 <= lat_diff <=5) and (-5<= lng_diff <=5) else False


def is_dark(daylight_savings = True,current_hr=hr_right_now):
    dark_hr = 19 if not daylight_savings else 16
    return True if current_hr > dark_hr else False    


def email_setup():
    connection = smtplib.SMTP("smtp.gmail.com");
    return connection


def send_email(user_email,recepient_email,password):
    connection = email_setup()
    connection.starttls()
    connection.login(user=user_email,password=password)
    connection.sendmail(
        from_addr= user_email,
        to_addrs= recepient_email,
        msg="Subject:ISS Near your proximity!(Python Project)\n\nLookup! ISS should be passing the house in a few mins."
    )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


my_email = "ehianesocials@gmail.com"; #!this email should have the app password activated.
password_ = "ouyzzwqnznprrghu"  #password gotten from your email provider, (for gmail-> setup app password).
recepient_email = "ehiane.business@gmail.com";


def main():
    if is_within_distance(get_iss_position()) and is_dark() :
        print("sending email...")
        send_email(user_email=my_email,recepient_email=recepient_email,password=password_)        
        print("SENT!, wait for a minute!")
    else:
        print(f"ISS is not near you!\nISS Current location is: ({get_iss_position()[0],get_iss_position()[1]})")


## BONUS
# if you want to run it for 24 hrs do this (and keep the program running):
# while True:
#     time.sleep(60) #run every 60 secs
#     main()
    

main()





