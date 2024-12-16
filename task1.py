from __future__ import annotations

"""
Programming Task #1
Given a list of digits, determine the integer that it represents.

For example, given the list: [8,3,5,1], your program should output 8351 as an integer.

Author: Albert Liesman (32436793)
"""

def list_to_integer(list_of_digits: list[int]) -> int:
    """
    This function takes a list of digits (like [8, 3, 5, 1]) and turns it into a single number 
    (like 8351) using math only without conversion / casting.
    
    :param list_of_digits: A list of digits (0-9) in the order they should be in the final number.
    :return: The integer that the list of digits represents.
    """
    # Initialize the result variable to store the final number.
    result = 0  
    
    # Go through each digit in the list, one by one until the end.
    for number in list_of_digits:
        # Imagine the result is a number, and we are shifting it to the left.
        # Multiplying by 10 to make room for the next digit.
        result = (result * 10) + number
        
        # Here's what's happening step by step:
        # - result * 10 shifts the current number left (like writing a new column).
        # - Adding 'digit' puts the next number in the last position.
        # Example: give a List [8, 3, 5, 1], the first iteration will be
        # result = 0 * 10 + 8 = 8, next iteration will be result = 8 * 10 + 3 = 83, then
        # result = 83 * 10 + 5 = 835, and finally result = 835 * 10 + 1 = 8351.
        # This way, we build the final number digit by digit.
        
    return result  # When we finish, result has the final number.

# Example usage:
list_of_digits = [8, 3, 5, 1]  # A list of digits 
print(list_to_integer(list_of_digits))  # It prints: 8351
