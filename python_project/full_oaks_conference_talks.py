#Lucilene DeWeese
#Python Project: President Oaks Conference Talks Manager
#This program loads President Oaks conference talks from a CSV file and provides functions
#to list talks, search by year, search by keyword, sort, and save results.

import csv  # Import CSV module to read/write CSV files

# -----------------------------
# GLOBAL LIST
# -----------------------------
# This list stores all conference talks as dictionaries
conference_talks = []

# -----------------------------
# FUNCTION: load_talks_from_csv
# -----------------------------
def load_talks_from_csv(filename):
    """
    Loads talks from a CSV file into the global conference_talks list.
    Each talk is stored as a dictionary with keys: Title, Date, Session, URL.
    """
    global conference_talks
    conference_talks = []  # Reset list each time this function is called
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Read CSV with headers
            for row in reader:
                conference_talks.append({
                    "Title": row["Title"],
                    "Date": row["Date"],
                    "Session": row["Session"],
                    "URL": row["URL"]
                })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# -----------------------------
# FUNCTION: get_all_talks
# -----------------------------
def get_all_talks():
    """Returns the full list of talks."""
    return conference_talks

# -----------------------------
# FUNCTION: get_talks_by_year
# -----------------------------
def get_talks_by_year(year):
    """Returns a list of talks that match a given year."""
    return [talk for talk in conference_talks if str(year) in talk['Date']]

# -----------------------------
# FUNCTION: get_talks_by_keyword
# -----------------------------
def get_talks_by_keyword(keyword):
    """Returns a list of talks where the title contains the keyword (case-insensitive)."""
    return [talk for talk in conference_talks if keyword.lower() in talk['Title'].lower()]

# -----------------------------
# FUNCTION: sort_talks
# -----------------------------
def sort_talks(key='Title', reverse=False):
    """
    Returns talks sorted by 'Title' or 'Date'.
    Default is sorting by Title alphabetically.
    """
    return sorted(conference_talks, key=lambda talk: talk[key], reverse=reverse)

# -----------------------------
# FUNCTION: save_talks_to_csv
# -----------------------------
def save_talks_to_csv(talk_list, filename):
    """
    Save a list of talks to a new CSV file.
    """
    if not talk_list:
        print("No talks to save.")
        return
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Title', 'Date', 'Session', 'URL'])
        writer.writeheader()
        writer.writerows(talk_list)
    print(f"Saved {len(talk_list)} talks to '{filename}'.")

# -----------------------------
# FUNCTION: display_talks
# -----------------------------
def display_talks(talk_list):
    """Prints a list of talks in a readable format."""
    if not talk_list:
        print("No talks found.")
        return
    for talk in talk_list:
        print(f"{talk['Date']} - {talk['Title']} ({talk['Session']})\nLink: {talk['URL']}\n")

# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    load_talks_from_csv("president_Oaks_Talks.csv")

    while True:
        print("\n--- President Oaks Talks Manager ---")
        print("1. Show all talks")
        print("2. Show talks by year")
        print("3. Search talks by keyword")
        print("4. Sort talks by title")
        print("5. Save talks to CSV")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_talks(get_all_talks())
        elif choice == "2":
            year = input("Enter year: ")
            display_talks(get_talks_by_year(year))
        elif choice == "3":
            keyword = input("Enter keyword: ")
            display_talks(get_talks_by_keyword(keyword))
        elif choice == "4":
            sorted_list = sort_talks()
            display_talks(sorted_list)
        elif choice == "5":
            filename = input("Enter filename to save: ")
            save_talks_to_csv(get_all_talks(), filename)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
