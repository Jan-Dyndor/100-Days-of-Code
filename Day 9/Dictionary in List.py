travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_name, number_of_visits, cities):
    temp_dictionary = {
        "country": country_name,
        "visits": number_of_visits,
        "cities": cities,
    }
    travel_log.append(temp_dictionary)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
add_new_country("Poland", 98, ["Warszawa", "Poznań"])
print(travel_log)
