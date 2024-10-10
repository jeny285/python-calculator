def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    valid_operators = {'+': 'Add', '-': 'Subtract', '*': 'Multiply', '/': 'Divide'}
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        print("Invalid operator. Please try again.")

def calculate(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            raise ValueError("Cannot divide by zero")
        return first_number / second_number

def main():
    print("Calculator Program")
    
    # Enter first number
    first_number = get_valid_number("Enter first number: ")
    
    # Operator selection
    operator = get_operator()
    
    # Enter second number
    second_number = get_valid_number("Enter second number: ")
    
    try:
        # Calculate result
        result = calculate(first_number, operator, second_number)
        
        # Display result
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
