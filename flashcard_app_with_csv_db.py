import csv

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

main()
