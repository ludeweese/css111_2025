# example_4.py

def main():
    # Create a list that will be written to the file.
    plants = [
        "baobab",
        "kangaroo paw",
        "eucalyptus",
        "heliconia",
        "tulip",
        "chupasangre cactus",
        "prickly pear cactus",
        "ginkgo biloba"
    ]

    # Write the list of plants to the text file.
    write_list("plants.txt", plants)

    print("plants.txt has been created with plant names!")


def write_list(filename, text_list):
    """Write the contents of a list to a text file.
    Each element in the list will be written on its own line.

    Parameter filename: the name of the text file to write
    Parameter text_list: the list of strings to write
    """
    # Open the file in write text mode ("wt").
    with open(filename, "wt") as text_file:
        for item in text_list:
            text_file.write(item + "\n")


# Call main to start this program.
if __name__ == "__main__":
    main()
