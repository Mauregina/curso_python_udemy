import json, os, re
from utils.utils import deleta_ultimas_linhas

class Conta:
    arquivo = 'utils/contas.json'

    def __init__(self, novo: bool):
        if novo:
            self._num_conta: int = self.gerar_num_conta()
            self._saldo: float = 0.0

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome):
        while True:
            if len(nome) == 0:
                print('Nome deve ser informado! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                nome = input('Nome: ')
            elif len(nome) > 20:
                print('Nome deve ter no maximo 20 caracteres! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
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
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                email = input('E-mail: ')
            elif len(email) > 20:
                print('E-mail deve ter no maximo 20 caracteres! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                email = input('E-mail: ')
            elif '@' not in email:
                print('E-mail invalido! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
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
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                cpf = input('CPF (nnn.nnn.nnn-nn): ')
            elif not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                print('CPF invalido! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
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
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                cpf = input('Data de nascimento (dd/mm/yyyy): ')
            elif not re.match(r'\d{2}\/\d{2}\/\d{4}', data_nascimento):
                print('Data de nascimento inválida! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
            else:
                break
        self._data_nascimento = data_nascimento

    def gerar_num_conta(self) -> int:
        if os.path.isfile(Conta.arquivo):
            lista_contas = json.load(open(self.arquivo))
            return lista_contas[-1]['_num_conta'] + 1
        else:
            return 1

    def salvar(self):
        if os.path.isfile(self.arquivo):
            lista_contas = json.load(open(self.arquivo))
        else:
            lista_contas = []
        lista_contas.append(self.__dict__)
        with open(Conta.arquivo, 'w+') as f:
            json.dump(lista_contas, f)

    def listar_contas(self):
        if os.path.isfile(self.arquivo):
            lista_contas = json.load(open(self.arquivo))
            for i in lista_contas:
                print(f'{str(i["_num_conta"]).zfill(4)} {i["_nome"].capitalize().ljust(20)} Saldo R$ {i["_saldo"]}')
            print('------------------------------------------')
        else:
            print('\nNao ha contas cadastradas!')
