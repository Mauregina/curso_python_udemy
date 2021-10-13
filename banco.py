from utils.utils import deleta_ultimas_linhas, limpa_tela
from models.conta import Conta

def cria_conta():
    conta = Conta(novo = True)
    conta.nome = input('Nome: ')
    conta.email = input('E-mail: ')
    conta.cpf = input('CPF (nnn.nnn.nnn-nn): ')
    conta.data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
    conta.salvar()

def lista_contas():
    conta = Conta(novo = False)
    conta.listar_contas()
    input('\nTecle algo para voltar ao menu principal... ')

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
                limpa_tela()
                break
    #Sair
    if opcao == 0:
        return False

    #Criar conta ------------------------------------------------------------------------------
    elif opcao == 1:
        limpa_tela()
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
        limpa_tela()
        continua = menu()

if __name__ == "__main__":
    main()