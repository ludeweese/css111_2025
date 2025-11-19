def main():
    try:
        # Open the file phone_numbers.txt for reading and read all
        # of the phone numbers into a list named phone_numbers.
        phone_numbers = read_list("phone_numbers.txt")

        # Some of the phone numbers in phone_numbers.txt do not start
        # with an area code. Replace each short phone number with a
        # phone number that begins with the area code "208-"
        # Call the map function and pass add_area_code and the list of phone numbers
        new_numbers = list(map(add_area_code, phone_numbers))  # <-- FIXED

        # Print the list with the corrected phone numbers.
        print(new_numbers)

    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")


def add_area_code(phone_number):
    """Phone numbers in the U.S. are often stored as ten digits and
    two dashes in this format: "ddd-ddd-dddd" where each d is a digit.
    If the length of phone_number is less than 12 characters, add the
    area code "208-" at the beginning of phone_number and return
    phone_number.

    Parameter phone_number: a string of digits formatted as
        "ddd-dddd" or "ddd-ddd-dddd"
    Return: a string of digits formated as "ddd-ddd-dddd"
    """
    # If the phone number is less than 12 characters (doesn't include area code)
    if len(phone_number) < 12:
        phone_number = "208-" + phone_number
    return phone_number  # <-- FIXED


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list


if __name__ == "__main__":
    main()
