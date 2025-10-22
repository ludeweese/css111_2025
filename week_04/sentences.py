# Lucilene DeWeese- Week 04

# Import random to choose words randomly
import random 

def main():
    """
    Generate and print six sentences with different quantities and verb tenses.
    Loops through all required singular/plural and past/present/future combinations.
    """
    # List of (quantity, tense) combinations for the six sentences
    sentence_specs = [
        (1, "past"), (1, "present"), (1, "future"),
        (2, "past"), (2, "present"), (2, "future")
    ]
    
    # Loop through each combination and print a sentence
    for quantity, tense in sentence_specs:
        sentence = make_sentence(quantity, tense)
        print(sentence)

def make_sentence(quantity, tense):
    """
    Build and return a sentence with a determiner, noun, two prepositional
    phrases, and a verb. (Exceeds requirements by adding two phrases.)

    Sentence Structure: Determiner + Noun + Phrase 1 + Verb + Phrase 2

    Parameters:
        quantity: 1 for singular, 2 for plural nouns
        tense: "past", "present", or "future"
    Return: a complete, capitalized sentence string.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    
    # Exceeding Requirement: Two prepositional phrases
    # Phrase 1 modifies the subject (noun), placed before the verb.
    prepositional_phrase_1 = get_prepositional_phrase(quantity)
    # Phrase 2 modifies the verb, placed at the end.
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    
    # Construct the sentence: Subj + Phrase1 + Verb + Phrase2
    sentence = (f"{determiner} {noun} {prepositional_phrase_1} "
                f"{verb} {prepositional_phrase_2}.")
    
    # Return the sentence with the first letter capitalized
    return sentence.capitalize()


def get_determiner(quantity):
    """Return a randomly chosen determiner based on quantity (singular or plural)."""
    words = ["a", "one", "the"] if quantity == 1 else ["some", "many", "the"]
    return random.choice(words)


def get_noun(quantity):
    """Return a randomly chosen noun based on quantity (singular or plural)."""
    singular = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(singular if quantity == 1 else plural)


def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense."""
    verbs = {
        "past": ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
        "present_singular": ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
        "present_plural": ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
        "future": ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    }
    if tense == "past":
        return random.choice(verbs["past"])
    elif tense == "present":
        key = "present_singular" if quantity == 1 else "present_plural"
        return random.choice(verbs[key])
    else:  # future tense
        return random.choice(verbs["future"])


def get_preposition():
    """Return a randomly chosen preposition from a list of 30 options."""
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at",
        "before", "behind", "below", "beyond", "by", "despite", "except",
        "for", "from", "in", "into", "near", "of", "off", "on", "onto",
        "out", "over", "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)


def get_prepositional_phrase(quantity):
    """
    Return a prepositional phrase composed of a preposition,
    a determiner, and a noun based on the given quantity.
    """
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"


# Run the program
if __name__ == "__main__":
    main()