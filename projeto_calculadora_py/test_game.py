import unittest
from models.calcular import Calcular

class CalcularTestes(unittest.TestCase):
    def test_gerar_valor_dificuldade_entre_1_e_9(self):
        calc = Calcular(1)
        valor = calc.gerar_valor()

        self.assertGreaterEqual(valor, 1)
        self.assertLessEqual(valor, 9)

    def test_gerar_valor_dificuldade_entre_10_e_99(self):
        calc = Calcular(2)
        valor = calc.gerar_valor()

        self.assertGreaterEqual(valor, 10)
        self.assertLessEqual(valor, 99)

    def test_gerar_valor_dificuldade_entre_100_e_999(self):
        calc = Calcular(3)
        valor = calc.gerar_valor()

        self.assertGreaterEqual(valor, 100)
        self.assertLessEqual(valor, 999)

if __name__ == '__main__':
    unittest.main