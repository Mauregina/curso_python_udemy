from random import randint


class Calcular:
    def __init__(self, dificuldade: int):
        self.__dificuldade = dificuldade
        self.__operacao = randint(1,3)
        self.__valor1 = self.gerar_valor()
        self.__valor2 = self.gerar_valor()
        self.__resultado_correto = self.calcular_operacao()

    @property
    def operacao(self) -> str:
        if self.__operacao == 1: return '+'
        elif self.__operacao == 2: return '-'
        else: return 'x'

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def resultado_correto(self) -> int:
        return self.__resultado_correto

    def gerar_valor(self) -> int:
        if self.__dificuldade == 1:
            return randint(1,9)
        elif self.__dificuldade == 2:
            return randint(10,99)
        else:
            return randint(100,999)

    def mostrar_operacao(self) -> str:
        return f'{self.valor1} {self.operacao} {self.valor2}'

    def calcular_operacao(self):
        if self.__operacao == 1: return (self.__valor1 + self.__valor2)
        elif self.__operacao == 2: return (self.__valor1 - self.__valor2)
        else: return (self.__valor1 * self.__valor2)

    def checar_resultado(self, resultado: int) -> bool:
        return self.__resultado_correto == resultado