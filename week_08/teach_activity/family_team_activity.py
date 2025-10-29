#Team Activity week 08

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1695, 1752],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1737, 1803],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1802, 1858],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1899, 1945]
    }

    marriages_dict = {
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1829],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)


# -- CORE REQUIREMENT 1 --
def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death."""
    print("Ages at Death")
    for key, value in people_dict.items():
        name = value[NAME_INDEX]
        birth_year = value[BIRTH_YEAR_INDEX]
        death_year = value[DEATH_YEAR_INDEX]
        age = death_year - birth_year
        # STRETCH: also print birth and death years
        print(f"{name} ({birth_year}–{death_year}) {age}")


# -- CORE REQUIREMENT 2 --
def count_genders(people_dict):
    """Count and print the number of males and females."""
    print("Genders")
    male_count = 0
    female_count = 0

    for value in people_dict.values():
        gender = value[GENDER_INDEX]
        if gender == "M":
            male_count += 1
        elif gender == "F":
            female_count += 1

    print(f"Number of males: {male_count}")
    print(f"Number of females: {female_count}")


# -- CORE REQUIREMENT 3 --
def print_marriages(marriages_dict, people_dict):
    """For each marriage, print readable information."""
    print("Marriages")
    # Dictionary to count marriages for stretch goal
    marriage_count = {}

    for marriage in marriages_dict.values():
        husband_key = marriage[HUSBAND_KEY_INDEX]
        wife_key = marriage[WIFE_KEY_INDEX]
        wedding_year = marriage[WEDDING_YEAR_INDEX]

        # Get husband and wife data
        husband = people_dict[husband_key]
        wife = people_dict[wife_key]

        # Calculate ages at wedding
        husband_age = wedding_year - husband[BIRTH_YEAR_INDEX]
        wife_age = wedding_year - wife[BIRTH_YEAR_INDEX]

        # Print marriage info
        print(f"{husband[NAME_INDEX]} {husband_age} > {wedding_year} < {wife[NAME_INDEX]} {wife_age}")

        # STRETCH: count marriages for each person
        marriage_count[husband_key] = marriage_count.get(husband_key, 0) + 1
        marriage_count[wife_key] = marriage_count.get(wife_key, 0) + 1

    # STRETCH: show number of marriages and most-married person
    print()
    print("Marriages Per Person")
    most_married_key = None
    most_married_count = 0
    for person_key, count in marriage_count.items():
        name = people_dict[person_key][NAME_INDEX]
        print(f"{name} was married {count} time{'s' if count > 1 else ''}")
        if count > most_married_count:
            most_married_count = count
            most_married_key = person_key

    most_married_name = people_dict[most_married_key][NAME_INDEX]
    print()
    print(f"The person who married the most times was {most_married_name} ({most_married_count} marriages).")


# If this file was executed like this:
# > python family_history.py
if __name__ == "__main__":
    main()
