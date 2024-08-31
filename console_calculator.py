l = []
op = []

# This function calculates the total 
def total(op, l):
    if len(l) < 2:
        print("Not enough numbers to perform operations.")
        return None
    
    # Initialize result with the first operation
    result = l[0]
    
    for i in range(len(op)):
        if i+1 >= len(l):  # Ensure there's a corresponding number for each operation
            break
        
        if op[i] == '+':
            result += l[i+1]
        elif op[i] == '-':
            result -= l[i+1]
        elif op[i] == '*':
            result *= l[i+1]
        elif op[i] == '/':
            if l[i+1] == 0:
                print("Error: Division by zero.")
                return None
            result /= l[i+1]
        elif op[i] == '%':
            if l[i+1] == 0:
                print("Error: Modulus by zero.")
                return None
            result %= l[i+1]
    
    return result

print('Welcome to our calculator')
type_op = ["+", "-", "*", "/", "%"]

# This loop stores the numbers and operators
while True:
    try:
        number = float(input("Enter a number: "))
        l.append(number)
    except ValueError:
        print("Invalid input number!!!")
        continue
    
    while True:
        operator = input('Enter an operator or [=] to calculate: ')

        if operator in type_op:
            op.append(operator)
            break
        elif operator == "=":
            break
        else:
            print('Invalid operator input!!')
    
    if operator == "=":
        break

if len(l) > 0:
    print("Numbers:", l)
    print("Operators:", op)
    result = total(op, l)
    if result is not None:
        print("Result:", result)
else:
    print("No valid calculation to perform.")