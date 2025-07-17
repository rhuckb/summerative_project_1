def get_user_guess():
    """
    Asks the user to find the answer to the equation and validates the input.
    
    Keeps asking for a valid input if they enter incorrectly.
    
    Returns:
    int: The answer the user inputs
    """
    while True:
        try:
            user_input = input("The answer is: ")
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print("This is not a valid answer. Please enter an integer.")

def display_message(message):
    """Displays a message to the user."""
    print(message)

def display_equation(equation):
    """Displays the equation to the user."""
    print(equation)

def display_score(score, num_questions):
    """Displays the final score to the user."""
    if score == num_questions:
        # If score is 10 / 10, congrats the user.
        display_message(f"Congratulations! Your total score: {score} out of {num_questions}.")
    else:
        display_message(f"Your total score: {score} out of {num_questions}.")