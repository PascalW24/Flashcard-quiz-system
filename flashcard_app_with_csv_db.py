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
    #Choos the language
    language = str(input("Choose the quiz language: German or English: "))
    correct_answer_count = 0

    overall_tries=0


    while True:
        # def list of used up words
        opposite = "English" if language == "German" else "German"
        entry = random.choice(flashcards)
        flashcards.remove(entry)
        print(entry[language])
        number_of_tries_per_word = 0
        user_answer = input(f"Translate: {entry[language]} or type exit() to End the Quiz\n")
        overall_tries += 1
        if user_answer == "exit()":
            print(f"your score {correct_answer_count} and you tried{overall_tries}")
            exit(0)
        if user_answer == entry[opposite]:

            print("correct")
            correct_answer_count+=1

        else:
            number_of_tries_per_word += 1
            while user_answer != entry[opposite]:
                number_of_tries_per_word += 1
                overall_tries += 1
                user_answer = input("it is wrong, guess again or type next() for the next question\n")
                if user_answer == "next()":
                    print(f"it was {entry[opposite]}")
                    break
                if user_answer == "exit()":
                    print(f"your score {correct_answer_count} and you tried {overall_tries}")
                    exit(0)
                elif user_answer == entry [opposite]:
                    print("you tried ", number_of_tries_per_word, "to answer correctly")
                    correct_answer_count += 1





# def


# def


# variables: amount_tries_word, amount_tries_overall, amount_right_words, variables for the words






main()
