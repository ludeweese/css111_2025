#discount.py activity team 10

"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday,
which are the store’s slowest sales days. On Tuesday and Wednesday, 
if a customer’s subtotal is $50 or greater, the store will discount the customer’s
subtotal by 10%.
"""

# Import the datetime class from the datetime
from datetime import datetime

# get the current datetime
current_date_and_time = datetime.now() 

# get the day of the week
day_of_week = current_date_and_time.weekday() 

# Temporary override for testing purposes
# Uncomment one line below to test a specific day:
# day_of_week = 0  # Monday
# day_of_week = 1  # Tuesday
# day_of_week = 2  # Wednesday
# day_of_week = 3  # Thursday
# day_of_week = 4  # Friday
# day_of_week = 5  # Saturday
# day_of_week = 6  # Sunday

# Print the day of the week for testing purpose
print(day_of_week) 

# Ask the user for the subtotal of their purchase
subtotal =float(input("Please enter subtotal:")) 

# Initialize discount
discount = 0

# Apply discount if today is Tuesday (1) or Wednesday (2) and subtotal is at least $50
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = subtotal * 0.10
    subtotal -= discount

# Calculate sales tax (6%) and total
sales_tax = subtotal * 0.06
total = subtotal + sales_tax

# Print results
if discount > 0:
    print(f"discount amount: {discount:.2f}")
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")


#Notify the user how much more they need to spend to get the discount

# Stretch Challenge Part 1:
# If today is Tuesday or Wednesday and subtotal is less than 50,
# show the user how much more they need to spend to get the discount.
if (day_of_week == 1 or day_of_week == 2) and subtotal < 50:
    difference = 50 - subtotal
    print(f"Spend ${difference:.2f} more to qualify for the discount.")