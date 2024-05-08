import os

def encryptUsingECB(plainText):
    encECB = {
        "000": "010",
        "001": "100",
        "010": "101",
        "100": "110",
        "101": "011",
        "110": "111",
        "011": "000",
        "111": "001"
    }
    cipherText = ""
    padLength = 3 - (len(plainText) % 3)
    
    if (padLength == 3):
        plainText += "000"
    elif (padLength == 2):
        plainText += "10010"
    else:
        plainText += "1001"
    
    for i in range (0, len(plainText), 3):
        block = plainText[i: i+3]
        cipherText += encECB.get(block)
    
    return cipherText

def decryptUsingECB(cipherText):
    decECB = {
        "010": "000",
        "100": "001",
        "101": "010",
        "110": "100",
        "011": "101",
        "111": "110",
        "000": "011",
        "001": "111"
    }
    plainText = ""

    for i in range (0, len(cipherText), 3):
        block = cipherText[i: i+3]
        plainText += decECB.get(block)
    
    padValue = plainText[-3:]

    if (padValue == "000"):
        plainText = plainText[:len(plainText) - 3]
    elif (padValue == "001"):
        plainText = plainText[:len(plainText) - 4]
    elif (padValue == "010"):
        plainText = plainText[:len(plainText) - 5]
    
    return plainText

def encryptUsingCBC(plainText):
    encECB = {
        "000": "010",
        "001": "100",
        "010": "101",
        "100": "110",
        "101": "011",
        "110": "111",
        "011": "000",
        "111": "001"
    }
    initialValue = "001"
    cipherText = ""
    padLength = 3 - (len(plainText) % 3)

    if (padLength == 3):
        plainText += "000"
    elif (padLength == 2):
        plainText += "10010"
    else:
        plainText += "1001"
    
    for i in range (0, len(plainText), 3):
        block = plainText[i: i+3]
        xorValue = str(int(initialValue) ^ int(block))
        xorValue = xorValue.zfill(3)
        cipherBlock = str(encECB.get(xorValue))
        initialValue = cipherBlock
        cipherText += cipherBlock
    
    return cipherText

def decryptUsingCBC(cipherText):
    decECB = {
        "010": "000",
        "100": "001",
        "101": "010",
        "110": "100",
        "011": "101",
        "111": "110",
        "000": "011",
        "001": "111"
    }
    initialValue = "001"
    plainText = ""

    for i in range (0, len(cipherText), 3):
        block = cipherText[i: i+3]
        plainBlockWithIV = str(decECB.get(block))
        plainBlock = str(int(initialValue) ^ int(plainBlockWithIV))
        plainBlock = plainBlock.zfill(3)
        initialValue = block
        plainText += plainBlock

    padValue = plainText[-3:]
        
    if (padValue == "000"):
        plainText = plainText[:len(plainText) - 3]
    elif (padValue == "001"):
        plainText = plainText[:len(plainText) - 4]
    elif (padValue == "010"):
        plainText = plainText[:len(plainText) - 5]
    
    return plainText

if __name__ == '__main__':
    while(True):
        os.system('cls')
        print("Block Ciphers")
        print("--------------")
        print("1. ECB Mode")
        print("2. CBC Mode")
        print("3. Quit")
        choice = int(input("Enter your choice (1-3):- "))
        if (choice == 1):
            while (True):
                os.system('cls')
                print("ECB-Mode Encryption")
                print("-------------------")
                print("1. Encrypt using ECB")
                print("2. Decrypt using ECB")
                print("3. Exit")
                option = int(input("Enter your choice (1-3):- "))
                if (option == 1):
                    plainText = input("Enter the value to encrypt (in binary):- ")
                    print(f"The encrypted value is {encryptUsingECB(plainText)}.")
                    print()
                    option = int(input("Enter your choice (1-3):- "))
                elif (option == 2):
                    cipher = input("Enter the value to decrypt (in binary):- ")
                    print(f"The decrypted value is {decryptUsingECB(cipher)}.")
                    print()
                    option = int(input("Enter your choice (1-3):- "))
                elif (option == 3):
                    break
                else:
                    print("Invalid option selected!")
                    option = int(input("Enter your choice (1-3):- "))
        elif (choice == 2):
            while (True):
                os.system('cls')
                print("CBC-Mode Encryption")
                print("-------------------")
                print("1. Encrypt using CBC")
                print("2. Decrypt using CBC")
                print("3. Exit")
                option = int(input("Enter your choice (1-3):- "))
                if (option == 1):
                    plainText = input("Enter the value to encrypt (in binary):- ")
                    print(f"The encrypted value is {encryptUsingCBC(plainText)}.")
                    print()
                    option = int(input("Enter your choice (1-3):- "))
                elif (option == 2):
                    cipher = input("Enter the value to decrypt (in binary):- ")
                    print(f"The decrypted value is {decryptUsingCBC(cipher)}.")
                    print()
                    option = int(input("Enter your choice (1-3):- "))
                elif (option == 3):
                    break
                else:
                    print("Invalid option selected!")
                    option = int(input("Enter your choice (1-3):- "))
        elif (choice == 3):
            break
        else:
            print("Invalid option selected!")
            choice = int(input("Enter your choice (1-3):- "))