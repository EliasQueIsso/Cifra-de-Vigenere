class Cipher(object):
    def format_str(self, text):
        return text.replace(' ', ' ').upper()
    def shift_alphabet(self, alphabet, shift):
        return alphabet[shift:] + alphabet[:shift]
    
    from cipher import Cipher
    class Vigenere(Cipher):
        def __init__(self):
            self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def repeat_password(self, password, text):
            if len(password) < len(text):
                new_pass = password * int((len(text)/len(password)))
                if len(new_pass):
                    new_pass += password[:len(new_pass)]
                return new_pass.upper()
            return password.upper()
        def cripto(self, plaintext, password, descripto=False):
            password = self.repeat_password(password, plaintext)
            plaintext = self.format_str(plaintext)
            textout = ''
            for idx, char in enumerate(plaintext.upper()):
                idx_key = self.plain.find(password[idx])
                c_alphabet = self.shift_alphabet(self.plain, idx_key)
                if descripto:
                    idx_p = c_alphabet.find(char)
                    textout += self.plain[idx_p]
                else:
                    idx_p = self.plain.find(char)
                    textout += c_alphabet[idx_p]
            return textout
        def descripto(self,  ciphertext, password):
            return self.cripto(ciphertext, password, True)
    
    from vigenere import Vigenere
    import sys

    versao = sys.version_info[0]

    if versao == 2:
        leitura = raw_input
    elif versao == 3:
        leitura = input
    txt_in = leitura('Texto a ser cifrado: ')
    password = leitura('Senha: ')

    cifra = Vigenere()
    txt_cifrado = cifra.cripto(txt_in, password)
    print
    print('Texto cifrado: {0}'.format(txt_cifrado))
    print('  Texto plano: {0}'.format(cifra.descripto(txt_cifrado, password)))