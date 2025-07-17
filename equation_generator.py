import random
def generate_equation():
    """
    Generate a random multiplication equation with an unknown 'x'. 
    
    The equation is in the format: number1 * x = answer
    This function calculates 'x' and returns the equation with the correct answer.

    Returns:
    tuple: A tuple containing:
          str: The equation string.
          int: The correct answer for 'x'.
    """
    # Generate the two random numbers.
    number1 = random.randint(2,10)
    number2 = random.randint(2,10)

    # Calculate the answer of the two random numbers (answer).

    answer = number1 * number2

    # Assign the value of x to true_answer for clarity.

    true_answer = number2

    # Create the equation.

    equation1 = f"{number1} * x = {answer}"

    return equation1, true_answer