# Import the csv module so that it can be used
# to read from the accidents.csv file.
#team activity week 10

import csv

# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9

def main():
    try:
        # Prompt the user for a filename and open that text file.
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:

            # Prompt the user for a percentage and handle ValueError
            try:
                perc_reduc = float(input(
                    "Percent reduction of texting while driving [0, 100]: "))
            except ValueError as val_err:
                print(f"Error: could not convert input to float: {val_err}")
                return  # stop program if invalid percentage

            # Check if the percentage is within a valid range
            if perc_reduc < 0:
                print(f"Error: {perc_reduc} is too low. Please enter a different number.")
                return
            elif perc_reduc > 100:
                print(f"Error: {perc_reduc} is too high. Please enter a different number.")
                return

            # Print header information
            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                  "phone while driving, approximately the",
                  "following number of injuries and deaths",
                  "would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            # Use the csv module to create a reader object
            # and handle CSV formatting errors
            try:
                reader = csv.reader(text_file, strict=True)
                next(reader)  # skip headers
            except csv.Error as csv_err:
                print(f"CSV Error in file {filename}: {csv_err}")
                return

            # Process each row in the CSV file
            for i, row in enumerate(reader, start=2):  # start=2 because headers are row 1
                try:
                    # Call the estimate_reduction function
                    injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)
                    # Print the estimated reductions
                    print(row[YEAR_COLUMN], injur, fatal, sep=", ")

                # Stretch Challenge: handle ZeroDivisionError
                except ZeroDivisionError:
                    print(f"Error: Fatal Crashes is zero in row {i} (year {row[YEAR_COLUMN]}) "
                          f"in file {filename}. Cannot divide by zero.")

    # Core Requirement: handle file not found
    except FileNotFoundError as fnf_err:
        print(f"[Errno 2] No such file or directory: '{filename}'")
        print("Please choose a different file.")

def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes  # can raise ZeroDivisionError

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
