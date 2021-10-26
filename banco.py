from utils.utils import deletar_ultimas_linhas, limpar_tela
from models.conta import Conta

def inicar_banco() -> None:
    conta = Conta(novo=False)
    conta.resgatar_contas_cadastradas()

def criar_conta() -> None:
    print('\n*********** Nova Conta ***********\n')
    conta = Conta(novo = True)
    conta.nome = input('Nome: ')
    conta.email = input('E-mail: ')
    conta.cpf = input('CPF (nnn.nnn.nnn-nn): ')
    conta.data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
    conta.salvar()
    input('\nConta cadastrada com sucesso! Tecle algo para voltar ao menu principal... ')

def listar_contas() -> None:
    conta = Conta(novo = False)
    conta.exibir_dados_contas()
    input('\nTecle algo para voltar ao menu principal... ')

def efetuar_deposito() -> None:
    conta = Conta(novo = False)
    print('\n*********** Deposito ***********\n')

    if Conta.contas:
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if conta.existe_conta(num_conta):
            valor_dep = input("Informe o valor do deposito R$: ")
            conta.depositar(valor_dep)
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def efetuar_saque():
    pass

def efetuar_transferencia():
    pass

def menu() -> bool:
    inicar_banco()

    print(f'Selecione uma opção abaixo:')
    print('---------------------------\n'
          '0 - Sair\n'
          '1 - Criar conta\n'
          '2 - Listar contas\n'
          '3 - Efetuar deposito\n'
          '4 - Efetuar saque\n'
          '5 - Efetuar transferencia\n'
          '--------------------------')

    while True:
        #Valida opcao do Menu
        try:
            opcao = int(input())
        except ValueError:
            print('Opcao invalida!\n')
            deletar_ultimas_linhas(qtde_linhas=2, espera=2)
        else:
            if (opcao < 0) or (opcao > 6):
                print('Menu nao contem essa opcao! Tente novamente...')
                deletar_ultimas_linhas(qtde_linhas=2, espera=2)
            else:
                limpar_tela()
                break
    #Sair
    if opcao == 0:
        return False

    #Criar conta ---------------------------------------------------------------------------
    elif opcao == 1:
        limpar_tela()
        criar_conta()
    #Listar contas -------------------------------------------------------------------------
    elif opcao == 2:
        limpar_tela()
        listar_contas()
    #Efetuar deposito ----------------------------------------------------------------------
    elif opcao == 3:
        limpar_tela()
        efetuar_deposito()
    #Efetuar saque -------------------------------------------------------------------------
    elif opcao == 4:
        efetuar_saque()
    #Efetuar transferencia------------------------------------------------------------------
    elif opcao == 5:
        efetuar_transferencia()
    return True

def main():
    continua = True
    print('### BEM-VINDO AO BANCO ###\n')

    while continua:
        limpar_tela()
        continua = menu()

if __name__ == "__main__":
    main()