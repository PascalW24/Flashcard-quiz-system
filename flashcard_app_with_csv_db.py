import csv
import random


def load_flashcards():
    flashcards = []
    try:
        with open("flashcard_words.csv", "r") as f:
            reader = csv.DictReader(f)
            flashcards = list(reader)
    except FileNotFoundError:
        print(f"⚠️  File 'flashcard_words.csv' not found.")
    return flashcards


def main():

    flashcards = load_flashcards()
    # Choose the language
    language = input("Choose the quiz language: German or English:\n ").strip().lower()
    correct_answer_count = 0

    overall_tries = 0

    while True:
        # def list of used up words
        opposite = "english" if language == "german" else "german"
        entry = random.choice(flashcards)
        flashcards.remove(entry)
        print(entry[language])
        number_of_tries_per_word = 0
        user_answer = input(f'Translate: "{entry[language]}" or type "n" for the next question, or type "x" to end the quiz\n')
        overall_tries += 1
        with open('user_answers.txt', 'a') as writer:
            writer.write(user_answer + '\n')
        if user_answer.isdigit():
            print('Invalid Input, only words are accepted')
            input('Please try again or type "n" for the next question, or "x" to end the quiz \n')
        if user_answer == "n":
            overall_tries -= 1
            print(f'The correct answer was "{entry[opposite]}". You tried {number_of_tries_per_word} times ')
        if user_answer == "x":
            overall_tries -= 1
            print(f"Your Score is {correct_answer_count}, and you tried {overall_tries} times ")
            exit(0)
        if user_answer == entry[opposite]:
            print("correct")
            correct_answer_count += 1

        else:
            number_of_tries_per_word += 1
            while user_answer != entry[opposite]:
                number_of_tries_per_word += 1
                overall_tries += 1
                user_answer = input(' It is wrong guess again or type "n" for the next question or "x" to end the quiz \n')
                with open('user_answers.txt', 'a') as writer:
                    writer.write(user_answer + '\n')
                if user_answer.isdigit():
                    print('Invalid Input, only words are accepted')
                    input('Please try again or type "n" for the next question, or "x" to end the quiz \n')

                if user_answer == "n":
                    overall_tries -= 1
                    print(f'The correct answer was "{entry[opposite]}". You tried {number_of_tries_per_word} times ')
                    break
                if user_answer == "x":
                    overall_tries -= 1
                    print(f"Your Score {correct_answer_count} and you tried {overall_tries} times")
                    exit(0)
                elif user_answer == entry[opposite]:
                    print("It's correct, you tried ", number_of_tries_per_word, " times to answer correctly")
                    correct_answer_count += 1







# variables: amount_tries_word, amount_tries_overall, amount_right_words, variables for the words


main()
