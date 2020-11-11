# Objetivo do projeto

Fazer um CRUD ( Create, Read, Update e Delete) de uma entidade
chamada pessoa.

**Cadastrar**

O usuário pode cadastrar pessoa, informando os seguintes
dados:
* Nome
* Cpf
* E-mail

Ao **cadastrar/editar** pessoa, o sistema deve validar as seguintes
informações:
* Nome obrigatório
* Nome deve possuir no máximo 150 caracteres
* Cpf obrigatório
* Cpf deve ser um cpf válido
* E-mail obrigatório
* E-mail deve ser um e-mail válido
* E-mail deve possuir no máximo 400 caracteres
* Cpf não pode ser duplicado, ou seja, não pode ser cadastrado
dois responsáveis com o mesmo cpf

**Remover**
* O sistema deve permitir que o usuário remova pessoas. Esta remoção
deve ser lógica, ou seja, o usuário continuará no sistema, porém você deve
utilizar uma marcação para determinar se ele foi excluído ou não.

**Consultar**

 O usuário pode consultar pessoas com os seguintes filtros:
* Cpf (formatado e não formatado)
* E-mail