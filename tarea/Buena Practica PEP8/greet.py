def greet(name):
    """
    Saluda al usuario con un mensaje personalizado

    Args:
        name (str): Nombre del usuario a saludar

    Returns:
        str: Mensaje de saludo
    """
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)