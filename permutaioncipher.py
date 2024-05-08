import os

def sortBasedOnPermutation(block, permutation):
    permutedBlock = [block[i - 1] for i in permutation]

    return permutedBlock

def inverseOfKey(key):
    sortedKey = sorted(key)
    combined = list(zip(key, sortedKey))
    sortedCombined = sorted(combined, key=lambda x: x[0])
    originalKey, inverseKey = zip(*sortedCombined)

    return inverseKey

def encryptMessage(plainText, key):
    keyLength = len(key)
    encryptedText = ""
    plainText = plainText.replace(" ", "")
    plainText = plainText.lower()
    if len(plainText) % keyLength == 0:
        paddingLength = 0
    else:
        paddingLength = keyLength - (len(plainText) % keyLength)
    plainText += 'x' * paddingLength
    plainText = list(plainText)
    for i in range (0, len(plainText), keyLength):
        block = plainText[i:i + keyLength]
        permutedBlock = sortBasedOnPermutation(block, key)
        encryptedBlock = "".join(permutedBlock)
        encryptedText += encryptedBlock
    return encryptedText

def decryptMessage(cipherText, key):
    keyLength = len(key)
    plainText = ""
    cipherText = list(cipherText)
    inverseKey = inverseOfKey(key)
    for i in range (0, len(cipherText), keyLength):
        block = cipherText[i:i + keyLength]
        decryptedBlock = sortBasedOnPermutation(block, inverseKey)
        plainText += "".join(decryptedBlock)
    return plainText

if __name__ == '__main__':
    while(True):
        os.system('cls')
        print("Permutation Cipher")
        print("------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        option = int(input("Enter your choice (1-3):- "))
        if (option == 1):
            plainText = input("Enter the text to be encrypted:- ")
            key = input("Enter the key (Starting position is 1):- ")
            keyList = list(key)
            key = [int(i) for i in keyList]
            print(f"The encrypted message is {encryptMessage(plainText, key)}.")
            input("Press Enter to continue...")
        elif (option == 2):
            cipher = input("Enter the text to be decrypted:- ")
            key = input("Enter the key (Starting position is 1):- ")
            keyList = list(key)
            key = [int(i) for i in keyList]
            print(f"The encrypted message is {decryptMessage(cipher, key)}.")
            input("Press Enter to continue...")
        elif (option == 3):
            break
        else:
            input("Wrong entry! Press Enter to retry...")