import base64
from Crypto.Cipher import AES


def encryptImg():

    key = "!1TDCRfiap2020#!"
    aes = AES.new(key, AES.MODE_ECB)

    with open('logo.jpeg', 'rb') as img:
        # binary to string
        img_binary = img.read()
        img64 = base64.b64encode(img_binary)
        img64_string = img64.decode('utf-8')

        # encryption -> 41992 + 8 bytes = 42000 bytes
        img64_string = img64_string + '11111111'
        img_encrypted = aes.encrypt(img64_string)

    if(len(img_encrypted) > 0):
        with open("img_encrypted_ransomware.csv", "wb") as img_encrypted_ransomware:
            img_encrypted_ransomware.write(img_encrypted)

        print("File encrypted")
    else:
        print("File could not be encrypted. Try again")

    img.close()


def decryptImg():

    key = "!1TDCRfiap2020#!"
    aes = AES.new(key, AES.MODE_ECB)

    with open('img_encrypted_ransomware.csv', 'rb') as img_encrypted:
        # file to string
        img64_encrypted = img_encrypted.read()
        img64_decrypted = aes.decrypt(img64_encrypted)
        img64_string = img64_decrypted.decode('utf-8')

        # string to binary
        img64_array = img64_string.split("11111111")
        img_binary = base64.b64decode(img64_array[0])

        # decryption
        if(len(img_binary) > 0):
            with open("img_decrypted.jpeg", "wb") as img:
                img.write(img_binary)

            print("Image decrypted.")
        else:
            print("File could not be decrypted. Try again")
    img.close()
