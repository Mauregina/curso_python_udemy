import json, os
from utils.utils import deleta_ultimas_linhas

class Carrinho:
    produtos_disponiveis = {}
    carrinho = {}
    arquivo = 'utils/produtos.json'

    def inicia_compra(self):
        #Carrega dicionario com produtos disponiveis para compra
        if os.path.isfile(self.arquivo):
            lista_produtos = json.load(open(self.arquivo))
            for i in lista_produtos:
                self.produtos_disponiveis.update({i["_cod_produto"]: [i["_descricao"], i["_valor"]]})
        else:
            print('\nNao ha produtos cadastrados!')

    def adiciona_produto(self, codprod: str):
        #Continua no loop enquanto informar um codprod inexistente ou invalido
        while True:
            try:
                int_codprod = int(codprod)
            except:
                print('Valor informado deve ser numerico! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                codprod = input("Informe o codigo do produto para adiciona-lo ao carrinho: ")
            else:
                encontrou = False
                index = 0

                #Verifica se produto esta cadastrado
                while (not encontrou) and (index < len(self.produtos_disponiveis)):
                    item = self.produtos_disponiveis.get(int_codprod)
                    if item:
                        encontrou = True
                    index += 1

                if encontrou: #Adiciona produto ao carrinho
                    #Se item ja esta no carrinho, apenas incrementa qtde
                    if self.carrinho.get(int_codprod):
                        self.carrinho[int_codprod][2] += 1
                    else:
                        #adiciona novo item ao carrinho
                        item.append(1)
                        self.carrinho.update({int_codprod : self.produtos_disponiveis.get(int_codprod)})
                    break
                else:
                    print(f'Cód. produto {str(codprod).zfill(4)} nao existe! Tente novamente...')
                    deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                    codprod = input("Informe o codigo do produto para adiciona-lo ao carrinho: ")

    def lista_carrinho(self):
        for i in self.carrinho:
            print(f'{self.carrinho[i][2]} x {self.carrinho[i][0].capitalize()} R$ {self.carrinho[i][1]} = '
                  f'{round(float(self.carrinho[i][1])*int(self.carrinho[i][2]),2)}')

    def fecha_carrinho(self):
        self.lista_carrinho()
        print('-------------------------------------')
        valor_total = sum(float(self.carrinho[i][1])*int(self.carrinho[i][2]) for i in self.carrinho)
        print(f'Total a pagar R$ = {round(valor_total,2)}')
        valor_pago = input('Valor pago R$ = ')

        #Continua no loop enquanto informar um valor invalido
        while True:
            try:
                float_valor_pago = float(valor_pago)
            except:
                print('Valor invalido! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                valor_pago = input('Valor pago R$ = ')
            else:
                if float_valor_pago < valor_total:
                    print('Valor pago menor que valor total! Tente novamente...')
                    deleta_ultimas_linhas(qtde_linhas=2, espera=2)
                    valor_pago = input('Valor pago R$ = ')
                else:
                    break

        troco = float(valor_total) - float(valor_pago)
        print(f'Troco R$ = {abs(round(troco,2))}')
        print('\nVenda finalizada!')
        self.carrinho.clear() #limpa carrinho
        input('\nTecle algo para voltar ao menu principal...')