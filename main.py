from functions import *

answer = "Y"

while answer == "Y":
    print("\nMenu Options:")
    print("Press 1 for encryption | Press 2 for decryption | Press 0 to exit")

    menu = input("Option: ")

    if menu == "1":
        encryptImg()
    elif menu == "2":
        decryptImg()
    elif menu == "0":
        answer = "N"
    else:
        print("Invalid option, try again!")
        answer = input("Do you wish to try again? Y/N").upper()
