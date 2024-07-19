import requests
from datetime import datetime


MY_LAT = 52.732201
MY_LNG = 15.237570
#response = requests.get(url="http://api.open-notify.org/iss-now.json") #500 Internal Server Error something is wrong with the server

# I am  going to hard code the values to complete the challenge
latitude = 51
longitude = 15

# response.raise_for_status()
# latitude = float(response.json()["iss_position"]["latitude"])
# longitude = float(response.json()["iss_position"]["longitude"])

iss_position = (latitude, longitude)
print(iss_position)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0 # change display od datetime
}



def is_above(iss_lat = latitude, iss_lng = longitude, my_lat = MY_LAT, my_lng = MY_LNG):
    """" Function check if ISS is +/- 5 near us so we can see it"""
    if my_lat - 5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5:
        return True
    else:
        return False


def is_night():
    """ Function check is it is a night"""
    response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()
    data = response2.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    print(sunrise, sunset)
    sunrise_24h = int(sunrise.split("T")[1].split(":")[0])  # Hour of sunrise in 24h clock
    sunset_24h = int(sunset.split("T")[1].split(":")[0])
    now = datetime.now()
    print(sunset_24h, sunrise_24h)
    print()
    if now.hour >= sunset_24h or now.hour < sunrise_24h:
        return True
    else:
        return False

def can_we_see_iss():
    if is_night() and is_above():
        print("Go! We can see it!")
    else:
        print("Not this time")


can_we_see_iss()

# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )
#
