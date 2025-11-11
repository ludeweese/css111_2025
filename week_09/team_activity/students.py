# Team Activity Students.py
# Program to look up student names using their I-Number from a CSV file
# Stretch Challenge: Includes validation, dash removal, and organized functions

def main():
    """Main function that calls read_dictionary and find_student"""
    
    # Read the students.csv file into a dictionary
    students_dict = read_dictionary("students.csv")
    
    # Stretch Challenge: Get I-Number from user and find the student
    find_student(students_dict)


def read_dictionary(filename):
    """Read the contents of a CSV file into a dictionary and return it.
    
    Parameters:
        filename: the name of the CSV file to read.
    Return: a dictionary with I-Number as key and Name as value.
    """
    students = {}
    
    with open(filename, "r") as file:
        # Skip the first line (header)
        next(file)
        
        # Read each line in the CSV
        for line in file:
            # Remove whitespace and newline characters
            clean_line = line.strip()
            
            # Split the line by comma into I-Number and Name
            i_number, name = clean_line.split(",")
            
            # Add to dictionary
            students[i_number] = name
    
    return students


def find_student(students_dict):
    """Get an I-Number from the user, validate it, and find the student.
       Stretch Challenge: Includes dash removal and input validation.
    """
    
    # Ask the user for an I-Number
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    
    # Stretch Challenge: Remove any dashes entered by the user
    i_number = i_number.replace("-", "")
    
    # Stretch Challenge: Validate that input contains only digits
    if not i_number.isdigit():
        print("Invalid I-Number")
        return
    
    # Stretch Challenge: Check for too few digits
    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        return
    
    # Stretch Challenge: Check for too many digits
    elif len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        return
    
    # Lookup the student in the dictionary
    if i_number in students_dict:
        print(students_dict[i_number])
    else:
        print("No such student")


# If this file is run directly, call main()
if __name__ == "__main__":
    main()
