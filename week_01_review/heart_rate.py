"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# 1. Get input from the user
age = int(input("Please enter your age: "))

# 2. Calculate maximum heart rate
max_heart_rate = 220 - age

# 3. Calculate the slowest and fastest heart rate
slowest = max_heart_rate * 0.65
fastest = max_heart_rate * 0.85

# 4. Display the results (rounded to whole numbers)
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {round(slowest)} and {round(fastest)} beats per minute.")
