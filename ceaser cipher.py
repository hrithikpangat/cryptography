from substituitionCipher import substitutionCipher

def ceasarCipherEncryption(plainText):
    encryptedString = substitutionCipher(plainText, 3)
    return encryptedString

def ceasarCipherDecryption(cipherText):
    decryptedString = ""
    key = 3
    for i in (cipherText):
        asciiValue = ord(i)
        shiftedAsciiValue = asciiValue - key
        if (shiftedAsciiValue < 65):
            shiftedAsciiValue = 91 - ((65 - shiftedAsciiValue) % 26)
            decryptedString += chr(shiftedAsciiValue)
        elif (shiftedAsciiValue < 97 and asciiValue > 96):
            shiftedAsciiValue = 123 - ((97 - shiftedAsciiValue) % 26)
            decryptedString += chr(shiftedAsciiValue)
        else:
            decryptedString += chr(shiftedAsciiValue)
    return decryptedString

if __name__ == '__main__':
    string = input("Enter the string:- ")
    operation = int(input("Enter 1 to encrypt and 2 to decrypt using Caesar Cipher:- "))
    if (operation == 1):
        print(f"The encrypted string is {ceasarCipherEncryption(string)}.")
    elif (operation == 2):
        print(f"The decrypted string is {ceasarCipherDecryption(string)}.")
    else:
        print("Enter a valid operation!")