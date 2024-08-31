#Console_Calculator

### 1. **Initialization**
```python
l = []
op = []
```
- **`l`**: This list is used to store the numbers that the user inputs.
- **`op`**: This list is used to store the operators (`+`, `-`, `*`, `/`, `%`) that the user inputs.

### 2. **Total Function**
```python
def total(op, l):
    if len(l) < 2:
        print("Not enough numbers to perform operations.")
        return None
```
- **`total(op, l)`**: This function calculates the total result based on the numbers (`l`) and the operators (`op`) provided.
- It first checks if there are at least two numbers in the list `l` because you need at least two numbers to perform any operation. If not, it prints a message and returns `None`.

### 3. **Performing Operations**
```python
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
```
- **`result = l[0]`**: The `result` variable is initialized with the first number in the list `l`.
- **Loop through the operators**: The code loops through each operator in `op`.
  - It checks if there is a corresponding number in the list `l` for each operator. If not, it breaks the loop.
  - **Operations**: Depending on the operator, it performs the corresponding operation (`+`, `-`, `*`, `/`, `%`) between `result` and the next number in `l`.
  - **Error Handling**: The code checks for division or modulus by zero to prevent errors.

### 4. **Main Program Execution**
```python
print('Welcome to our calculator')
type_op = ["+", "-", "*", "/", "%"]
```
- **Welcome Message**: A greeting message for the user.
- **`type_op`**: A list of valid operators that the calculator can handle.

### 5. **User Input Loop**
```python
while True:
    try:
        number = float(input("Enter a number: "))
        l.append(number)
    except ValueError:
        print("Invalid input number!!!")
        continue
```
- **User enters numbers**: The code repeatedly asks the user to input numbers and stores them in the list `l`.
- **Error Handling**: If the user enters something that's not a valid number, it catches the error and asks for input again.

### 6. **Operator Input**
```python
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
```
- **User enters operators**: The code asks the user to input an operator. 
  - If the input is a valid operator, it is stored in `op`.
  - If the user enters `=`, it breaks out of the loop to start the calculation.
  - If the input is invalid, it asks for input again.

### 7. **Calculation and Result**
```python
if len(l) > 0:
    print("Numbers:", l)
    print("Operators:", op)
    result = total(op, l)
    if result is not None:
        print("Result:", result)
else:
    print("No valid calculation to perform.")
```
- **Perform Calculation**: If there are numbers in `l`, it displays them along with the operators, calls the `total()` function to calculate the result, and prints it.
- **Handle Empty Input**: If no numbers were entered, it prints a message indicating there's no valid calculation to perform.

### Summary
This code is a simple calculator that takes a series of numbers and operators as input, stores them in lists, and then performs the specified operations sequentially. It handles errors like invalid inputs and division/modulus by zero. The result of the calculation is printed at the end.
