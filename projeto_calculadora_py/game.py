import os
from models.calcular import Calcular

def limpar_tela():
    os.system('cls')

def jogar() -> bool:
    global pontos

    print(f'PONTOS ACUMULADOS: {pontos}')
    print('---------------\n'
          '0 - Sair\n'
          '1 - Facil\n'
          '2 - Medio\n'
          '3 - Dificil\n'
          '---------------\n')

    while True:
        try:
            dificuldade = int(input('Selecione o nível de dificuldade (1 ou 2 ou 3):\n'))
        except ValueError:
            print('Opcao invalida!\n')
        else:
            if (dificuldade < 0) or (dificuldade > 3):
                print('Menu nao contem essa opcao!\n')
            else:
                break

    limpar_tela()

    if dificuldade == 0:
        return False

    calcular = Calcular(dificuldade)
    print(f'Qual o resultado da operacao?\n{calcular.mostrar_operacao()}')

    while True:
        try:
            resultado = int(input())
        except ValueError:
            print('Valor invalido! Tente novamente: ')
        else:
            break

    ##
    # answers = ['Errou', 'Correto']
    # print(answers[calcular.checar_resultado()])
    ##

    if calcular.checar_resultado(resultado):
        print('Correto!')
        pontos+=1
    else:
        print(f'Errou! Valor correto = {calcular.resultado_correto}')


    if input("\nDigite 'S' ou 's' caso queira continuar jogando:\n").upper() == 'S':
        limpar_tela()
        return True
    else:
        print('Jogo finalizado!')
        return False

def main():
    global pontos
    pontos = 0
    continua = True
    limpar_tela()
    print('BEM-VINDO AO JOGO DESAFIOS MATEMATICOS\n')

    while continua:
        continua = jogar()

if __name__ == "__main__":
    main()
