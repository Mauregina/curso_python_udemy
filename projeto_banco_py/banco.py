from utils.utils import deletar_ultimas_linhas, limpar_tela
from models.conta import Conta

def iniciar_banco() -> None:
    Conta.resgatar_contas_cadastradas()

def criar_conta() -> None:
    print('\n*********** Nova Conta ***********\n')
    conta = Conta()
    conta.nome = input('Nome: ')
    conta.email = input('E-mail: ')
    conta.cpf = input('CPF (nnn.nnn.nnn-nn): ')
    conta.data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')
    conta.salvar()
    input('\nConta cadastrada com sucesso! Tecle algo para voltar ao menu principal... ')

def listar_contas() -> None:
    Conta.exibir_dados_contas()
    input('\nTecle algo para voltar ao menu principal... ')

def efetuar_deposito() -> None:
    print('\n*********** Deposito ***********\n')

    if Conta.contas:
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if Conta.existe_conta(num_conta):
            limpar_tela()
            int_num_conta = int(num_conta)
            print('\n*********** Deposito ***********\n')
            Conta.exibir_dados_conta_especifica(int_num_conta)

            valor = input("Informe o valor do deposito R$: ")
            Conta.depositar(int_num_conta, valor)
            limpar_tela()
            print('\n*********** Deposito ***********\n')
            Conta.exibir_dados_conta_especifica(int_num_conta)

            input('\nDeposito realizado com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def efetuar_saque() -> None:
    print('\n*********** Saque ***********\n')

    if Conta.contas:
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if Conta.existe_conta(num_conta):
            limpar_tela()
            int_num_conta = int(num_conta)
            print('\n*********** Saque ***********\n')
            Conta.exibir_dados_conta_especifica(int_num_conta)

            if Conta.existe_saldo_zerado(int_num_conta):
                print("Saque nao pode ser realizado! Motivo: saldo da conta zerado.\n")
                input("Tecle algo para voltar ao menu principal... ")
            else:
                valor = input("Informe o valor do saque R$: ")
                Conta.sacar(int_num_conta, valor)
                limpar_tela()
                print('\n*********** Saque ***********\n')
                Conta.exibir_dados_conta_especifica(int_num_conta)

                input('\nSaque realizado com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def efetuar_transferencia():
    print('\n*********** Transferencia ***********\n')

    if Conta.contas:
       # Conta ORIGEM --------------------------------------------------------------------------------------------------
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if Conta.existe_conta(num_conta):
            limpar_tela()
            int_num_conta = int(num_conta)
            print('\n*********** Transferencia ***********\n')
            print('ORIGEM')
            Conta.exibir_dados_conta_especifica(int_num_conta)

            if Conta.existe_saldo_zerado(int_num_conta):
                print("Transferencia nao pode ser realizada! Motivo: saldo da conta zerado.\n")
                input("Tecle algo para voltar ao menu principal... ")

        # Conta DESTINO ------------------------------------------------------------------------------------------------
            else:
                num_conta_destino = input("Informe o numero da conta destino (digite 0 para voltar ao menu principal): ")

                if Conta.existe_conta(num_conta_destino):
                    deletar_ultimas_linhas(qtde_linhas=1, espera=0)
                    print('DESTINO')
                    int_num_conta_destino = int(num_conta_destino)
                    Conta.exibir_dados_conta_especifica(int_num_conta_destino)

                    if int_num_conta == int_num_conta_destino:
                        print("Transferencia nao pode ser realizada! Motivo: conta origem igual a conta destino.\n")
                        input("Tecle algo para voltar ao menu principal... ")

                    # realiza TRANSFERENCIA entre contras
                    else:
                        valor = input("Informe o valor da transferencia R$: ")
                        Conta.sacar(int_num_conta, valor)
                        Conta.depositar(int_num_conta_destino, valor)
                        limpar_tela()
                        print('\n*********** Transferencia ***********\n')
                        print('ORIGEM')
                        Conta.exibir_dados_conta_especifica(int_num_conta)
                        print('DESTINO')
                        Conta.exibir_dados_conta_especifica(int_num_conta_destino)

                        input('\nTransferencia realizada com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def menu() -> bool:
    iniciar_banco()

    print(f'Selecione uma op????o abaixo:')
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