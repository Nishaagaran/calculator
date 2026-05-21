def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"

def main():
    print("Basic Calculator")
    print("Operators: +  -  *  /")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers")
        return

    op = input("Enter operator (+, -, *, /): ").strip()
    result = calculate(a, b, op)

    if isinstance(result, str):
        print(result)
    else:
        print(f"{a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
