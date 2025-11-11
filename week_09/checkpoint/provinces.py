def main():
    # Read provinces.txt into a list
    provinces = read_list("provinces.txt")

    # Print the entire list
    print(provinces)

    # Remove the first and last elements
    provinces.pop(0)       # first element
    provinces.pop(-1)      # last element

    # Replace all occurrences of "AB" with "Alberta"
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

    # Count how many times "Alberta" appears
    ab_count = provinces.count("Alberta")
    print(f"Alberta occurs {ab_count} times in the modified list.")


def read_list(filename):
    """Read a text file into a list, one line per element."""
    text_list = []
    with open(filename, "rt") as file:
        for line in file:
            text_list.append(line.strip())
    return text_list


if __name__ == "__main__":
    main()
