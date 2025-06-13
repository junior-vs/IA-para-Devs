import unittest
from investimentos.investimentos import (
    calcular_retorno_investimento,
    calcular_taxa_retorno,
    calcular_juros_compostos,
    converter_taxa_anual_para_mensal,
    calcular_cagr
)

class TestInvestimentos(unittest.TestCase):
    def test_calcular_retorno_investimento(self):
        self.assertAlmostEqual(calcular_retorno_investimento(1000, 10, 2), 1210.0, places=2)
        self.assertAlmostEqual(calcular_retorno_investimento(500, 5, 3), 578.81, places=2)

    def test_calcular_taxa_retorno(self):
        self.assertAlmostEqual(calcular_taxa_retorno(1000, 1200), 20.0, places=2)
       

    def test_calcular_juros_compostos(self):
        self.assertAlmostEqual(calcular_juros_compostos(1000, 10, 2), 1210.0, places=2)
        self.assertAlmostEqual(calcular_juros_compostos(500, 5, 3), 578.81, places=2)

    def test_converter_taxa_anual_para_mensal(self):
        self.assertAlmostEqual(converter_taxa_anual_para_mensal(12), 0.9489, places=3)
        self.assertAlmostEqual(converter_taxa_anual_para_mensal(24), 1.8087, places=3)

    def test_calcular_cagr(self):
        self.assertAlmostEqual(calcular_cagr(1000, 1210, 2), 10.0, places=2)
        self.assertAlmostEqual(calcular_cagr(500, 578.81, 3), 5.0, places=2)

if __name__ == '__main__':
    unittest.main()
