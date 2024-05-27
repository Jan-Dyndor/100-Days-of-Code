import smtplib

my_email = "MMail adress"
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# connection.starttls()
# connection.login(user=my_email, password="")
# connection.sendmail(from_addr=my_email, to_addrs="t97138453@gmail.com", msg="hello")
# connection.close()

# !Better Version
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="")
#     connection.sendmail(from_addr=my_email, to_addrs="t97138453@gmail.com",
#                         msg="Wellcome dear Friend")
#     connection.close()
#
import datetime as dt
# now = dt.datetime.now()
# year = now.year
# if year == 2024:
#     print(year)
#
# #  Creation a datetime object of our own date
# date_of_birth = dt.datetime(year=2024, month=12, day=15)
# print(date_of_birth.strptime())

# Practical exercise ======================
# import datetime as dt
# import random
#
# with open("./quotes.txt" , "r") as quotes:
#     quotes = quotes.readlines()
# print(quotes)
#
# random_quote = random.randint(0,len(quotes))
# now = dt.datetime.now()
# if now.weekday() == 6:
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password="APP Password in google")
#         connection.sendmail(from_addr=my_email, to_addrs="t97138453@gmail.com",
#                             msg=quotes[random_quote])
#         connection.close()
# else:
#     print("Not today")
#
