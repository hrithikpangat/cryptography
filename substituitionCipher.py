def findSumOfDigits(num):
    sumOfDigits = 0
    while (num >= 1):
        digit = num % 10
        sumOfDigits += digit
        num //= 10
    if (sumOfDigits > 9):
        return findSumOfDigits(sumOfDigits)
    return sumOfDigits

def substitutionCipher(string, key):
    encryptedString = ""
    for i in (string):
        asciiValue = ord(i)
        shiftedAsciiValue = asciiValue + key
        if (shiftedAsciiValue > 90 and asciiValue <= 90):
            shiftedAsciiValue = ((shiftedAsciiValue - 65) % 26) + 65
            encryptedString += chr(shiftedAsciiValue)
        elif (shiftedAsciiValue > 122):
            shiftedAsciiValue = ((shiftedAsciiValue - 97) % 26) + 97
            encryptedString += chr(shiftedAsciiValue)
        else:
            encryptedString += chr(shiftedAsciiValue)
    return encryptedString

if __name__ == '__main__':
    fullName = input("Enter your name:- ")
    rollNumber = int(input("Enter your roll number:- "))
    encKey = findSumOfDigits(rollNumber)
    encValue = substitutionCipher(fullName, encKey)
    print(f"The encrypted form of string {fullName} is {encValue}.")