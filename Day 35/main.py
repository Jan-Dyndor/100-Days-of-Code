import requests
from twilio.rest import Client

account_sid = "0"
auth_token = "0"

api_key = "0"
LAT = 0
LONG = 0
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

params = {
     "lat": LAT,
     "lon": LONG,
     "appid": api_key,
     "cnt": 4,
 }

response = requests.get(END_POINT, params=params)
response.raise_for_status()
data = response.json()

code = data["cod"]

for i in range(len(data["list"])):
    # print("weather_id: ", data["list"][i]["weather"][0]["id"])
    # print("weather description:", data["list"][i]["weather"][0]["description"])
    condition_code = data["list"][i]["weather"][0]["id"]
    if condition_code < 700:
        cient = Client(account_sid, auth_token)
        message = cient.messages \
        .create(
            body="It's going to rain today. Bring umbrella!",
            from_ = "+0",
            to = "+0"
        )
    print(message.status)
    break