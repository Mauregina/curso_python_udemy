import json
import os
from models.produto import Produto
from models.carrinho import Carrinho
from utils.utils import deleta_ultimas_linhas

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def lista_produto() -> bool:
    produto = Produto(False)
    return produto.listar_produtos()

def cadastra_produto():
    produto = Produto(True)
    print("\nNOVO PRODUTO")
    produto.descricao = input('Descrição = ')
    produto.valor = input('Valor R$ = ')
    produto.salvar()
    input('\nProduto cadastrado com sucesso! Tecle algo para voltar ao menu principal... ')

def realiza_compra():
    carrinho = Carrinho()
    carrinho.inicia_compra()

    #Continua no loop enquanto estiver cadastrando itens ao carrinho
    while True:
        codprod = input("Informe o codigo do produto para adiciona-lo ao carrinho: ")
        carrinho.adiciona_produto(codprod)
        print('\n-------------- MEU CARRINHO --------------')
        carrinho.lista_carrinho()
        
        if input('\nTecle F para fechar o pedido. Caso contrario, tecle qualquer outra tecla para continuar adionando itens ao carrinho... ').lower() == 'f':
            limpar_tela()
            print('\n---------- FINALIZAR VENDA ----------')
            carrinho.fecha_carrinho()
            break
        else:
            limpar_tela()
            lista_produto()

def menu() -> bool:
    print(f'Selecione uma opção abaixo:')
    print('---------------------------\n'
          '0 - Sair\n'
          '1 - Cadastrar Produto\n'
          '2 - Realizar Compra\n'
          '--------------------------')

    while True:
        #Valida opcao do Menu
        try:
            opcao = int(input())
        except ValueError:
            print('Opcao invalida!\n')
            deleta_ultimas_linhas(qtde_linhas=2, espera=2)
        else:
            if (opcao < 0) or (opcao > 2):
                print('Menu nao contem essa opcao! Tente novamente...')
                deleta_ultimas_linhas(qtde_linhas=2, espera=2)
            else:
                limpar_tela()
                break
    #Sair
    if opcao == 0:
        return False

    #Cadastrar produto ------------------------------------------------------------------------------
    elif opcao == 1:
        if input('\nTecle P para visualizar os produtos ja cadastrados... ').lower() == 'p':
            limpar_tela()
            lista_produto()
            cadastra_produto()
        else:
            limpar_tela()
            cadastra_produto()

    #Realizar compra ---------------------------------------------------------------------------------
    elif opcao == 2:
        limpar_tela()
        if lista_produto():
            realiza_compra()
        else:
            input('\nTecle algo para voltar ao menu principal...')

    return True

def main():
    continua = True
    print('### BEM-VINDO AO MERCADO ###\n')

    while continua:
        limpar_tela()
        continua = menu()

if __name__ == "__main__":
    main()
