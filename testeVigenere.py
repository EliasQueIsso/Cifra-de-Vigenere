from vigenere import Vigenere



leitura = input

print("*"*25)
print(" ")
print("Este é um programa feito pra você denunciar anonimamente um crime ambiental")
print(" ")
print("*"*25)

denuncia = input("Deseja fazer uma denúncia?\nS/N: ")
denuncia_upper = denuncia.upper()

match denuncia_upper:
    case 'S':
        txt_in = leitura('Escreva a sua denúncia: ')
        senha = leitura('Informe uma senha para a criptografia: ')

        cifra = Vigenere()
        txt_cifrado = cifra.cifra(txt_in, senha)
        print('Denúncia criptografada: {0}'.format(txt_cifrado))
        print('Muito obrigado pela sua denúncia, o meio ambiente agradece.')
    case 'N':
        descripto = input("Deseja descriptografar uma denúncia?\nS/N: ")
        if (descripto == 'S' or descripto == 's'):    
            txt_cifrado = leitura('Escreva a denúncia criptografa: ')
            senha = leitura('Informe a senha usada na criptografia: ')

            cifra = Vigenere()
            txt_descripto = cifra.decifra(txt_cifrado, senha)
            print('Denúncia descriptografada: {0}'.format(txt_descripto))
        elif (descripto == 'N' or descripto == 'n'):
            print('Obrigado por usar o nosso software.')
        else:
            print('Insira uma opção váida.')
    case _:
        print('Insira uma opção válida.')
