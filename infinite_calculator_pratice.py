def calcultor(numbers,operators):

    if operators[0] == "+":
        sum = numbers[0] + numbers[1]
    elif operators[0] == "-":
        sum = numbers[0] - numbers[1]
    elif operators[0] == "*":
        sum = numbers[0] * numbers[1]
    elif operators[0] == "/":
        try:
            sum = numbers[0] / numbers[1]
        except ZeroDivisionError:
            print("invaild input you not have any mathmathical knowledge !!!")
            return None 
    elif operators[0] == "%":
        sum = numbers[0] % numbers[1]

    total = sum 

    i = 
    for j in range(2, len(numbers)):

        if 