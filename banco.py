from utils.utils import deleta_ultimas_linhas, limpar_tela

def cria_conta():
    pass

def lista_contas():
    pass

def efetua_saque():
    pass

def efetua_deposito():
    pass

def efetua_transferencia():
    pass

def menu() -> bool:
    print(f'Selecione uma opção abaixo:')
    print('---------------------------\n'
          '0 - Sair\n'
          '1 - Criar conta\n'
          '2 - Listar contas\n'
          '3 - Efetuar saque\n'
          '4 - Efetuar deposito\n'
          '5 - Efetuar transferencia\n'
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

    #Criar conta ------------------------------------------------------------------------------
    elif opcao == 1:
        cria_conta()
    #Listar contas ----------------------------------------------------------------------------
    elif opcao == 2:
        lista_contas()
    #Efetuar saque ----------------------------------------------------------------------------
    elif opcao == 3:
        efetua_saque()
    #Efetuar deposito -------------------------------------------------------------------------
    elif opcao == 4:
        efetua_deposito()
    #Efetuar transferencia---------------------------------------------------------------------
    elif opcao == 5:
        efetua_transferencia()
    return True

def main():
    continua = True
    print('### BEM-VINDO AO BANCO ###\n')

    while continua:
        limpar_tela()
        continua = menu()

if __name__ == "__main__":
    main()