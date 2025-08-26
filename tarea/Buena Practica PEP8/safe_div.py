def safe_divide(a, b):
    """
    Divide two numbers.

    Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or str: The result of the division, or an error message.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))