def isPrime(num):
    halfOfNum = num // 2
    if (num == 1):
        return -1
    elif (halfOfNum < 2):
        return 1
    elif (halfOfNum >= 2):
        for i in range (2, halfOfNum + 1):
            if (num % i == 0):
                return 0
    return 1

number = int(input("Enter a number:- "))
hasFactors = isPrime(number)

if (hasFactors == -1):
    print("The number 1 has no prime factors.")
elif (hasFactors == 1):
    print(f"The prime factors of {number} is 1 and {number}.")
else:
    num = number
    halfOfNum = number // 2
    primeFactors = {}
    while(num > 1):
        for i in range (2, halfOfNum + 1):
            if (num % i == 0):
                if i in primeFactors:
                    primeFactors[i] += 1
                    break
                else:
                    primeFactors[i] = 1
                    break
        num //= i
    print(f"The count of prime factors of {number} is {primeFactors}.")
