# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
# Debugger checklist activity fixed

def main():
    print("This program computes the fuel efficiency")
    print("of your vehicle in miles per gallon.")

    prev_odom = float(input("Enter the previous odometer reading in miles: "))
    curr_odom = float(input("Enter the current odometer reading in miles: "))
    fuel_amount = float(input("Enter the amount of fuel in U.S. gallons: "))

    # Corrected order of arguments
    efficiency = miles_per_gallon(prev_odom, curr_odom, fuel_amount)

    print(f"{efficiency} miles per gallon")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    distance = end_miles - start_miles
    mpg = distance / amount_gallons
    return mpg


if __name__ == "__main__":
    main()
