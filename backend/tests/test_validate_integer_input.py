from functions import validate_integer_input


def test_integer_as_string():
    valid, error_message = validate_integer_input("5", "age")
    assert valid


def test_string_instead_of_int():
    valid, error_message = validate_integer_input("jorrit", "age")
    assert not valid
    assert "age" in error_message
