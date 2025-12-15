number = int(input("Enter your number"))
digits = len(str(number))
resultnumber = 0
temp = number
while temp > 0:
    digit = temp %10
    resultnumber += digit ** digits
    temp //= 10
if number == resultnumber:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")

def print_factors(number):
    print("The factors of ", number, "are :")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input("Enter your number to find its factors"))
print_factors(number)

def romanToInt(romanInput):
    roman = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    resultinteger = 0
    for i in range(1, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultinteger -= roman[romanInput[i]]
        else:
            resultinteger += roman[romanInput[i]]
    return resultinteger + roman[romanInput[-1]]
roman = input("Input roman numeral")
print("Integer equivalent:", romanToInt(roman))