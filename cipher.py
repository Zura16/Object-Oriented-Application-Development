class Cipher:

    def __init__(self):
        self._alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @property
    def alphabet(self):
        return self._alphabet

    def encrypt_message(self, letter):
        encrypted_message = ""
        for char in letter.upper():
            if char.isalpha():
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_message(self, message):
        decrypted_message = ""
        for char in message.upper():
            if char.isalpha():
                decrypted_message += self._decrypt_letter(char)
            else:
                decrypted_message += char
        return decrypted_message

    def _encrypt_letter(self, letter):
        pass

    def _decrypt_letter(self, letter):
        pass
