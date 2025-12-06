# Flashcard-quiz-system
This project is intended to:

- Develop an interactive console application that helps users learn and test English–German vocabulary 
- Apply basic Python programming concepts learned in the Programming Foundations module
- Demonstrate the use of console interaction, data validation, and file processing
- Produce clean, well-structured, and documented code

---
**Problem**

  Around 15.4 million people learn German as a foreign language worldwide. Many people struggle with memorizing vocabulary, which leads to slower learning progress, mental frustration, and a poor progress overview.  


---
**Scenario**

The program loads vocabulary flashcards from a CSV file and quizzes the user by showing a word in one language and asking for its translation. Words are presented in random order, and the program tracks how many attempts the user makes for each answer. If the user enters the correct translation, the program records the result and shows how many tries were needed. If the user doesn’t know the answer, they can skip the word to reveal the correct translation before moving on. The skipped word will appear again later. At any time, the user can end the session and see a summary of their overall performance.

--- 

**User stories:**

1. As a user, I want to practise my English-German vocabulary in the console. 
2. As a user, I want to track my learning progress.
3. As a user, I want to see the correct answer, in case I can not answer it myself.

**Use cases:**

- Provide or use a vocabulary list with word pairs (flashcard_words.csv)
- Practise vocabulary (flashcard_app_with_csv_db.py)
- Skip unknown words and learn them later again
- Track progress (user_progress.txt)


---

## Project Requirements
1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---
### 1. Interactive App (Console Input)
The application interacts with the user via the console. Users can:

- Choose the language you want to be quizzed in 
- Enter translation
- Skip unknown words
- Exit the program

---

### 2. Data Validation
The application validates all user input to ensure data integrity and a smooth user experience. The program validates the following points:
- If a valid language was chosen at the beginning
	```python
	language = ""
	while language not in ("english", "german"):
	    language = input("Choose the quiz language: German or English:\n ").strip().lower()
	```
	This ensures only valid language is chosen. 

- If the words from the CSV file were loaded. The program validates the vocabulary file and checks its readability.
	```python 
		def load_flashcards():
	    	"""This function loads the flashcards data from the CSV file."""
	    	try:
	        	with open("flashcard_words.csv", encoding="utf-8", mode="r") as f:
	            	reader = csv.DictReader(f)
	            	flashcards = list(reader)
	    	except FileNotFoundError:
	        	print(f"⚠️  File 'flashcard_words.csv' not found.")
	        	return False
	    	return flashcards
	```
	```python
	def main():
    	flashcards = load_flashcards() # Load cards
    	if not flashcards:  # Checks if file was loaded
        	print('Exiting')
        	return
	```
	This ensures the program only operates when a valid data file was loaded. 

- If digits or letters were inserted by the user. The program validates user responses. 
	```python 
 	elif not user_answer.isalpha(): # The user's answer was invalid
		print('Invalid Input, only words are accepted')
    	user_answer = input(
    		'Please try again, or type "n" for the next question, or "x" to end the quiz.\n')
	```
	
	This ensures that the input contains only valid characters and prevents invalid inputs from being counted or stored in the results file (user_progress.txt). 
 

---
### 3. File Processing
The program reads and writes data using files:
- **Input file:** `flashcard_words.csv` - Contains the table of words and its translations per line in the format `English,German,type`.
    - Example:
		```
        house,Haus,noun
        difficult,schwierig,adjective
        zero,null,numeral
        ```
    - The program reads this file at the beginning to display words in a random order.

- **Output file:** `user_progress.txt` It writes the words that the user entered correctly in an additional txt file. It contains a summary of the progressed words. 
    - Example:
		```
  		Practice session started at Thu 04 Dec 2025, 07:17PM (German -> English)
		- Information -> information
		- Bluse -> blouse
		- eins -> one
		- hassen -> hate
		- Kamera -> camera
		- Regel -> rule
		- Messer -> knife
		Your performance: 70% correct answers with an accuracy rate of 54%. 
        ```
    - The output file serves as a record for the user to keep track of the progress.

## Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces, PyCharm and Visual Studio Code
- Libraries: random and csv

 ### Repository Structure
 ```text
Flashcard-quiz-system/

├── flashcard_app_with_csv_db.py    # Main program logic (console application)
├── flashcard_words.csv             # Table with all the words in english and german
├── user_progress.txt               # Words that the user progressed
└── README.md                       # Project description and milestones
```


 ### How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash

    python3 flashcard_app_with_csv_db.py

    ```

 ### Libraries Used

 - 'random': Module is used to select random words from the csv file, and shuffle the order of flashcards presented to the user. 
 - 'csv': Allows to read data, word pairs (english-german) in ´flashcard_words.csv´ file.
 - 'from datetime import datetime': Allows the program to display the current date and time—perfect for tracking when each practice session begins.

In this program, only Python standard libraries were used, with no external installations required. These libraries were chosen because of their simplicity, effectiveness, and reliability, while managing files and data processing in a console application. 

 ## Team and Contributions
 All team members collaborated on planning, testing, debugging, and the final presentation to ensure a consistent result.
 
 Group 2: Evgenia Boesiger, Noor Vinnai, Pascal Walther.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
