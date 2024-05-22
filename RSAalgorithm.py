from GCD import gcd
from primeornot import isPrime
import random
import os

def calculateN(num, subValue=0):
    nToBinary = bin(num)
    length = len(nToBinary) - 2 - subValue
    return length

def charToBinary(text):
    textList = []
    binaryString = ''
    textList = list(text)
    for char in textList:
        charToBinary = bin(ord(char))
        charToBinaryFormatted = charToBinary[2:]
        charToBinaryFormatted = charToBinaryFormatted.zfill(8)
        binaryString += ''.join(charToBinaryFormatted)
    return binaryString

def intToBinary(intBlock, size):
    binaryText = ""
    for value in intBlock:
        binary = bin(value)
        binaryFormatted = binary[2:]
        binaryFormatted = binaryFormatted.zfill(size)
        binaryText += ''.join(binaryFormatted)
    return binaryText

def prepareBlock(binaryString, size):
    blockList = []
    for start in range(0, len(binaryString), size):
        end = start + size
        block = binaryString[start:end]
        if (len(block) < size):
            block = block.zfill(size)
        blockList.append(block)
    return blockList

def blocksToInt(blockList): 
    blockToInt = []
    for value in blockList:
        valueToInt = int(value, 2)
        blockToInt.append(valueToInt)
    return blockToInt

def binaryToString(binaryString, size):
    finalString = ''
    binaryStringList = [binaryString[i:i+size] for i in range(0, len(binaryString), size)]
    for binaryValue in binaryStringList:
        asciiValue = int(binaryValue, 2)
        charValue = chr(asciiValue)
        finalString += "".join(charValue)
    return finalString

def calculate_e(num):
    array = []
    e = 2
    for _ in range (1, num):
        if (gcd(e, num) == 1):
            array.append(e)
        e += 1
    e = random.choice(array)
    return e

def encrypt():
    cipherText = ""
    p = int(input("Enter a prime number p (secret key):- "))
    isNumPrime = isPrime(p)
    if (isNumPrime == 1):
        q = int(input("Enter another prime number q (secret key):- "))
        isNumPrime = isPrime(q)
        if (isNumPrime == 1):
            n = p * q
            nLength = calculateN(n)
            eulersTotient = (p - 1) * (q - 1)
            e = calculate_e(eulersTotient)
            print(f"The public key is ({e}, {n}). The private keys p and q are {p} and {q}.")
            message = input("Enter the message to be encrypted:- ")
            messageToBinary = charToBinary(message)
            binaryMessageBlock = prepareBlock(messageToBinary, nLength - 1)
            binarymesageBlockToInt = blocksToInt(binaryMessageBlock)
            for value in binarymesageBlockToInt:
                cipherValue = pow(value, e, n)
                cipherValueToBinary = bin(cipherValue)
                cipherValueToBinaryFormatted = cipherValueToBinary[2:]
                cipherValueToBinaryFormatted = cipherValueToBinaryFormatted.zfill(nLength)
                cipherText += ''.join(cipherValueToBinaryFormatted)
            print(f"The cipher text is {cipherText}.")
            input("Press Enter to go back to menu.")
        else:
            input("Entered number is not prime. Try again.")
    else:
        input("Entered number is not prime. Try again.")

def decrypt():
    p = int(input("Enter a prime number p (secret key):- "))
    isNumPrime = isPrime(p)
    if (isNumPrime == 1):
        q = int(input("Enter another prime number q (secret key):- "))
        isNumPrime = isPrime(q)
        if (isNumPrime == 1):
            n = p * q
            nLength = calculateN(n)
            eulersTotient = (p - 1) * (q - 1)
            e = int(input("Enter your public key e:- "))
            d = pow(e, -1, eulersTotient)
            cipherText = input("Enter cipher to decrypt (number):- ")
            cipherTextBlock = prepareBlock(cipherText, nLength)
            cTextBlockToInt = blocksToInt(cipherTextBlock)
            plainTextToIntegerBlock = []
            for cipher in cTextBlockToInt:
                plainTextInt = pow(cipher, d, n)
                plainTextToIntegerBlock.append(plainTextInt)
            plainTextIntBinary = intToBinary(plainTextToIntegerBlock, nLength - 1)
            plainText = binaryToString(plainTextIntBinary, 8)
            print(f"The plain text is {plainText}.")
            input("Press Enter to go back to menu.")
        else:
            input("Entered number is not prime. Try again.")
    else:
        input("Entered number is not prime. Try again.")

if __name__ == "__main__":
    while (True):
        os.system('cls')
        print("RSA Algorithm")
        print("-------------")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3):- "))
        if (choice == 1):
            encrypt()
        elif (choice == 2):
            decrypt()
        elif (choice == 3):
            break
        else:
            input("Wrong choice. Press Enter to try again.")