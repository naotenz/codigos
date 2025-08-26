def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two input values.
    """
    result = a + b
    return result


if __name__ == "__main__":
    number = add_numbers(25, 15)
    print("El resultado es:", number)

    # The function add_numbers is already defined above, so no need to redefine it here.