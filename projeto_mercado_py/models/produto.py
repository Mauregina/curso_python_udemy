import json, os
from utils.utils import deleta_ultimas_linhas

class Produto:

    arquivo = 'utils/produtos.json'

    def __init__(self, novo=None):
        if novo:
            self._cod_produto = self.gerar_codigo()

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        while True:
            if len(descricao) == 0:
                print('Descricao deve ser informada! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                descricao = input('Descrição: ')
            elif len(descricao) > 20:
                print('Descricao deve ter no maximo 20 caracteres! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                descricao = input('Descrição: ')
            else:
                break

        self._descricao = descricao.lower()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        while True:
            try:
                flt_valor = float(valor)
            except:
                print('Valor informado deve ser numerico! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                valor = input('Valor: ')
            else:
                if flt_valor == 0:
                    print('Valor deve ser maior que zero! Tente novamente...')
                    deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor = input('Valor: ')
                else:
                    break

        self._valor = valor

    def gerar_codigo(self) -> int:
        if os.path.isfile(self.arquivo):
            lista_produtos = json.load(open(self.arquivo))
            return lista_produtos[-1]['_cod_produto'] + 1
        else:
            return 1

    def salvar(self):
        if os.path.isfile(self.arquivo):
            lista_produtos = json.load(open(self.arquivo))
        else:
            lista_produtos = []
        lista_produtos.append(self.__dict__)
        with open(Produto.arquivo, 'w+') as f:
            json.dump(lista_produtos, f)

    def listar_produtos(self) -> bool:
        if os.path.isfile(self.arquivo):
            lista_produtos = json.load(open(self.arquivo))
            print("\n---------- PRODUTOS DISPONIVEIS ----------")
            for i in lista_produtos:
                print(f'{str(i["_cod_produto"]).zfill(4)} {i["_descricao"].capitalize().ljust(20)} Valor R$ {i["_valor"]}')
            print('------------------------------------------')
            return True
        else:
            print('\nNao ha produtos cadastrados!')
            return False
