# example_3.py

def main():
    # Read the contents of plants.txt into a list.
    plants_list = read_list("plants.txt")

    # Print the first and last plant in the list.
    print("The first plant is:", plants_list[0])
    print("The last plant is:", plants_list[-1])

    # Print the total number of plants.
    print("Total plants in the list:", len(plants_list))


def read_list(filename):
    """Read the contents of a text file into a list and return it."""
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list


# Start the program
if __name__ == "__main__":
    main()
