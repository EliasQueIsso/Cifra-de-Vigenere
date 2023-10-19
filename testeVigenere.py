from vigenere import Vigenere
import sys

versao = sys.version_info[0]

if versao == 2:
    leitura = raw_input
elif versao == 3:
    leitura = input

print("*"*25)
print(" ")
print("Este é um programa feito pra você denunciar anonimamente um crime ambiental")
print(" ")
print("*"*25)

denuncia = input("Deseja fazer uma denúncia?\nS/N: ")

match denuncia:
    case 'S':
        txt_in = leitura('Escreva a sua denúncia: ')
        password = leitura('Informe uma senha para a criptografia: ')

        cifra = Vigenere()
        txt_cifrado = cifra.cripto(txt_in, password)
        print('Denúncia criptografada: {0}'.format(txt_cifrado))
        print('Muito obrigado pela sua denúncia, o meio ambiente agradece.')
    case 'N':
        descripto = input("Deseja descriptografar uma denúncia?\nS/N: ")
        if (descripto == 'S'):    
            txt_cifrado = leitura('Escreva a denúncia criptografa: ')
            password = leitura('Informe a senha usada na criptografia: ')

            cifra = Vigenere()
            txt_descripto = cifra.descripto(txt_cifrado, password)
            print('Denúncia descriptografada: {0}'.format(txt_descripto))
        elif (descripto == 'N'):
            print('Obrigado por usar o nosso software.')
        else:
            print('Insira uma opção váida.')
    case _:
        print('Insira uma opção válida.')
'''
txt_in = leitura('Texto a ser cifrado: ')
password = leitura('Senha: ')

cifra = Vigenere()
txt_cifrado = cifra.cripto(txt_in, password)
print
print('Texto cifrado: {0}'.format(txt_cifrado))
print('  Texto plano: {0}'.format(cifra.descripto(txt_cifrado, password)))
'''