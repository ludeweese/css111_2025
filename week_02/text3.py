# discount.py - Activity Team 10

"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday,
which are the store’s slowest sales days. On Tuesday and Wednesday, 
if a customer’s subtotal is $50 or greater, the store will discount the customer’s
subtotal by 10%.
Stretch Challenge: If today is Tuesday or Wednesday and the subtotal is less than $50,
show how much more the customer needs to spend to qualify for the discount.
"""

from datetime import datetime

# Get current day of the week (0=Monday, 6=Sunday)
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# --- Testing Override ---
# Ask the user if they want to override the day (for testing purposes)
override = input("Enter a day number (0=Mon ... 6=Sun) for testing or press Enter to use today: ")
if override.strip() != "":
    try:
        day_of_week = int(override)
    except ValueError:
        print("Invalid input, using today's date.")

print(f"(Debug) Day of week: {day_of_week}")  # Show day number so you know what is being used

# --- Input subtotal ---
original_subtotal = float(input("Please enter subtotal: "))
subtotal = original_subtotal  # copy for calculations

# --- Initialize discount ---
discount = 0

# --- Apply discount if conditions are met ---
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):  # Tuesday or Wednesday
    discount = subtotal * 0.10
    subtotal -= discount

# --- Calculate sales tax and total ---
sales_tax = subtotal * 0.06
total = subtotal + sales_tax

# --- Print results ---
if discount > 0:
    print(f"Discount amount: {discount:.2f}")
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")

# --- Stretch Challenge Part 1 ---
# If today is Tuesday or Wednesday AND subtotal was less than 50, tell user how much more is needed
if (day_of_week == 1 or day_of_week == 2) and original_subtotal < 50:
    difference = 50 - original_subtotal
    print(f"Spend ${difference:.2f} more to qualify for the discount.")

