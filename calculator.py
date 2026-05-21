"""Basic calculator module for performing arithmetic operations."""

from typing import Union

SUPPORTED_OPERATORS = ('+', '-', '*', '/')


def calculate(a: float, b: float, operator: str) -> Union[float, None]:
    """Perform arithmetic operation on two numbers.

    Args:
        a: The first operand.
        b: The second operand.
        operator: One of +, -, *, /.

    Returns:
        The result as a float, or None on error.

    Raises:
        ValueError: If the operator is not supported.
        ZeroDivisionError: If dividing by zero.
    """
    if operator not in SUPPORTED_OPERATORS:
        raise ValueError(f"Unsupported operator '{operator}'. Use one of: {', '.join(SUPPORTED_OPERATORS)}")

    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b


def get_float_input(prompt: str) -> float:
    """Prompt the user for a float value, retrying on invalid input.

    Args:
        prompt: The message to display to the user.

    Returns:
        A valid float entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operator_input() -> str:
    """Prompt the user for a valid arithmetic operator.

    Returns:
        A valid operator character.
    """
    while True:
        operator = input(f"Enter operator ({', '.join(SUPPORTED_OPERATORS)}): ").strip()
        if operator in SUPPORTED_OPERATORS:
            return operator
        print(f"Invalid operator. Choose from: {', '.join(SUPPORTED_OPERATORS)}")


def format_result(a: float, b: float, operator: str, result: float) -> str:
    """Format the calculation result as a readable string.

    Args:
        a: The first operand.
        b: The second operand.
        operator: The operator used.
        result: The computed result.

    Returns:
        A formatted result string.
    """
    a_fmt = int(a) if a == int(a) else a
    b_fmt = int(b) if b == int(b) else b
    result_fmt = int(result) if result == int(result) else result
    return f"{a_fmt} {operator} {b_fmt} = {result_fmt}"


def main() -> None:
    """Entry point for the calculator application."""
    print("=" * 30)
    print("       Basic Calculator")
    print("=" * 30)

    a = get_float_input("Enter first number : ")
    b = get_float_input("Enter second number: ")
    operator = get_operator_input()

    try:
        result = calculate(a, b, operator)
        print(format_result(a, b, operator, result))
    except ZeroDivisionError as exc:
        print(f"Math error: {exc}")
    except ValueError as exc:
        print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
