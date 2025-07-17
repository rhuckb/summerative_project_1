
import pytest
from user_interaction import get_display_message, get_display_equation, get_display_score_message

# Test for get_display_message
def test_get_display_message_works():
    message = "Hello World"
    expected_result = "Hello World"
    actual_result = get_display_message(message)
    assert actual_result == expected_result

# Test for get_display_equation
def test_get_display_equation_works():
    equation = "5 * x = 25"
    expected_result = "5 * x = 25"
    actual_result = get_display_equation(equation)
    assert actual_result == expected_result

# Test for get_display_score_message
def test_get_display_score_message_all_correct():
    score = 10
    num_questions = 10
    expected_result = "Congratulations! Your total score: 10 out of 10."
    actual_result = get_display_score_message(score, num_questions)
    assert actual_result == expected_result

def test_get_display_score_message_some_correct():
    score = 7
    num_questions = 10
    expected_result = "Your total score: 7 out of 10."
    actual_result = get_display_score_message(score, num_questions)
    assert actual_result == expected_result