# This file contains some general functions used by the backend script.

def validate_integer_input(potential_integer, origin):
    """This functions validates if input can be converted to an integer."""
    error_message = (
        f"Couldn't convert the `{origin}` input to an integer. "
        "Please insert a valid number"
    )
    try:
        _ = int(potential_integer)
        valid = True
    except ValueError:
        valid = False

    return valid, error_message


def get_greeting(age: int):
    """This functions determines a proper greeting for the user, given his/her age."""
    greeting = ""
    if age < 5:
        greeting = "TA-DA"
    elif 5 <= age < 12:
        greeting = "Hoi"
    elif 12 <= age < 18:
        greeting = "Yo"
    elif 18 <= age < 30:
        greeting = "Hallo"
    elif age > 30:
        greeting = "Goedendag"
    return greeting


def get_farewell(age: int):
    """This functions determines a proper farewell for the user, given his/her age."""
    farewell = ""
    if age < 5:
        farewell = "TA-DA"
    elif 5 <= age < 18:
        farewell = "Doei"
    elif 18 <= age < 30:
        farewell = "De ballen"
    elif age > 30:
        farewell = "Tot ziens"
    return farewell


if __name__ == "__main__":
    print(validate_integer_input("5", "age"))
    print(validate_integer_input("jorrit", "age"))
    print(get_greeting(5))
