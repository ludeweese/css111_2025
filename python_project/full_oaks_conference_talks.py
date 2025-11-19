#Lucilene DeWeese
#Python Project: This program loads President Oaks conference talks from a CSV file and provides functions to list talks and search them by year.


import csv  # Import CSV module to read CSV files

# -----------------------------
# GLOBAL LIST
# -----------------------------
# This list will store all conference talks as dictionaries
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
                # Append each row as a dictionary to the list
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
    """
    Returns the full list of talks.
    """
    return conference_talks

# -----------------------------
# FUNCTION: get_talks_by_year
# -----------------------------
def get_talks_by_year(year):
    """
    Returns a list of talks that match a given year.
    """
    return [talk for talk in conference_talks if str(year) in talk['Date']]

# -----------------------------
# FUNCTION: display_talks
# -----------------------------
def display_talks(talk_list):
    """
    Prints a list of talks in a readable format.
    """
    if not talk_list:
        print("No talks found.")
        return
    for talk in talk_list:
        print(f"{talk['Date']} - {talk['Title']} ({talk['Session']})\nLink: {talk['URL']}\n")

# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    # Load talks from CSV
    load_talks_from_csv("president_Oaks_Talks.csv")
    
    # Display all talks
    print("=== All President Oaks Conference Talks ===\n")
    display_talks(get_all_talks())
    
    # Example: search talks by year (uncomment to use)
    # print("=== Talks from 2020 ===\n")
    # display_talks(get_talks_by_year(2020))
