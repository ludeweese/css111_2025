# example_2.py

def main():
    # Open plants.txt in read mode
    with open("plants.txt", "rt") as text_file:
        # Read the file line by line
        for line in text_file:
            clean_line = line.strip()  # remove spaces and newlines
            print(clean_line)           # print each plant name on its own line


if __name__ == "__main__":
    main()
