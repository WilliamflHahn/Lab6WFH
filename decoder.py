def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)  # shifting down by 3 numbers
        decoded_password += decoded_digit
    return decoded_password


if 'encoded_password' not in locals():
    print("Please encode a password first.\n")
    continue
decoded_password = decode_password(encoded_password)
print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")