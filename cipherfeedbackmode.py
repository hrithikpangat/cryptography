def cfm_encrypt(plaintext, s, iv, permutation_key):
    ciphers = []
    updated_iv = []
    xor_result = []

    split_plaintext = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]

    """ xor function"""
    for i in split_plaintext:
        iv_temp = iv[:4]
        updated_iv.append(iv)
        xor_val = int(i, 2) ^ int(iv_temp, 2)
        xor_result.append(bin(xor_val)[2:].zfill(4))

        """ function for permutation """
        cipher_block = ''
        for index in permutation_key:
            cipher_block += xor_result[-1][int(index) - 1]

        ciphers.append(cipher_block)

        """ updating the iv """
        iv = iv[s:] + bin(int(cipher_block, 2))[2:].zfill(4)
        iv = iv[-6:]


        cipher_text = "".join(ciphers)
    return cipher_text,updated_iv

""" function for inversing the key """
def inverse_permutation_key(permutation_key):
    positions = [0] * len(permutation_key)
    for i, char in enumerate(permutation_key):
        positions[int(char) - 1] = i + 1

    inverse_key = ''.join(str(pos) for pos in positions)
    return inverse_key

def cmf_decrypt(ciphertext,updated_iv, inverse_key):
    xor_result = []
    split_cipher_text = [ciphertext[i:i + 4] for i in range(0, len(ciphertext), 4)]

    """ permutation function"""
    permuted_cipher_list = []
    for each_val in split_cipher_text:
        each_val_binary = list(each_val)
        for index in inverse_key:
            permuted_cipher_list.append(each_val_binary[int(index) - 1])

    permuted_cipher_text = ''.join(permuted_cipher_list)
    split_permuted_cipher = [permuted_cipher_text[i:i + 4] for i in range(0, len(permuted_cipher_text), 4)]

    """ xor function """

    for i, k in zip(split_permuted_cipher, updated_iv):

        xor_val = int(i, 2) ^ int(k[:4], 2)
        xor_result.append(bin(xor_val)[2:].zfill(4))

    decrypted_text = ''.join(xor_result)
    return decrypted_text


""" test case """
plaintext = '101101110110'
s = 4
iv = '011011'
permutation_key = '3421'

print(f"plaintext : {plaintext}")
result = cfm_encrypt(plaintext,s,iv,permutation_key)
ciphertext = result[0]
print(f"ciphertext :{result[0]}")
updated_iv = result[1]
inverse_key = inverse_permutation_key(permutation_key)
decrypted_text = cmf_decrypt(ciphertext,updated_iv,inverse_key)
print(f"decrypted_text :{decrypted_text}")