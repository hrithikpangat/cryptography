def findGCD(n1, n2):
    if (n1 == 0):
        return n2
    elif (n2 == 0):
        return n1
    else:
        dividend = n1
        divisor = n2
        while (True):
            remainder = dividend % divisor
            if (remainder == 0):
                return divisor
            else:
                dividend = divisor
                divisor = remainder

number1 = int(input("Enter first number:- "))
number2 = int(input("Enter second number:- "))

gcd = findGCD(number1, number2)
product = number1 * number2

def findLCM(gcd, prod):
    lcm = int(product / gcd)
    return lcm

print(f"LCM of {number1} and {number2} is {findLCM(gcd,product)}.")