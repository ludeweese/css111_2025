#Team activity
import csv
from datetime import datetime

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.
    """
    compound_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header
        for row in reader:
            compound_list.append(row)
    return compound_list


def print_list(a_list):
    """Print each element of a list on a separate line."""
    for item in a_list:
        print(item)


def main():
    # Read the CSV into a list
    students_list = read_compound_list("pupils.csv")

    # Lambda function to extract birthdate and convert to datetime object
    birthdate_key = lambda student: datetime.strptime(student[BIRTHDATE_INDEX], "%Y-%m-%d")

    # Sort the students by birthdate from oldest to youngest
    students_list_sorted = sorted(students_list, key=birthdate_key)

    # Print the sorted list
    print("Ordered from Oldest to Youngest")
    print_list(students_list_sorted)

    # Stretch: sort by given name
    students_by_name = sorted(students_list, key=lambda student: student[GIVEN_NAME_INDEX])
    print("\nOrdered by Given Name")
    print_list(students_by_name)

    # Stretch: sort by birth month and day (ignore year)
    students_by_month_day = sorted(
        students_list,
        key=lambda student: datetime.strptime(student[BIRTHDATE_INDEX], "%Y-%m-%d").replace(year=1900)
    )
    print("\nOrdered by Birth Month and Day")
    print_list(students_by_month_day)


# Call main to run the program
main()
