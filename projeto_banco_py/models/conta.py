import json, os, re
from utils.utils import deletar_ultimas_linhas, limpar_tela

class Conta:
    arquivo = 'utils/contas.json'
    contas = []

    def __init__(self):
        self._num_conta: int = self.gerar_num_conta()
        self._saldo: float = 0.0

# Getters e setter (inicio) --------------------------------------------------------------------------------------------
    @property
    def num_conta(self) -> int:
        return self._num_conta

    @num_conta.setter
    def num_conta(self, num_conta: int):
        self._num_conta = num_conta

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        while True:
            if len(nome) == 0:
                print('Nome deve ser informado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                nome = input('Nome: ')
            elif len(nome) > 20:
                print('Nome deve ter no maximo 20 caracteres! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                nome = input('Nome: ')
            else:
                break
        self._nome = nome.lower()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        while True:
            if len(email) == 0:
                print('E-mail deve ser informado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                email = input('E-mail: ')
            elif len(email) > 20:
                print('E-mail deve ter no maximo 20 caracteres! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                email = input('E-mail: ')
            elif '@' not in email:
                print('E-mail invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                email = input('E-mail: ')
            else:
                break
        self._email = email.lower()

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str):
        while True:
            if len(cpf) == 0:
                print('CPF deve ser informado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                cpf = input('CPF (nnn.nnn.nnn-nn): ')
            elif not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                print('CPF invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                cpf = input('CPF (nnn.nnn.nnn-nn): ')
            elif self.existe_cpf_cadastrado(cpf):
                print('CPF ja cadastrado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                cpf = input('CPF (nnn.nnn.nnn-nn): ')
            else:
                break
        self._cpf = cpf

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        while True:
            if len(data_nascimento) == 0:
                print('Data de nascimento deve ser informado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
            elif not re.match(r'\d{2}\/\d{2}\/\d{4}', data_nascimento):
                print('Data de nascimento inv??lida! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
            else:
                break
        self._data_nascimento = data_nascimento

# Getters e setter (fim) -----------------------------------------------------------------------------------------------

    def gerar_num_conta(self) -> int:
        if Conta.contas:
            return Conta.contas[-1]['_num_conta'] + 1
        else:
            return 1

    @classmethod
    def resgatar_contas_cadastradas(cls):
        if os.path.isfile(cls.arquivo):
            cls.contas = json.load(open(cls.arquivo))

    @classmethod
    def exibir_dados_contas(cls) -> None:
        if cls.contas:
            print('\n*********** Lista de Contas ***********\n')

            for i in cls.contas:
                print(f'{i["_nome"].title().ljust(20)} \nConta = {str(i["_num_conta"]).zfill(4)} \nSaldo R$ {i["_saldo"]}')
                print('--------------------')
        else:
            print('\nNao ha contas cadastradas!')

    @classmethod
    def exibir_dados_conta_especifica(cls, num_conta = None) -> None:
        if cls.contas:
            if num_conta is None:
                pass
                # dados_conta = list(filter(lambda i: i['_num_conta'] == self._num_conta, Conta.contas))
            else:
                dados_conta = list(filter(lambda i: i['_num_conta'] == num_conta, cls.contas))
            print(f'{dados_conta[0]["_nome"].title().ljust(20)} \nConta = {str(dados_conta[0]["_num_conta"]).zfill(4)} \nSaldo R$ {dados_conta[0]["_saldo"]}\n')

    def salvar(self) -> None:
        Conta.contas.append(self.__dict__)
        with open(Conta.arquivo, 'w+') as f:
            json.dump(Conta.contas, f)

    @classmethod
    def depositar(cls, num_conta: int, valor: str) -> None:
        #Continua no loop enquanto informar um valor invalido
        while True:
            try:
                f_valor = float(valor)
            except:
                print('Valor invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                valor = input("Informe o valor do deposito R$: ")
            else:
                if f_valor > 1000.00:
                    print('Valor maximo permitido por deposito ?? de R$ 1.000! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input("Informe o valor do deposito R$: ")
                elif f_valor < 5.0:
                    print('Valor minimo permitido por deposito ?? de R$ 5.00! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input("Informe o valor do deposito R$: ")
                else:
                    break
        
        #Efetua DEPOSITO

        # Recupera linha da lista onde esta conta onde sera feito deposito
        linha = list(index for index, conta in enumerate(cls.contas) if conta["_num_conta"] == num_conta)[0]

        # Soma saldo atual com valor deposito
        cls.contas[linha]["_saldo"] += f_valor

        with open(cls.arquivo, 'w') as f:
            json.dump(Conta.contas, f)
        #---------------------------------------------------------------------------------------------------------------

    @classmethod
    def sacar(cls, num_conta: int, valor: str) -> None:
        # Continua no loop enquanto informar um valor invalido
        while True:
            try:
                f_valor = float(valor)
            except:
                print('Valor invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                valor = input("Informe o valor do saque R$: ")
            else:
                if f_valor > 1000:
                    print('Valor maximo permitido por saque ?? de R$ 1.000! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input("Informe o valor do saque R$: ")
                elif f_valor < 5:
                    print('Valor minimo permitido por saque ?? de R$ 5.00! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input("Informe o valor do saque R$: ")
                elif not cls.existe_saldo_suficiente(num_conta, f_valor):
                    print('Saldo insuficiente! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input("Informe o valor do saque R$: ")
                else:
                    break

        # Efetua SAQUE--- ----------------------------------------------------------------------------------------------

        # Recupera linha da lista onde esta conta onde sera feito saque
        linha = list(index for index, conta in enumerate(cls.contas) if conta["_num_conta"] == num_conta)[0]

        # Subtrai saldo atual com valor saque
        cls.contas[linha]["_saldo"] -= f_valor

        with open(Conta.arquivo, 'w') as f:
            json.dump(cls.contas, f)
        #---------------------------------------------------------------------------------------------------------------

    def existe_cpf_cadastrado(self, cpf: str) -> bool:
        if Conta.contas:
            return any(i['_cpf'] == cpf for i in Conta.contas)
        else:
            return False

    @classmethod
    def existe_saldo_zerado(cls, num_conta: int) -> bool:
        if Conta.contas:
            return any((i['_num_conta'] == num_conta and i['_saldo'] == 0.0) for i in cls.contas)
        else:
            return False

    @classmethod
    def existe_saldo_suficiente(cls, num_conta: str, valor: float) -> bool:
        if cls.contas:
            return any((i['_num_conta'] == num_conta and i['_saldo'] >= valor) for i in cls.contas)
        else:
            return False

    @classmethod
    def existe_conta(cls, num_conta: str) -> bool:
        encontrou = False

        #Continua no loop enquanto nao informar conta existente ou digitar 0
        while (not encontrou) and (num_conta != '0'):
            try:
                int_num_conta = int(num_conta)
            except:
                print('Numero de conta invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")
            else:
                if any(i['_num_conta'] == int_num_conta for i in cls.contas):
                    encontrou = True
                else:
                    print('Numero de conta n??o existente! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        return encontrou