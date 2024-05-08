def encrypt(plaintext,counter,permutation_key):
    xor_val = []
    """ splitting the plain text into 4 bit sizes"""
    split_plaintext = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]
    # print(splited_plaintext)

    """ doing the xor operation"""

    for i in split_plaintext:
        xor_result = int(i, 2) ^ int(fbB[counter], 2)
        counter = counter + 1
        xor_val.append(bin(xor_result)[2:].zfill(4))

    """ permutation function"""

    permuted_list = []
    for each_val in xor_val:
        each_val_binary = list(each_val)
        for index in permutation_key:
            permuted_list.append(each_val_binary[int(index) - 1])

    permuted_string = ''.join(permuted_list)
    return permuted_string

"""  function for inversing the key """
def inverse_permutation_key(permutation_key):
    positions = [0] * len(permutation_key)
    for i, char in enumerate(permutation_key):
        positions[int(char) - 1] = i + 1
        #print(positions)
    inverse_key = ''.join(str(pos) for pos in positions)
    return inverse_key

def decrypt(cipher_text, counter, inverse_key):
    xor_final = []
    """ splitting the cipher text into 4bit size and applying reverse key permutation in it"""
    split_cipher_text = [cipher_text[i:i + 4] for i in range(0, len(cipher_text), 4)]
    permuted_cipher_list = []
    for each_val in split_cipher_text:
        each_val_binary = list(each_val)
        for index in inverse_key:
            permuted_cipher_list.append(each_val_binary[int(index) - 1])
    permuted_cipher_text = ''.join(permuted_cipher_list)

    """ split the permuted ciphertext into four bit sizes and do the xor operation"""

    split_permuted_cipher_text = [permuted_cipher_text[i:i + 4] for i in range(0, len(permuted_cipher_text), 4)]

    for i in split_permuted_cipher_text:
        xor_result = int(i, 2) ^ int(fbB[counter], 2)
        xor_final.append(bin(xor_result)[2:].zfill(4))
        counter += 1

    decrypted_string = ''.join(xor_final)
    return decrypted_string


fbB = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
#plaintext = input("enter the plaintext: ")
plaintext ='100110101001'
#counter = int(input("enter the counter value:"))
counter=0
#permutation_key = input("enter the key combination:")
permutation_key ='3214'
inverse_key = inverse_permutation_key(permutation_key)

print(f"plain text : {plaintext}")
cipher_text = encrypt(plaintext,counter,permutation_key)
print(f"cipher text : {cipher_text}")

decrypted_text = decrypt(cipher_text,counter,inverse_key)
print(f"decrypted text : {decrypted_text}")


