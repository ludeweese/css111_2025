"""
02 Team Activity: Calling Functions - Discount
Brad C (5 Spice)
Your program gets the day of the week from your computer’s operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""
print()

#Library
import math
from datetime import datetime

#Date Method
current_time = datetime.now()

#Input & Variables
sub_total = float(input("Please enter the subtotal\t:"))
sales_tax = None
discount = None
total = None

#Time: Tues/Wed? 
weekday = current_time.weekday()

if  (weekday == 1 or weekday == 2) and (sub_total >= 50):
    discount = sub_total * .10
    sub_total = sub_total - discount

    #Calculate Tues/Wed
    sales_tax = sub_total * 0.06
    total = sub_total + sales_tax

    #Display Results: Tues/Wed
    print(f"Your discount amount is: ${discount:.2f}")
    print(f"Sales tax ammount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}", "\n")

else:
    #Calculte =! Tues/Wed
    sales_tax = sub_total * 0.06
    total = sub_total + sales_tax

    #Display Results =! Tues/Wed
    print(f"Sales tax ammount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}", "\n")