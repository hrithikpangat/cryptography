from modular import modular_inverse
import random

def fermatsPrimalityTest(num, numOfIerations):
    prime = 1
    if (num == 1):
        prime = 0
        return prime
    elif (num == 2 or num == 3):
        return prime
    else:
        for i in range(numOfIerations):
            a = random.randint(2, num - 1)
            aPowered = pow(a, (num - 1))
            modularMultInv = modular_inverse(aPowered, num)
            if (modularMultInv != 1):
                prime = 0
                break
    return prime

if __name__ == '__main__':
    n = int(input("Enter a number:- "))
    numOfIerations = int(input("Enter how many times to repeat Fermat's Primality Test:- "))
    primalityCheck = fermatsPrimalityTest(n, numOfIerations)
    if (primalityCheck == 1):
        print(f"{n} is likely to prime.")
    else:
        print(f"{n} is not prime.")