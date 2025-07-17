def answer_check(user_answer, correct_answer):
    """
    Checks the users answer against the correct answer.

    Parameters:
               user_answer (int): The answer provided by the user.
               correct_answer (int): The actual answer.

    Returns:
            bool: True if answer is correct, False if not.           
    """
    return user_answer == correct_answer