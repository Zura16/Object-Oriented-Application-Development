from atbash import AtbashCipher
from caesar_cipher import CaesarCipher
from check_input import get_int_range
from check_input import get_yes_no


def main():
    print("Secret Decoder Ring:")

    while True:
        choice = input("1. Encrypt\n2. Decrypt\n").lower()
        if choice == "1":
            cipher_choice = input("Enter encryption type:\n1. Atbash\n2. Caesar\n").lower()
            if cipher_choice == "1":
                cipher = AtbashCipher()
            elif cipher_choice == "2":
                shift = get_int_range("Enter the shift value (0-25): ", 0, 25)
                cipher = CaesarCipher(shift)
            else:
                print("Invalid cipher choice.")
                continue

            message = input("Enter the message to encrypt: ")
            encrypted_message = cipher.encrypt_message(message)
            with open("message.txt", "w") as f:
                f.write(encrypted_message)
            print(f"Encrypted message has been written to message.txt.\nEncrypted message written to file:\n{encrypted_message}")
            if not get_yes_no("\nContinue playing? (y/n): "):
                break

        elif choice == "2":
            try:
                with open("message.txt", "r") as f:
                    encrypted_message = f.read()
            except FileNotFoundError:
                print("No message found to decrypt.")
                continue

            cipher_choice = input("Enter decryption type:\n1. Atbash\n2. Caesar\n").lower()
            if cipher_choice == "1":
                cipher = AtbashCipher()
            elif cipher_choice == "2":
                shift = get_int_range("Enter the shift value (0-25): ", 0, 25)
                cipher = CaesarCipher(shift)
            else:
                print("Invalid cipher choice.")
                continue

            decrypted_message = cipher.decrypt_message(encrypted_message)
            print("Decrypted message:", decrypted_message)
            break

        else:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
