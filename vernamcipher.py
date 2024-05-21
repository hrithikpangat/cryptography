import random

def generateKey(plainTextLength):
    key = "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(plainTextLength))
    return key

def encryptUsingVernam(plainText, key):
    plainTextList = list(plainText)
    keyList = list(key)
    cipherText = []
    for i in range(len(plainText)):
        plainTextNum = ord(plainTextList[i])
        keyNum = ord(keyList[i])
        cipherValue = plainTextNum ^ keyNum
        cipherText.append(cipherValue)
    return cipherText

def decryptUSingVernam(cipherText, key):
    keyList = list(key)
    plainText = ""
    for i in range(len(cipherText)):
        keyNum = ord(keyList[i])
        keyNum = ord(keyList[i])
        plainValue = int(cipherText[i]) ^ keyNum
        plainChar = chr(plainValue)
        plainText = "".join([plainText, plainChar])
    return plainText

if __name__ == '__main__':
    while(True):
        print("Vernam Cipher")
        print("-------------")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Quit")
        choice = int(input("Enter your choice (1-3):- "))
        if (choice == 1):
            plainText = input("Enter the text to be encrypted:- ")
            key = generateKey(len(plainText))
            cipher = encryptUsingVernam(plainText, key)
            print(f"The encrypted text in denary is {cipher}. The key used to encrypt is {key}.")
        elif (choice == 2):
            cipher = input("Enter the cipher (in denary) separated by comma:- ")
            cipherList = cipher.split(",")
            key = input("Enter the decryption key:- ")
            if (len(key) != len(cipherList)):
                print("Length of key should match the length of cipher text. Error!")
                break
            decryptedText = decryptUSingVernam(cipherList, key)
            print(f"The decrypted text is {decryptedText}.")
        elif (choice == 3):
            break
        else:
            print("\nWrong option. Retry!!!")