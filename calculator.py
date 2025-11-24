
# Anuja's calculator
# Simple calculator


ADD_KEY = '+'      
SUB_KEY = '-'      
MUL_KEY = '*'      
DIV_KEY = '/'     
POW_KEY = '^'      



def parse_number(text: str):
    """
    Try to convert text to int or float.
    Raises ValueError if not a valid number.
    """
    text = text.strip()
    


    if text.count('.') == 0 and text.isdigit() or (text.startswith('-') and text[1:].isdigit()):
        return int(text)
    return float(text)

def calculate(a, b, op: str):
    """Perform the operation op on numbers a and b. Raises ValueError for invalid op."""
    if op == ADD_KEY:
        return a + b
    if op == SUB_KEY:
        return a - b
    if op == MUL_KEY:
        return a * b
    if op == DIV_KEY:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    if op == POW_KEY:
        return a ** b
    raise ValueError(f"Unsupported operation: {op!r}")

def show_menu():
    """Print the operation menu using current keys."""
    print("Choose an operation (type the symbol):")
    print(f"  {ADD_KEY}  -> Addition")
    print(f"  {SUB_KEY}  -> Subtraction")
    print(f"  {MUL_KEY}  -> Multiplication")
    print(f"  {DIV_KEY}  -> Division")
    print(f"  {POW_KEY}  -> Power (a raised to b)")

def main():
    print("Simple Calculator")
    print("-----------------")
    # Input first number
    try:
        x_text = input("Enter first number: ")
        a = parse_number(x_text)
    except ValueError:
        print("Invalid input for the first number. Please enter a numeric value (e.g., 3, -2, 4.5).")
        return

    # Input second number
    try:
        y_text = input("Enter second number: ")
        b = parse_number(y_text)
    except ValueError:
        print("Invalid input for the second number. Please enter a numeric value (e.g., 3, -2, 4.5).")
        return

    # Show menu and read operation
    show_menu()
    op = input("Operation: ").strip()

    # Calculate and display result, with error handling
    try:
        result = calculate(a, b, op)
    except ZeroDivisionError as zde:
        print("Error:", zde)
        return
    except ValueError as ve:
        print("Error:", ve)
        return

    
    
    if isinstance(result, float) and result.is_integer():
        


        result = int(result)

    print(f"\nResult: {a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
