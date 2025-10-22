#team 10

""" You work for a retail store that wants to increase sales on Tuesday and Wednesday,
 which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s 
 subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%. 
"""
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

#For Testing Purpose 
#Day of the week =0 #Monday
#Day od the week =1 #Tuesday
#Day od the week =2 #Wed
#Day od the week =3 #Thur
#Day od the week =4 #Fri
#Day od the week =5 #SAt
#Day of the week =6 #Sunday

# Print the day of the week for the user to see.
print(day_of_week)

#Gets the subtotal
subtotal =float(input("Please enter subtotal:"))

#Initiate discount
discount= 0

#Apply discount on Tueday(1) and Wednesday (2)
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount= subtotal * 0.10
    subtotal-= discount


#calculate  sales tax of 6% to and total
sales_taxes = subtotal * 0.06
total = subtotal + sales_taxes

#Print result
if discount > 0:
    print(f"discount amount: {discount:.2f}")

print(f"Sales tax amount: {sales_taxes:.2f}")
print(f"Total: {total:.2f}")

#Notify the user how much more they need to spend to get the discount

# Stretch Challenge Part 1:
# If today is Tuesday or Wednesday and subtotal is less than 50,
# show the user how much more they need to spend to get the discount.
if (day_of_week == 1 or day_of_week == 2) and subtotal < 50:
    difference = 50 - subtotal
    print(f"Spend ${difference:.2f} more to qualify for the discount.")




