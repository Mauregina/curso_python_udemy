import json, os, re
from utils.utils import deletar_ultimas_linhas, limpar_tela

class Conta:
    arquivo = 'utils/contas.json'
    contas = []

    def __init__(self, novo: bool):
        if novo:
            self._num_conta: int = self.gerar_num_conta()
            self._saldo: float = 0.0

# Getters e setter (inicio) --------------------------------------------------------------------------------------------
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome):
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
    def email(self, email):
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
    def cpf(self, cpf):
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
    def data_nascimento(self, data_nascimento):
        while True:
            if len(data_nascimento) == 0:
                print('Data de nascimento deve ser informado! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
            elif not re.match(r'\d{2}\/\d{2}\/\d{4}', data_nascimento):
                print('Data de nascimento inválida! Tente novamente...')
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

    def resgatar_contas_cadastradas(self):
        if os.path.isfile(self.arquivo):
            Conta.contas = json.load(open(self.arquivo))

    def exibir_dados_contas(self) -> None:
        if Conta.contas:
            print('\n*********** Lista de Contas ***********\n')

            for i in Conta.contas:
                print(f'{i["_nome"].title().ljust(20)} \nConta = {str(i["_num_conta"]).zfill(4)} \nSaldo R$ {i["_saldo"]}')
                print('--------------------')
        else:
            print('\nNao ha contas cadastradas!')

    def exibir_dados_conta_especifica(self, num_conta: int) -> None:
        if Conta.contas:
            print('\n*********** Deposito ***********\n')
            dados_conta = list(filter(lambda i: i['_num_conta'] == num_conta, Conta.contas))
            print(f'{dados_conta[0]["_nome"].title().ljust(20)} \nConta = {str(dados_conta[0]["_num_conta"]).zfill(4)} \nSaldo R$ {dados_conta[0]["_saldo"]}\n')

    def salvar(self) -> None:
        Conta.contas.append(self.__dict__)
        with open(Conta.arquivo, 'w+') as f:
            json.dump(Conta.contas, f)

    def depositar(self, valor_dep: str) -> None:
        #Continua no loop enquanto informar um valor invalido
        while True:
            try:
                f_valor_dep = float(valor_dep)
            except:
                print('Valor invalido! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                valor_dep = input("Informe o valor do deposito R$: ")
            else:
                if f_valor_dep > 10000:
                    print('Valor maximo permitido por deposito é de R$ 10.000! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor_dep = input("Informe o valor do deposito R$: ")
                elif f_valor_dep < 5:
                    print('Valor minimo permitido por deposito é de R$ 5.00! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor_dep = input("Informe o valor do deposito R$: ")
                else:
                    break
        
        #Efetua deposito


    def existe_cpf_cadastrado(self, cpf: str) -> bool:
        if Conta.contas:
            return any(i['_cpf'] == cpf for i in Conta.contas)
        else:
            return False

    def existe_conta(self, num_conta: str) -> bool:
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
                if any(i['_num_conta'] == int_num_conta for i in Conta.contas):
                    limpar_tela()
                    self.exibir_dados_conta_especifica(int_num_conta)
                    self._num_conta = int_num_conta
                    encontrou = True
                else:
                    print('Numero de conta não existente! Tente novamente...')
                    deletar_ultimas_linhas(qtde_linhas=2, espera=2)
                    num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        return encontrou