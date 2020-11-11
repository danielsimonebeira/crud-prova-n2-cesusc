import re

class Memoria:
    lista_cad = []
    def grava(self, nome, cpf, email, flag):
        dicionario = {}
        novo = [('nome', nome), ('cpf', cpf), ('email', email), ('flAtivo', flag)]
        dicionario.update(novo)
        self.lista_cad.append(dicionario)
        print(40 * '-')
        print(self.lista_cad)
        print(40 * '-')

    def valida_duplicado(self, valor_digitado):
        for dados in self.lista_cad:
            for valor_memoria in dict.values(dados):
                if valor_digitado == valor_memoria:
                    raise ValueError('\n' + 120 * '-' + '\n' +
                                     "CPF já cadastrado!" + '\n' + 120 * '-')

    # TO-DO: Reduzir o codigo em mais metodos de forma simplificada
    def consulta(self, valor):
        for dados in self.lista_cad:
            for grupo in dados:
                if valor == dados[grupo]:
                    dicionario_dados = dict(dados)
                    print('\n======_Resultado da Pesquisa_======')
                    for valida in dicionario_dados:
                        chave_flativo = str(valida).upper()
                        if chave_flativo == 'FLATIVO' and valida == 'N':
                            print("Usuário não encontrado...")
                        else:
                            for chave_nome in dicionario_dados:
                                chave_ajustado = str(chave_nome).upper()
                                if chave_ajustado == 'NOME':
                                    print(chave_ajustado, " : ", dicionario_dados[chave_nome])
                            for chave_cpf in dicionario_dados:
                                chave = str(chave_cpf).upper()
                                if chave == 'CPF':
                                    documento = Estrutura_cpf(dicionario_dados[chave_cpf])
                                    documento.retira_mascara_cpf(chave_cpf)
                                    cpf = documento.cria_mascara_cpf(dicionario_dados[chave_cpf])
                                    print(chave, " : ", cpf)
                            for chave_email in dicionario_dados:
                                chave = str(chave_email).upper()
                                if chave == 'EMAIL':
                                    print(chave.replace("EMAIL", "E-MAIL"), "= ", dicionario_dados[chave_email])
                            print('===================================\n')
                            break

    # TO-DO: Ajustar para utilizar o metodo de pesquisa(reduzir o código) e melhorar os nomes.
    #        Adicionar algumas validações para os fluxos de exceção.
    def edicao(self, altera):
        def altera_cadastro(chave, valor):
            nome = input("Novo {}: ".format(valor))
            teste[chave] = nome
            self.lista_cad[conta_lista] = teste
            print(40 * '-')
            print(self.lista_cad)
            print(40 * '-')
        for dados in self.lista_cad:
            for grupo in dados:
                if altera == dados[grupo]:
                    conta_lista = len(self.lista_cad) - 1
                    teste = dict(dados)
                    for chave in teste:
                        if teste[chave] == altera:
                            if teste['flAtivo'] == 'S':
                                novo_valor = int(input("Digite o numeto da opção abaixo para alterar no cadastro:\n(1) - Nome\n(2) - cpf\n(3) - E-mail\n"))
                                if novo_valor == 1:
                                    altera_cadastro(chave, 'Nome')
                                    break
                                elif novo_valor == 2:
                                    altera_cadastro(chave, 'CPF')
                                    break
                                elif novo_valor == 3:
                                    altera_cadastro(chave, 'E-mail')
                                    break
                                else:
                                    raise ValueError("Favor digitar numeros de 1 a 3!")

    # TO-DO: Ajustar para utilizar o metodo de pesquisa(reduzir o código) e melhorar os nomes
    def deleta(self, deleta):
        for dados in self.lista_cad:
            for grupo in dados:
                if deleta == dados[grupo]:
                    conta_lista = len(self.lista_cad) - 1
                    teste = dict(dados)
                    for x in teste:
                        if x == 'nome':
                            op = input("Deseja deletar o usuário {} \n(S) - Sim\n(N) - Não\n ".format(teste[x].upper()))
                            if op == 'S':
                                for valida in teste:
                                    chave_flativo = str(valida).upper()
                                    if chave_flativo == 'FLATIVO':
                                        teste['flAtivo'] = 'N'
                                        self.lista_cad[conta_lista] = teste
                                        print(40 * '-')
                                        print(self.lista_cad)
                                        print(40 * '-')
                            elif op == 'N':
                                print(50 * '-' +
                                      "O usuario {} não foi deletado.".format(teste['nome']) + 50 * '-')
                            else:
                                print(50 * '-' +
                                      "Favor digitar o S ou N" + 50 * '-')


class Caractere:
    def quantidade(self, valor_digitado, quantidade_limite):
        if not 0 <= len(valor_digitado) <= quantidade_limite:
            raise ValueError(
                '\n' + 120 * '-' + '\n' +
                'Quantidade de caracteres acima de {}.'.format(quantidade_limite) + '\n' + 120 * '-'
            )

    def texto_obrigatorio(self, valor_digitado):
        if len(valor_digitado) == 0 or valor_digitado == '':
            raise ValueError('\n' + 120 * '-' + '\n' +
                             "Campo obrigatório não preenchido!" + '\n' + 120 * '-')


class Estrutura_cpf:
    def __init__(self, documento_cpf):
        documento_cpf = str(documento_cpf)
        if self.cpf_eh_valido(documento_cpf):
            self.cpf = documento_cpf
        else:
            raise ValueError(120 * '-' +
                             "\nCpf informado não é valido" + '\n' + 120 * '-' + '\n')

    def cpf_eh_valido(self, documento_cpf):
        if len(documento_cpf) == 11:
            return True
        else:
            return False

    def cria_mascara_cpf(self, cpf):
        if len(cpf) < 11:
            cpf = cpf.zfill(11)
        mascara_cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        return mascara_cpf

    def retira_mascara_cpf(self, cpf):
        cpf = re.sub('[^0-9]', '', cpf)
        return cpf


class Estrutura_email:
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    def verifica(self, email):
        if (re.search(self.regex, email)):
            return True
        else:
            raise ValueError(120 * '-' +
                             "\nE-mail informado não é valido" + '\n' + 120 * '-' + '\n')
