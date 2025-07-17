from equation_generator import generate_equation
from user_interaction import get_user_guess, display_message, display_equation, display_score
from quiz_logic import answer_check

def run_quiz(num_questions=10):
    """
    Runs the quiz in the terminal.
    
    Generates the number of questions, checks the answers,
    keeps track of score, and displays the final score.

    Parameters:
        num_questions (int): The total number of questions in the quiz
    """
    score = 0
    display_message("Welcome to the quiz!")

    for i in range(1, num_questions + 1):
        equation, answer = generate_equation()
        display_equation(equation)
        user_response = get_user_guess()

        if answer_check(user_response, answer):
            display_message("Correct. + 1 point")
            score += 1
        else:
            display_message(f"Incorrect. The answer was {answer}.")
    
    display_score(score, num_questions)

run_quiz()
