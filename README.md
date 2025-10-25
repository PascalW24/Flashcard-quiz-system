# Flashcard-quiz-system
This project is intended to:

- Develop an interactive console application that helps users learn and test English–German vocabulary 
- Apply basic Python programming concepts learned in the Programming Foundations module
- Demonstrate the use of console interaction, data validation, and file processing
- Produce clean, well-structured, and documented code

---
**Problem**

  Around 15.4 million people learn German as a foreign language worldwide. Many people struggle with memorizing vocabulary, which leads to slower learning progress, mental frustration and poor progress overview.  


---
**Scenario**

 The user opens the program. The program loads word pairs from a file, presents them in random
order, and asks the user to translate each word. The program count’s the amount of tries used and displays it when you entered the right word. If the user doesn’t know an
answer, he has the option to show the answer and skip it.

--- 

**User stories:**

1. As a user, I want to practise my english - german vocabulary in the console. 
2. As a user, I want to track my learning progress.
3. As a user, I want to see the correct answer, in case i can not answer it myself.

**Use cases:**

-
-
-
-

---

## Project Requirements
1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---
### 1. Interactive App (Console Input)
The application interacts with the user via the console. Users can:

- Choose the language 
- Enter translation
- Skip unknown words
- Exit the program

---

### 2. Data Validation
The program validates the following points:
- If a valid language was chosen at the beginning
- If he was able to load the words from the csv file
- If a digit or letters were inserted by the user

---
### 3. File Processing
The program reads and writes data using files:
- It reads the words from a csv file
- It writes the words that the user guessed right in a additional txt file
## Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces and PyCharm
- Libraries: random and csv

 ### Repository Structure
Flashcard-quiz-system/

├── flashcard_app_with_csv_db.py    # main program logic (console application)
├── flashcard_words.csv             # Table with all the words in english and german
├── user_progress.txt               # words that the user progressed
└── README.md                       # project description and milestones

 ### How to Run

 ### Libraries Used

 ## Team and Contributions
 | Name       | Contribution                                 |
|------------|----------------------------------------------|
| Evgenia Boesiger | ...|
| Noor Vinnai | ...              |
| Pascal Walther | ...  |

##  Contributing

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
