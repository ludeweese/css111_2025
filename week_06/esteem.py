#Team Activity
# Step 1: Plan the Functions
# - get_user_response(statement): Ask the user for input (D, d, a, A) and validate it.
# - score_response(response, is_positive): Convert the response into points based on whether the statement is positive or negative.
# - main(): Display intro, loop through statements, get responses, compute total score, and display it.

# Step 2: Map Scores
# Positive Statements (1, 2, 4, 6, 7):
#   D -> 0, d -> 1, a -> 2, A -> 3
# Negative Statements (3, 5, 8, 9, 10):
#   D -> 3, d -> 2, a -> 1, A -> 0

# Function to get a valid user response for a statement
def get_user_response(statement):
    while True:
        # Prompt the user to enter D, d, a, or A for the given statement
        response = input(f"{statement}\n   Enter D, d, a, or A: ")
        # Check if the input is valid
        if response in ['D', 'd', 'a', 'A']:
            return response  # Return valid response
        else:
            # Print error message if input is invalid
            print("Invalid input. Please enter D, d, a, or A.")

# Function to calculate the score for a response
def score_response(response, is_positive):
    # Define scoring for positive statements
    positive_scores = {'D':0, 'd':1, 'a':2, 'A':3}
    # Define scoring for negative statements
    negative_scores = {'D':3, 'd':2, 'a':1, 'A':0}
    
    # Return score based on whether statement is positive or negative
    if is_positive:
        return positive_scores[response]
    else:
        return negative_scores[response]

# Main function that runs the program
def main():
    # Print introductory text explaining the program
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")
    
    # List of the 10 Rosenberg self-esteem statements
    statements = [
        "1. I feel that I am a person of worth, at least on an equal plane with others.",
        "2. I feel that I have a number of good qualities.",
        "3. All in all, I am inclined to feel that I am a failure.",
        "4. I am able to do things as well as most other people.",
        "5. I feel I do not have much to be proud of.",
        "6. I take a positive attitude toward myself.",
        "7. On the whole, I am satisfied with myself.",
        "8. I wish I could have more respect for myself.",
        "9. I certainly feel useless at times.",
        "10. At times I think I am no good at all."
    ]
    
    # List of indexes for positive statements (0-based)
    positive_statements = [0, 1, 3, 5, 6]
    
    # Initialize total score to 0
    total_score = 0
    
    # Loop through each statement
    for i, statement in enumerate(statements):
        # Get valid response from the user
        response = get_user_response(statement)
        # Determine if the current statement is positive
        is_positive = i in positive_statements
        # Calculate score for this response and add to total
        total_score += score_response(response, is_positive)
    
    # Print the user's total score
    print(f"\nYour score is {total_score}.")
    # Print a note if the score indicates potentially low self-esteem
    print("A score below 15 may indicate problematic low self-esteem.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()