#week 03

"""
Many vehicle owners record the fuel efficiency of their vehicles
as a way to track the health of the vehicle. If the fuel efficiency 
of a vehicle suddenly drops, there is probably something wrong with
the engine or drive train of the vehicle. In the United States, 
fuel efficiency for gasoline powered vehicles is calculated as miles per gallon. 
In most other countries, fuel efficiency is calculated as liters per 100 kilometers.
"""

def main():
    # Step 1: Get an odometer value in U.S. miles from the user.
    start_miles = float(input("Enter the first odometer reading (miles): "))

    # Step 2: Get another odometer value in U.S. miles from the user.
    end_miles = float(input("Enter the second odometer reading (miles): "))

    # Step 3: Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # Step 4: Call the miles_per_gallon function and store the result
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Step 5: Call the lp100k_from_mpg function and store the result
    lp100k = lp100k_from_mpg(mpg)

    # Step 6: Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    """
    miles_traveled = end_miles - start_miles
    return miles_traveled / amount_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100 kilometers."""
    return 235.215 / mpg


# Call the main function so that this program will start executing.
main()
