# Day 24 - Date, Time and Random Module

import datetime
import random

# Current date and time

now = datetime.datetime.now()

print("Current date and time:", now)

# Current date

today = datetime.date.today()

print("Today's date:", today)

# Extract date components

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Formatting date

formatted_date = now.strftime("%d-%m-%Y")

print("Formatted date:", formatted_date)


# Random number

random_number = random.randint(1, 100)

print("Random number:", random_number)


# Random choice

languages = ["Python", "Java", "C++", "JavaScript"]

selected_language = random.choice(languages)

print("Randomly selected language:", selected_language)


# Generate multiple random numbers

print("Five random numbers:")

for i in range(5):
    print(random.randint(1, 50))
