import os

def vigenereTable(letter):
    letterToNumMap = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21,
        "W": 22, "X": 23, "Y": 24, "Z": 25
    }
    return letterToNumMap.get(letter)

def reverseVignereTable(numericalValue):
    numToLetterMap = {
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K",
        11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U",
        21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"
    }
    return numToLetterMap.get(numericalValue)

def generateKey(key, plainTextLength):
    keyLength = len(key)
    generatedKey = list(key)
    if (plainTextLength == keyLength):
        return generatedKey
    else:
        for i in range (plainTextLength - keyLength):
            generatedKey.append(generatedKey[i % keyLength])
    return generatedKey

def encryptUsingVigenere(plainText, key):
    plainText = plainText.replace(" ", "")
    plainText = plainText.upper()
    key = key.upper()
    finalKey = generateKey(key, len(plainText))
    cipherText = ""
    plainTextList = list(plainText)

    for i in range(len(plainText)):
        plainTextNumValue = vigenereTable(plainTextList[i])
        keyNumValue = vigenereTable(finalKey[i])
        cipherValue = (plainTextNumValue + keyNumValue) % 26
        cipherText = "".join([cipherText, reverseVignereTable(cipherValue)])
    return cipherText

def decryptUsingVigenere(cipherText, key):
    cipherText = cipherText.upper()
    key = key.upper()
    finalKey = generateKey(key, len(cipherText))
    plainText = ""
    cipherTextList = list(cipherText)

    for i in range(len(cipherText)):
        cipherTextNumValue = vigenereTable(cipherTextList[i])
        keyNumValue = vigenereTable(finalKey[i])
        decryptedValue = (cipherTextNumValue - keyNumValue) % 26
        plainText = "".join([plainText, reverseVignereTable(decryptedValue)])
    return plainText

if __name__ == "__main__":
    while(True):
        os.system('cls')
        print("Vernam-Vigenere Cipher")
        print("----------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        option = int(input("Enter your choice (1-3):- "))
        if (option == 1):
            plainText = input("Enter the text to be encrypted:- ")
            key = input("Enter the key (Key should be text):- ")
            print(f"The encrypted message is {encryptUsingVigenere(plainText, key)}.")
            input("Press Enter to continue...")
        elif (option == 2):
            cipher = input("Enter the text to be decrypted:- ")
            key = input("Enter the key (Key should be text):- ")
            print(f"The encrypted message is {decryptUsingVigenere(cipher, key)}.")
            input("Press Enter to continue...")
        elif (option == 3):
            break
        else:
            input("Wrong entry! Press Enter to continue...")