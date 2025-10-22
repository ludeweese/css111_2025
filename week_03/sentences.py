#Lucilene DeWeese
# Program to generate random simple English sentences
# Purpose: Practice writing and calling functions with parameters

# randomly select words from a list:
import random


# Function to return a random determiner depending on quantity
def get_determiner(quantity):
    """Return a randomly chosen determiner (article).
    If quantity is 1 → singular words
    Otherwise → plural words
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1 → singular noun
    Otherwise → plural noun
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

# Choose and return a random verb based on the given tense and quantity
def get_verb(quantity, tense):
    """Return a randomly chosen verb based on tense and quantity."""
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present":
        if quantity == 1:  # singular subject
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:  # plural subject
            words = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]

    else:  # future tense
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    return random.choice(words)

# Build a full sentence by combining a determiner, a noun, and a verb
def make_sentence(quantity, tense):
    """Build and return a sentence:
    [Determiner] + [Noun] + [Verb].
    Example: "The cat runs."
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    # Build the sentence
    sentence = f"{determiner} {noun} {verb}."
    return sentence.capitalize()  # Capitalize first word


def main():
    """Print six sentences with different quantity/tense combinations."""

    # Single noun sentences
    print(make_sentence(1, "past"))     # e.g. "One cat ran."
    print(make_sentence(1, "present"))  # e.g. "A dog eats."
    print(make_sentence(1, "future"))   # e.g. "The girl will sleep."

    # Plural noun sentences
    print(make_sentence(2, "past"))     # e.g. "Many boys laughed."
    print(make_sentence(2, "present"))  # e.g. "Some men walk."
    print(make_sentence(2, "future"))   # e.g. "The children will write."


# Call main function only if this file is run directly
if __name__ == "__main__":
    main()
