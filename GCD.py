def gcd(n1,n2):
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


if __name__ == '__main__':
     num1 = int(input("enter the numbers:"))
     num2 = int(input("enter the numbers:"))
     print (f"thr gcd of {num1} and {num2} is {gcd(num1,num2)}")
