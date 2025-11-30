import csv
import random
from datetime import datetime


def load_flashcards():
    try:
        with open("flashcard_words.csv",encoding="utf-8", mode="r") as f:
            reader = csv.DictReader(f)
            flashcards = list(reader)
    except FileNotFoundError:
        print(f"⚠️  File 'flashcard_words.csv' not found.")
        return False #should we return here or exit(1)
    return flashcards

def save_word(question,user_answer):
    with open("user_progress.txt", "a") as writer:
        writer.write(f'- {question} -> {user_answer}\n')

def clear_file():
    with open("user_progress.txt", "w") as writer:
        writer.write("")

def end_quiz(entry, opposite, correct_answer_count, overall_tries):
    overall_tries -= 1
    print(f'The correct answer was "{entry[opposite]}".\nYour Score is "{correct_answer_count}", and you tried "{overall_tries}" times')
    user_choice = '-'
    while user_choice not in ("", "clear"):
        user_choice = input('Press Enter to keep your progress or "clear" to delete all saved progress\n').strip().lower()
        if user_choice == "clear":
            clear_file()
    exit(0)

def skip_word(entry, opposite, overall_tries, number_of_tries_per_word):
    overall_tries -= 1
    print(f'The correct answer was "{entry[opposite]}". You tried "{number_of_tries_per_word}" times ')
    return overall_tries

def main():
    #load cards
    flashcards = load_flashcards()
    if not flashcards: #Checks if file was loaded
        print('Exiting')
        return #should we return here or exit(1)
    # Choose the language
    language= ""
    while language not in ("english", "german"):
        language = input("Choose the quiz language: German or English:\n ").strip().lower()
    correct_answer_count = 0
    overall_tries = 0
    opposite = "english" if language == "german" else "german"
    with open("user_progress.txt", "a") as writer:
        writer.write(f'Practice session started at {datetime.now().strftime('%a %d %b %Y, %I:%M%p')} ({language.capitalize()} -> {opposite.capitalize()})\n')
    while True:
        entry = random.choice(flashcards)
        flashcards.remove(entry)
        print(f'\n"{entry[language]}"')
        number_of_tries_per_word = 0
        user_answer = input(f'Translate: "{entry[language]}" or type "n" for the next question, or type "x" to end the quiz\n')
        overall_tries += 1

        if not user_answer.isalpha() :
            print('Invalid Input, only words are accepted')
        if user_answer.lower() == "n":
            overall_tries = skip_word(entry, opposite, overall_tries, number_of_tries_per_word)
        elif user_answer.lower() == "x":
            end_quiz(entry, opposite, correct_answer_count, overall_tries)
        elif user_answer == entry[opposite]:
            print("correct")
            correct_answer_count += 1
            save_word(entry[language],user_answer)
        else:
            number_of_tries_per_word = 0
            while user_answer != entry[opposite]:
                number_of_tries_per_word += 1
                overall_tries += 1

                user_answer = input('It’s incorrect.\nPlease try again, or type “n” for the next question, or “x” to end the quiz.\n')
                if not user_answer.isalpha():
                    print('Invalid Input, only words are accepted')
                if user_answer.lower() == "n":
                    overall_tries = skip_word(entry, opposite, overall_tries, number_of_tries_per_word)
                    break
                elif user_answer.lower() == "x":
                    end_quiz(entry, opposite, correct_answer_count, overall_tries)
                elif user_answer == entry[opposite]:
                    number_of_tries_per_word+= 1
                    print("It's correct, you tried ", number_of_tries_per_word, " times to answer correctly")
                    save_word(entry[language],user_answer)
                    correct_answer_count += 1

if __name__== '__main__':
    main()
