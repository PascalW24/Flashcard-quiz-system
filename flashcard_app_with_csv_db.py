import csv
import random



def load_flashcards():
    flashcards = []
    try:
        with open("flashcard_words.csv", "r") as f:
            reader = csv.DictReader(f)
            flashcards = list(reader)
            print(flashcards)
    except FileNotFoundError:
        print(f"⚠️  File 'flashcard_words.csv' not found.")
    return flashcards


def main():
    flashcards = load_flashcards()


#Choose the language
while True:
    language = int(input("Enter 0 for German and 1 for English words: "))
    if language == 0:
        print("German")
    elif language == 1:
        print("English")
    else:
        print("Invalid input. Please try again.")

# def


# def


# variables: amount_tries_word, amount_tries_overall, amount_right_words, variables for the words


def quiz():
    while(True):




main()
