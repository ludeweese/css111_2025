# map and filter
# Example 5

def read_list(filename):
    """Read the contents of a text file into a list."""
    with open(filename, "rt") as file:
        text = file.read()
        lines = text.splitlines()
        return lines


def main():
    # Read a file that contains a list
    # of Canadian province names.
    provinces_list = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print("Original list of provinces:")
    print(provinces_list)
    print()

    # Define a nested function that converts AB to Alberta.
    def alberta_from_ab(province_name):
        if province_name == "AB":
            province_name = "Alberta"
        return province_name

    # Replace all occurrences of "AB" with "Alberta" by
    # calling the map function and passing the alberta_from_ab
    # function and provinces_list into the map function.
    new_list = list(map(alberta_from_ab, provinces_list))
    print("List of provinces after AB was changed to Alberta:")
    print(new_list)
    print()

    # Define a lambda function that returns True if a
    # province's name is Alberta and returns False otherwise.
    is_alberta = lambda name: name == "Alberta"

    # Filter the new list to only those provinces that
    # are "Alberta" by calling the filter
