from comum import *

class Pessoa:
    def cria_usuario(self):
        try:
            caractere = Caractere()
            valida_email = Estrutura_email()
            memoria = Memoria()
            print(50 * '=' + '\nCadastro de usuário ( CREATE )' + '\n' + 50 * '=')

            nome = input("Nome: ")
            caractere.texto_obrigatorio(nome)
            caractere.quantidade(nome, 150)

            cpf = input("CPF: ")
            caractere.texto_obrigatorio(cpf)
            Estrutura_cpf(cpf)
            memoria.valida_duplicado(cpf)

            email = input("E-mail: ")
            caractere.texto_obrigatorio(email)
            caractere.quantidade(email, 400)
            valida_email.verifica(email)

            memoria.grava(nome, cpf, email, "S")

        except ValueError as error:
            print(error)


    def consulta(self):
        memoria = Memoria()
        print(50 * '=' + '\nConsulta de usuário ( READ )' + '\n' + 50 * '=')
        valor_pesquisa = input("Digite (nome, cpf ou email): ")
        memoria.consulta(valor_pesquisa)


    def edita(self):
        memoria = Memoria()
        print(50 * '=' + '\nEdita usuário ( UPDATE )' + '\n' + 50 * '=')
        valor_edita = input("Digite (nome, cpf ou email): ")
        memoria.edicao(valor_edita)


    def deleta(self):
        memoria = Memoria()
        print(50 * '=' + '\nDelete usuário ( DELETE )' + '\n' + 50 * '=')
        valor_deleta = input("Digite (nome, cpf ou email): ")
        memoria.deleta(valor_deleta)