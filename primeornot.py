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

if __name__ == '__main__':
    number = int(input("Enter a number:- "))
    prime = isPrime(number)
    if (prime == -1):
        print("The number is neither prime nor composite.")
    elif (prime == 1):
        print("The number is prime.")
    else:
        print("The number is not prime.")