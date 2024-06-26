# William Hahn

encoded_password = 0

def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # shifting up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded_password):
    encoded_password = str(encoded_password)
    decodedlist = []
    decoded = ""
    for i in range(len(encoded_password)):
        i = (int(encoded_password[i]) - 3) % 10
        decodedlist.append(str(i))
    for i in range(len(decodedlist)):
        decoded = decoded + str(decodedlist[i])
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is: {int(encoded_password)}, the decoded password is {int(decoded_password)}.")
            print()
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose again.\n")


if __name__ == "__main__":
    main()
