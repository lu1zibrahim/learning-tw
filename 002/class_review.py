from cachorro import Cachorro
from gato import Gato
from animal import Animal
from dono import Dono


# cachorro = Cachorro("Beto", 4, "Preto", 3, dono=Dono('José'))
# print(cachorro.nome)
# print(cachorro.idade)
# cachorro.idade = 5
# print(cachorro.idade)
# print(cachorro.dono.nome)
# print(cachorro.cor)
# print(cachorro.fazer_barulho())
# print(cachorro._Cachorro__qtd_brinquedos)
# print(cachorro.brincar())
# cachorro2 = Cachorro("Tótó", 2, "Caramelo", 2)
# print(cachorro2.nome)
# print(cachorro2.fazer_barulho())
#
# gato = Gato("Mimi", 2, "Branco", 5, dono=Dono('Maria'))
# print(gato.fazer_barulho())
# print(gato.qtd_bolinhas)
# print(gato.brincar())
# print(gato.dono.nome)


lista_cachorro = list()
lista_gato = list()

while True:
    print(25*"-")
    print("1. Cadastrar usuário")
    print("2. Cadastrar cachorro")
    print("3. Cadastrar gato")
    print("4. Listar cachorros")
    print("5. Listar gatos")
    print("6. Brincar cachorros")
    print("7. Brincar gatos")
    print("8. Sair")
    print(25*"-")

    global dono
    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        nome_usuario = input("Digite o nome do usuário: ")
        dono = Dono(nome_usuario)
    elif opcao == 2:
        nome_cachorro = input("Digite o nome do cachorro: ")
        idade_cachorro = input("Digite a idade do cachorro: ")
        cor_cachorro = input("Digite a cor do cachorro: ")
        qtd_brinquedos_cachorro = input("Digite a quantidade de brinquedos do cachorro: ")
        cachorro = Cachorro(nome_cachorro, idade_cachorro, cor_cachorro, qtd_brinquedos_cachorro, dono=dono)
        lista_cachorro.append(cachorro)
    elif opcao == 3:
        nome_gato = input("Digite o nome do gato: ")
        idade_gato = input("Digite a idade do gato: ")
        cor_gato = input("Digite a cor do gato: ")
        qtd_bolinhas_gato = input("Digite a quantidade de bolinhas do gato: ")
        gato = Gato(nome_gato, idade_gato, cor_gato, qtd_bolinhas_gato,dono=dono)
        lista_gato.append(gato)
    elif opcao == 4:
        for cachorro in lista_cachorro:
            print(cachorro)
    elif opcao == 5:
        for gato in lista_gato:
            print(gato)
    elif opcao == 6:
        for cachorro in lista_cachorro:
            print(cachorro.brincar())
            if cachorro.felicidade >= 5:
                print(cachorro.fazer_barulho())
    elif opcao == 7:
        for gato in lista_gato:
            print(gato.brincar())
            if gato.felicidade >= 1:
                print(gato.fazer_barulho())
    else:
        break