# example_5.py

import csv

def main():
    # Column index of phone number (used as dictionary key)
    PHONE_INDEX = 2

    # Read the CSV into a dictionary using phone numbers as keys
    dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

    # Print the dictionary
    for phone, info in dentists_dict.items():
        print(f"{phone}: {info}")


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a dictionary using a unique column as key."""
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        # Read each row
        for row_list in reader:
            if len(row_list) != 0:  # skip empty rows
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()
