
def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

def decode(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

def main():
    shift = int(input("Enter the shift value: "))

    while True:
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            message = input("Enter the message to encode: ")
            encoded_message = encode(message, shift)
            print(f"Encoded message: {encoded_message}")
        elif choice == "2":
            encoded_message = input("Enter the message to decode: ")
            decoded_message = decode(encoded_message, shift)
            print(f"Decoded message: {decoded_message}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


main()
