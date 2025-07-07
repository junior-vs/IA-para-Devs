import investimentos

valor_inicial = 1000
valor_final = 1500
anos = 5
taxa_anual = 6

retorno = investimentos.calcular_taxa_retorno(valor_inicial, valor_final)
print(f"Retorno do investimento: {retorno:.2f}%")

retorno_investimento = investimentos.calcular_retorno_investimento(
    valor_inicial, taxa_anual, anos
)
print(f"Retorno do investimento após {anos} anos: R$ {retorno_investimento:.2f}")

taxa = investimentos.converter_taxa_anual_para_mensal(taxa_anual)
print(f"Taxa de juros mensal equivalente a {taxa_anual}% ao ano: {taxa:.2f}%")

cagr = investimentos.calcular_cagr(valor_inicial, valor_final, anos)
print(f"CARG (Taxa Anual de Retorno): {cagr:.2f}%")
