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
            limpar_tela()
            conta.num_conta = int(num_conta)
            print('\n*********** Deposito ***********\n')
            conta.exibir_dados_conta_especifica()

            valor = input("Informe o valor do deposito R$: ")
            conta.depositar(valor)
            limpar_tela()
            print('\n*********** Deposito ***********\n')
            conta.exibir_dados_conta_especifica()

            input('\nDeposito realizado com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def efetuar_saque() -> None:
    conta = Conta(novo = False)
    print('\n*********** Saque ***********\n')

    if Conta.contas:
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if conta.existe_conta(num_conta):
            limpar_tela()
            conta.num_conta = int(num_conta)
            print('\n*********** Saque ***********\n')
            conta.exibir_dados_conta_especifica()

            if conta.existe_saldo_zerado():
                print("Saque nao pode ser realizado! Motivo: saldo da conta zerado.\n")
                input("Tecle algo para voltar ao menu principal... ")
            else:
                valor = input("Informe o valor do saque R$: ")
                conta.sacar(valor)
                limpar_tela()
                print('\n*********** Saque ***********\n')
                conta.exibir_dados_conta_especifica()

                input('\nSaque realizado com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

def efetuar_transferencia():
    conta = Conta(novo = False)
    print('\n*********** Transferencia ***********\n')

    if Conta.contas:
       # Conta ORIGEM --------------------------------------------------------------------------------------------------
        num_conta = input("Informe o numero da conta (digite 0 para voltar ao menu principal): ")

        if conta.existe_conta(num_conta):
            limpar_tela()
            conta.num_conta = int(num_conta)
            print('\n*********** Transferencia ***********\n')
            print('ORIGEM')
            conta.exibir_dados_conta_especifica()

            if conta.existe_saldo_zerado():
                print("Transferencia nao pode ser realizada! Motivo: saldo da conta zerado.\n")
                input("Tecle algo para voltar ao menu principal... ")

        # Conta DESTINO ------------------------------------------------------------------------------------------------
            else:
                num_conta_destino = input("Informe o numero da conta destino (digite 0 para voltar ao menu principal): ")

                if conta.existe_conta(num_conta_destino):
                    deletar_ultimas_linhas(qtde_linhas=1, espera=0)
                    print('DESTINO')
                    int_num_conta_destino = int(num_conta_destino)
                    conta.exibir_dados_conta_especifica(int_num_conta_destino)

                    if conta.num_conta == int_num_conta_destino:
                        print("Transferencia nao pode ser realizada! Motivo: conta origem igual a conta destino.\n")
                        input("Tecle algo para voltar ao menu principal... ")

                    # realiza TRANSFERENCIA entre contras
                    else:
                        valor = input("Informe o valor da transferencia R$: ")
                        conta.sacar(valor)
                        conta.num_conta = int_num_conta_destino
                        conta.depositar(valor)
                        limpar_tela()
                        print('\n*********** Transferencia ***********\n')
                        conta.num_conta = int(num_conta)
                        print('ORIGEM')
                        conta.exibir_dados_conta_especifica()
                        conta.num_conta = int_num_conta_destino
                        print('DESTINO')
                        conta.exibir_dados_conta_especifica()

                        input('\nTransferencia realizada com sucesso! Tecle algo para voltar ao menu principal... ')
    else:
        input('\nNao ha contas cadastradas! Tecle algo para voltar ao menu principal... ')

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