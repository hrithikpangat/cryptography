import random
from prime_factors import primeFactors
from GCD import gcd
from primeornot import isPrime


def keyGeneration(P):
    eulerstotient = P-1
    factors = list((primeFactors(eulerstotient)))
    for j in range (2,P):
        for i in factors:
            calcuate1 = eulerstotient // i
            calcuate2 = pow(j,calcuate1)
            G = calcuate2 % P 
            if G == 1:
                break
            else:
                return j


def encryption():
    encryption1 = pow(Generator,key,P)
    encryption2 = message * pow(calculate_E,key,P) % P
    return encryption1, encryption2

            

if __name__ == '__main__':
    P = int(input("Enter the prime number:"))
    Generator = keyGeneration(P)
    checkprime = isPrime(P)
    if checkprime == 1: 
        print(f"Generator ----> {Generator}")

        findGCD = gcd(Generator,P)
    if findGCD == 1:
        privatekey1 = random.randint(2,P-2)
        print(privatekey1)
        calculate_E = pow(Generator,privatekey1,P)
        key = random.randint(2,100)
        print(key)
        

        message = int(input("Enter your message:"))
        if message < P :
            result = encryption()
            print(f"the cipher text is {result}")
