#Team Activity week 07

# Import the random module for generating random numbers and choosing words
import random  

# Function to append random numbers to a list
def append_random_numbers(numbers_list, quantity=1):
    # Create a list of 'quantity' random numbers between 0 and 100, rounded to 1 decimal place
    new_numbers = [round(random.uniform(0, 100), 1) for _ in range(quantity)]
    # Add all the new numbers to the end of the existing numbers_list
    numbers_list.extend(new_numbers)

# Function to append random words to a list (Stretch Challenge)
def append_random_words(words_list, quantity=1):
    # List of sample words to choose from
    sample_words = ['love', 'smile', 'join', 'cloud', 'head', 'star', 'moon', 'sun', 'tree', 'joy']
    # Randomly select 'quantity' words from sample_words
    new_words = [random.choice(sample_words) for _ in range(quantity)]
    # Add the selected words to the end of the existing words_list
    words_list.extend(new_words)

# Main function that runs the program
def main():
    # Create the initial list of numbers
    numbers = [16.2, 75.1, 52.3]
    print("numbers", numbers)  
    
    # Add 1 random number to the numbers list (default quantity=1)
    append_random_numbers(numbers)
    print("numbers", numbers) 
    
    # Add 3 random numbers to the numbers list
    append_random_numbers(numbers, 3)
    print("numbers", numbers)  
    
    # Create the initial list of words (Stretch Challenge)
    words = ['join', 'love', 'smile']
    # Add 3 random words to the words list
    append_random_words(words, 3)
    print("words", words)  

# Check if this file is being run directly
if __name__ == "__main__":
    main()  
