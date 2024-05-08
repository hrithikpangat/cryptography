from primeornot import is_prime
from prime_factors import primeFactors

def eulerTotient(num):
    numIsPrime = is_prime(num)
    primes = primeFactors(num)
    ans = 1
    if (numIsPrime == 1):
        return (num - 1)
    else:
        for x in primes.keys():
            ans *= (1 - 1/x)
        return int(num * ans)

if __name__ == '__main__':
    number = int(input("Enter a number:- "))
    print(f"Euler's Totient of {number} is {eulerTotient(number)}.")