# Import the Math Module
import math

# Get user input
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Step-by-step calculation
inner = w * a + 2540 * d
volume = math.pi * w**2 * a * inner / 10000000000

# Display result
print(f"\nThe approximate volume is {volume:.2f} liters")
