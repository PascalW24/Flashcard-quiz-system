import csv
import random
from datetime import datetime


def load_flashcards():
    """This function loads the flashcards data from the csv file."""
    try:
        with open("flashcard_words.csv", encoding="utf-8", mode="r") as f:
            reader = csv.DictReader(f)
            flashcards = list(reader)
    except FileNotFoundError:
        print(f"File 'flashcard_words.csv' not found.")
        return False
    return flashcards


def save_word(question, user_answer):
    """This function saves the user progress in a txt file."""
    with open("user_progress.txt", encoding = "utf-8", mode = "a") as writer:
        writer.write(f'- {question} -> {user_answer}\n')


def clear_file_or_keeping():
    """This function prompts the user to decide whether to clear all contents of the progress file."""
    user_choice = '-'
    while user_choice not in ("", "clear"):
        user_choice = input(
            'Thanks for exploring these flashcards — keep discovering.\nPress Enter to keep your progress or type "clear" to delete all saved progress\n').strip().lower()
        if user_choice == "clear":
            with open("user_progress.txt", encoding = "utf-8", mode = "w") as writer:
                writer.write("")
        exit(0)


def end_quiz(entry, opposite, correct_answer_count, overall_tries, number_of_entry):
    """This function ends the quiz when the user wants to quit."""
    if overall_tries > 1 and number_of_entry > 1 : # Avoiding division by zero
        overall_tries -= 1
        number_of_entry -= 1
    percentage = round(correct_answer_count / number_of_entry * 100)
    accuracy = round(correct_answer_count / overall_tries * 100)
    print(
        f'The correct answer was "{entry[opposite]}".\nYour score is {correct_answer_count} out of {number_of_entry} questions: ({percentage}%), and your accuracy {accuracy}%')
    with open("user_progress.txt", encoding = "utf-8", mode = "a") as writer:
        writer.write(f'Your performance: {percentage}% correct answers with an accuracy rate of {accuracy}%.\n\n')
    clear_file_or_keeping() # Ask the user whether they want to keep the progress in the progress file or not


def finish_quiz(correct_answer_count, overall_tries, number_of_entry):
    """This function ends the quiz when there are no words left."""
    percentage = round(correct_answer_count / number_of_entry * 100)
    accuracy = round(correct_answer_count / overall_tries * 100)
    print(
        f'No more flashcards left. Great job!\nYour score is {correct_answer_count} out of {number_of_entry} questions: ({percentage}%), and your accuracy {accuracy}%')
    with open("user_progress.txt", encoding="utf-8", mode="a") as writer:
        writer.write(f'Your performance: {percentage}% correct answers with an accuracy rate of {accuracy}%.\n\n')
    clear_file_or_keeping() # Ask the user whether they want to keep the progress in the progress file or not


def skip_word(entry, opposite, overall_tries, number_of_tries_per_word,flashcards):
    """This function skips a word from the flashcards and puts it back to the pool of words."""
    overall_tries -= 1 # Undo the try we already counted for this word
    print(f'The correct answer was "{entry[opposite]}". You tried "{number_of_tries_per_word}" times ')
    flashcards.append(entry) # Put the word back into the pool of flashcards
    return overall_tries


def main():
    flashcards = load_flashcards() # Load cards
    if not flashcards:  # Checks if file was loaded
        print('Exiting')
        return
    # Choose the language
    the_type = "type"
    print("Welcome to your flashcard practice session! You’ll practice vocabulary and your progress will be tracked.")
    language = input("Which language do you want to translate from - German or English?\n").strip().lower()
    while language not in ("english", "german"):
        language = input("The only supported options are: German or English?\n").strip().lower()

    correct_answer_count = 0
    overall_tries = 0
    number_of_entry = 0
    opposite = "english" if language == "german" else "german"
    print(f"Awesome! Let's begin... translate the words from {language.title()} into {opposite.title()}.")
    with open("user_progress.txt", encoding = "utf-8", mode = "a") as writer: # Write the start time and date into the progress file
        writer.write(
            f'Practice session started at {datetime.now().strftime('%a %d %b %Y, %I:%M%p')} ({language.capitalize()} -> {opposite.capitalize()})\n')

    while flashcards:
        entry = random.choice(flashcards)
        flashcards.remove(entry) # To prevent repeating words
        number_of_entry += 1
        print(f'\n{entry[language]}, "{entry[the_type]}"') # Display the word and its type
        number_of_tries_per_word = 0
        user_answer = input(
            f'Translate: "{entry[language]}" or type "n" for the next question, or type "x" to end the quiz\n')
        overall_tries += 1
        if user_answer.lower() == "n": # The user wants to skip the word
            overall_tries = skip_word(entry, opposite, overall_tries, number_of_tries_per_word,flashcards)
        elif user_answer.lower() == "x": # The user wants to end the quiz
            end_quiz(entry, opposite, correct_answer_count, overall_tries, number_of_entry)
        elif user_answer == entry[opposite]: # The user answer was correct
            print("Correct")
            correct_answer_count += 1
            save_word(entry[language], user_answer)

        else: # The user answer was wrong or invalid
            while user_answer != entry[opposite]:
                number_of_tries_per_word += 1
                overall_tries += 1
                if user_answer.isalpha(): # The user answer was wrong
                    user_answer = input(
                        'It’s incorrect.\nPlease try again, or type "n" for the next question, or "x" to end the quiz.\n')
                elif not user_answer.isalpha(): # The user answer was invalid
                    print('Invalid Input, only words are accepted')
                    user_answer = input(
                        'Please try again, or type "n" for the next question, or "x" to end the quiz.\n')
                if user_answer.lower() == "n": # The user wants to skip the word
                    overall_tries = skip_word(entry, opposite, overall_tries, number_of_tries_per_word,flashcards)
                    break
                elif user_answer.lower() == "x": # The user wants to end the quiz
                    end_quiz(entry, opposite, correct_answer_count, overall_tries, number_of_entry)
                elif user_answer == entry[opposite]: # The user answer was correct
                    number_of_tries_per_word += 1
                    print("It's correct, you tried", number_of_tries_per_word, "times to answer correctly")
                    save_word(entry[language], user_answer)
                    correct_answer_count += 1
    finish_quiz(correct_answer_count, overall_tries, number_of_entry) # No words left in flashcards


if __name__ == '__main__':
    main()
