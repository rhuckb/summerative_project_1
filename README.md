# **Multiplication Quiz Program**

## User Manual

### What is this program?

The multiplication quiz is a simple game to help you practice your multiplication skills. It runs directly into the user’s terminal for ease of use. When the program is run it creates a series of 10 multiplication equations with one of the beginning numbers replaced with ‘x’. The goal is to figure out what ‘x’ is to complete the equation.

### How to play

Once the program is run, the user is presented with an equation such as the following:

2 \* x = 10

The user must then figure out what the value of x is to make the equation true. In this example the value of x would be 5.

The user must then input their chosen value (e.g. 5) and the program will then determine if the user is correct or incorrect, adding a point onto the score board if they are.

### Getting Started

To run this program, you will first need to install Python on your computer.

1. Save the program. This can be done by copy and pasting the codes for the .py files directly into your Python application. Then simply saving them all in the same folder.
2. Open the folder in your Python application ensuring all the correct files are in the folder.
3. Run the program.

### Gameplay

1. The quiz will greet you with "Welcome to the quiz!".
2. For each question, an equation will be displayed.
3. A message "The answer is: " will appear. Type your answer and press Enter.
4. If you type something that isn't an integer, the program will tell you "This is not a valid answer. Please enter an integer." and ask you to try again until you enter a valid number.
5. After each answer, you'll be told if you were "Correct. + 1 point" or "Incorrect. The answer was \[correct answer\]."
6. After 10 questions, the quiz will finish, and it will show you your score.

### Technical Documentation

The program consists of 4 python files that contain several functions that work together to create the quiz.

It is modularized into 4 sections:

1. main.py – This is the main call to start the quiz.
2. equation_generator – This is where the quiz questions are created.
3. quiz_logic – This is where the users answer is checked to see if it is correct.
4. user_interaction – This is what talks directly to the user such as displaying messages and calling for inputs from the user.

### Functions Overview

The programmes functionality is distributed amongst these files through 7 functions:

- generate_equation() : This creates a random multiplication question.
- get_user_guess() : Gets the users answer and ensures it is a valid integer.
- display_message(message) : Displays messages to the user.
- display_equation(equation) : Displays the equation to the user.
- display_score(score, num_questions) : Displays the final score.
- answer_check(user_answer, correct_answer) : Checks the users answer against the correct answer.
- run_quiz(num_questions=10) : Starts the program calling all the functions and sets the amount of questions.

### Dependencies

The program relies on only Pythons built in ‘random’ module (used in equation_generator.py). No external libraries need to be installed.

### Code Explanation

**equation_generator.py**

**1. generate_equation()**

*Purpose:* To create a multiplication equation with a missing 'x' and determine its correct answer.

*Logic:*

- number1 and number2 are randomly generated integers between 2 and 10.
- answer is calculated as the product of number1 and number2.
- true_answer is assigned the value of number2, as this is the unknown 'x' in the equation.
- An f-string is used to construct the equation1 string.

*Returns:* A tuple containing the equation string and the true_answer.

**user_interaction.py**

**1. get_user_guess()**

*Purpose:* To prompt the user for their answer and validate that the input is an integer.

*Logic:*

- Uses a while True loop to continuously prompt the user until a valid input is received.
- A try-except ValueError block attempts to convert the user's string input to an integer.
- If ValueError occurs (input is not an integer), an error message is printed, and the loop continues.
- If successful, the integer input is returned, breaking the loop.

*Returns:* The user's answer as a valid integer.


**2. display_message(message)**

*Purpose:* Displays a message string to the console.

*Parameters:* message (str): The text to be displayed.

*Returns:* None.


**3. display_equation(equation)**

*Purpose:* Displays the equation string to the console.

*Parameters:* equation (str): The equation string to be displayed.

*Returns:* None


**4. display_score(score, num_questions)**

*Purpose:* Displays the final quiz score to the user.

*Parameters:*

- score: The number of correct answers as an integer.
- num_questions: The total number of questions as an integer.

*Logic:* Checks to see if score = num_scor =e and displays congratulations, if not then it just returns the score.

*Returns:* None.

**quiz_logic.py**

**1. answer_check(user_answer, correct_answer)**

*Purpose:* To compare the user's answer against the correct answer.

*Parameters:*

- user_answer: The integer provided by the user.
- correct_answer: The actual correct integer answer.

*Logic:* Uses an equality operator to compare the answers (==).

*Returns:* A boolean; True if user_answer matches correct_answer, False otherwise.

**main.py**

**1. run_quiz(num_questions=10)**

*Purpose:* The main function that controls the quiz, from generating questions to displaying the final score. It imports and utilizes functions from the other modules.

*Parameters:* num_questions (int, default 10): Specifies the total number of questions in the quiz.

*Logic:*

- Starts the score at 0.
- Uses display_message() to print a welcome message.
- Iterates num_questions times using a for loop.
- In each iteration:

                   1. Calls generate_equation() (from equation_generator.py) to get a new equation.
                   2. Calls display_equation() (from user_interaction.py) to print the equation.
                   3. Calls get_user_guess() (from user_interaction.py) to get and validate the user's response.
                   4. Calls answer_check() (from quiz_logic.py) to verify the user_response.
                   5. Provides feedback using display_message() and updates the score.
                   6. After the loop, it calls display_score() (from user_interaction.py) to present the final results.

*Returns:* None
