# Day 37: Advanced DateTime Operations

from datetime import datetime, timedelta


now = datetime.now()

print("Current Date and Time:", now)
print("Date:", now.date())
print("Time:", now.time())


# Add days
future_date = now + timedelta(days=7)

print("Date After 7 Days:", future_date)


# Subtract days
past_date = now - timedelta(days=7)

print("Date 7 Days Ago:", past_date)


# Formatting date
formatted_date = now.strftime("%d-%m-%Y")

print("Formatted Date:", formatted_date)


# Parse string into datetime
date_string = "05-10-2026"

parsed_date = datetime.strptime(date_string, "%d-%m-%Y")

print("Parsed Date:", parsed_date)


# Difference between dates
date1 = datetime(2026, 10, 5)
date2 = datetime(2026, 12, 31)

difference = date2 - date1

print("Days Between Dates:", difference.days)
