from equation_generator import generate_equation
from user_interaction import get_user_guess, get_display_message, get_display_equation, get_display_score_message
from quiz_logic import answer_check

def run_quiz(num_questions = 10):
    """
    Runs the quiz in the terminal.
    
    Generates the number of questions, checks the answers,
    keeps track of score, and displays the final score.

    Parameters:
        num_questions (int): The total number of questions in the quiz
    """
    score = 0
    print(get_display_message("Welcome to the quiz!"))

    for i in range(1, num_questions + 1):
        equation, answer = generate_equation()
        print(get_display_equation(equation))
        user_response = get_user_guess()

        if answer_check(user_response, answer):
            print(get_display_message("Correct. + 1 point"))
            score += 1
        else:
            print(get_display_message(f"Incorrect. The answer was {answer}."))
    
    print(get_display_score_message(score, num_questions))

run_quiz()
