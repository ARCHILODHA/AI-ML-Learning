# Day 36: Regular Expressions

import re


text = "My email is archi@example.com and my phone number is 9876543210."

# Find email
email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

email = re.search(email_pattern, text)

if email:
    print("Email:", email.group())


# Find phone number
phone_pattern = r'\b\d{10}\b'

phone = re.search(phone_pattern, text)

if phone:
    print("Phone:", phone.group())


# Find all numbers
numbers = re.findall(r'\d+', text)

print("Numbers:", numbers)


# Replace text
updated_text = re.sub("example.com", "gmail.com", text)

print("Updated Text:", updated_text)
