# Lucilene DeWeese 

"""
Problem Statement:
Many companies wish to understand the needs and wants of their customers more deeply
so the company can create products that fill those needs and wants.
One way to understand customers more deeply is to record the values entered by customers
while they are using a program and then to analyze those values.
One common way to record values is for a program to store them in a file.
"""

# Import the mathematical constant pi for calculating tire volume
from math import pi

# Import the datetime class from the datetime
# it can be used in this program.
from datetime import datetime

# Prompt the user for the width of the tire
width = int(input("Enter the width of the tire in mm (ex 205): "))

# Prompt the user for the aspect ratio of the tire
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Prompt the user for the diameter of the wheel
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the approximate tire volume
volume = (pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Print the tire volume with two decimal places
print(f"\nThe approximate volume is {volume:.2f} liters")

# ----------------- Exceeds Requirements Feature -----------------
# Ask if the user wants to buy tires and optionally record their phone number
buy = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
phone = input("Enter your phone number: ") if buy == "yes" else ""

# Open the volumes.txt file in append mode
with open("volumes.txt", "at") as file:

    # Print the date, tire dimensions, volume, and optionally the phone number to the file
    print(
        f"{datetime.now():%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}" 
        + (f", {phone}" if phone else ""),
        file=file
    )
