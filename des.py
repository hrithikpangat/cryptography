from Crypto.Cipher import DES
import base64

def encrypt_des(key, data):
    des = DES.new(key, DES.MODE_ECB)
    padded_data = data + ((8 - len(data) % 8) * ' ')
    encrypted_data = des.encrypt(padded_data.encode())
    return base64.b64encode(encrypted_data).decode()

def decrypt_des(key, encrypted_data):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_data = des.decrypt(base64.b64decode(encrypted_data)).decode().rstrip()
    return decrypted_data

key = input("Enter 8-character DES key: ")
data = input("Enter data to encrypt: ")

encrypted_data = encrypt_des(key.encode(), data)
print("Encrypted data:", encrypted_data)

decrypted_data = decrypt_des(key.encode(), encrypted_data)
print("Decrypted data:", decrypted_data)