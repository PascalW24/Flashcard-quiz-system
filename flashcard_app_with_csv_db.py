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


def save_answer(user_answer):
    with open("user_answers.txt", "a") as writer:
        writer.write(user_answer + "\n")


def main():
    # Load cards
    flashcards = load_flashcards()
    if not flashcards: #Checks if file was loaded
        print("Exiting")
        return
    #Choose the language
    while language not in ("english", "german"):
        language = input("Choose the quiz language: German or English:\n ").strip().lower()
    correct_answer_count = 0
    overall_tries = 0

    while True:

        opposite = "english" if language == "german" else "german"
        entry = random.choice(flashcards)
        flashcards.remove(entry)
        print(entry[language])
        number_of_tries_per_word = 0
        user_answer = input(f'Translate: "{entry[language]}" or type "n" for the next question, or type "x" to end the quiz\n')
        overall_tries += 1

        if user_answer.isdigit():
            print('Invalid Input, only words are accepted')
        if user_answer == "n":
            overall_tries -= 1
            print(f'The correct answer was "{entry[opposite]}". You tried {number_of_tries_per_word} times ')
        elif user_answer == "x":
            overall_tries -= 1
            print(f"Your Score is {correct_answer_count}, and you tried {overall_tries} times ")
            exit(0)
        elif user_answer == entry[opposite]:
            print("correct")
            correct_answer_count += 1
            save_answer(user_answer)
        else:
            number_of_tries_per_word += 1
            while user_answer != entry[opposite]:
                number_of_tries_per_word += 1
                overall_tries += 1
                save_answer(user_answer)
                user_answer = input(' It is wrong guess again or type "n" for the next question or "x" to end the quiz \n')
                if user_answer.isdigit():
                    print('Invalid Input, only words are accepted')
                if user_answer == "n":
                    overall_tries -= 1
                    print(f'The correct answer was "{entry[opposite]}". You tried {number_of_tries_per_word} times ')
                    break
                elif user_answer == "x":
                    overall_tries -= 1
                    print(f"Your Score {correct_answer_count} and you tried {overall_tries} times")
                    exit(0)
                elif user_answer == entry[opposite]:
                    print("It's correct, you tried ", number_of_tries_per_word, " times to answer correctly")
                    save_answer(user_answer)
                    correct_answer_count += 1


# variables: amount_tries_word, amount_tries_overall, amount_right_words, variables for the words


if __name__ == "__main__":
    main()
