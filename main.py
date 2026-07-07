#################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
MONTH = dt.datetime.now().month
DAY = dt.datetime.now().day

# 1. Update the birthdays.csv
with open("birthdays.csv") as birthday_file:
    birthday_data = pandas.read_csv(birthday_file)

# 2. Check if today matches a birthday in the birthdays.csv
birthday_list = [{
    'name': values['name'],
    'email': values['email']
} for index, values in birthday_data.iterrows()
    if values['month'] == MONTH and values['day'] == DAY
]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
for person in birthday_list:
    random_letter = "letter_" + str(random.randint(1, 3)) + ".txt"
    with open(f"./letter_templates/{random_letter}", mode="r") as letter_file:
         birthday_letter = letter_file.read().replace("[NAME]", person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person['email'],
            msg=f"Subject: Happy Birthday!!\n\n{birthday_letter}"
        )
