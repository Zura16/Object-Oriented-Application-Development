from cipher import Cipher

class CaesarCipher(Cipher):

    def __init__(self, shift):
        super().__init__()
        if shift < 0 or shift > 25:
            raise ValueError("Shift value must be between 0 and 25.")
        self.shift = shift

    def _encrypt_letter(self, letter):
        index = self.alphabet.index(letter)
        encrypted_index = (index + self.shift) % 26
        return self.alphabet[encrypted_index]

    def _decrypt_letter(self, letter):
        index = self.alphabet.index(letter)
        decrypted_index = (index - self.shift) % 26
        return self.alphabet[decrypted_index]
