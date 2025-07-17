def get_user_guess(input_function=input):
    """
    Asks the user to find the answer to the equation and validates the input.
    
    Keeps asking for a valid input if they entered incorrectly.
    
    Parameters:
    input_function (callable): A function to use for getting user input.

    Returns:
    int: The answer the user inputs
    """
    while True:
        user_input = input_function("The answer is: ")
        try:
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print("This is not a valid answer. Please enter an integer.")

def get_display_message(message):
    """Returns a message to the user."""
    return(message)

def get_display_equation(equation):
    """Returns the equation to the user."""
    return(equation)

def get_display_score_message(score, num_questions):
    """Returns the final score to the user."""
    if score == num_questions:
        # If score is 10 / 10, congrats the user.
        return f"Congratulations! Your total score: {score} out of {num_questions}."
    else:
        return f"Your total score: {score} out of {num_questions}."