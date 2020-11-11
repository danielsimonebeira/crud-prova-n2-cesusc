from pessoa import *

def menu():
    while True:
        escolha = int(input("Digite a opção desejada:"
                            "\n[1] - Cadastrar (create)"
                            "\n[2] - Consultar (read)"
                            "\n[3] - Editar    (Update)"
                            "\n[4] - Deletar   (delete)"
                            "\n[5] - Sair"
                            "\n "))
        cadastro = Pessoa()
        if escolha == 1:
            cadastro.cria_usuario()
        elif escolha == 2:
            cadastro.consulta()
        elif escolha == 3:
            cadastro.edita()
        elif escolha == 4:
            cadastro.deleta()
        elif escolha == 5:
            quit()
        else:
            print("\nFavor, digitar os numeros de 1 a 5!\n")


if __name__ == '__main__':
    menu()


