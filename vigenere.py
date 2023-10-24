from cipher import Cipher

class Vigenere(Cipher):

    def __init__(self):
        self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def repetir_senha(self, senha, text):
        #Repete até o tamanho do texto inserido
        if len(senha) < len(text):
            new_pass = senha * int((len(text)/len(senha)))
            if len(new_pass):
                new_pass += senha[:len(new_pass)]
            return new_pass.upper()
        return senha.upper()
    
    def cifra(self, plaintext, senha, descripto=False):
        senha = self.repetir_senha(senha, plaintext)
        plaintext = self.format_str(plaintext)
        textout = ''
        for idx, char in enumerate(plaintext.upper()):
            idx_key = self.plain.find(senha[idx])
            c_alphabet = self.shift_alphabet(self.plain, idx_key)
            if descripto:
                idx_p = c_alphabet.find(char)
                textout += self.plain[idx_p]
            else:
                idx_p = self.plain.find(char)
                textout += c_alphabet[idx_p]
        return textout
    
    def decifra(self,  ciphertext, senha):
        return self.cifra(ciphertext, senha, True)
