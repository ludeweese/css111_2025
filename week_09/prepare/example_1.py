# example_1.py

def main():
    # Read the contents of a text file named plants.txt into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and return the list.
    Each element in the list will contain one line of text from the text file.
    """
    text_list = []

    # Open the text file for reading (text mode).
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list


if __name__ == "__main__":
    main()
