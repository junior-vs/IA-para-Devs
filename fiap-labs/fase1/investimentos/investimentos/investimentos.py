def calcular_retorno_investimento(investimento_inicial, taxa_juros, anos):
    """
    Calcula o retorno de um investimento com base no valor inicial,
    taxa de juros anual e número de anos.

    :param investimento_inicial: Valor inicial do investimento
    :param taxa_juros: Taxa de juros anual (em porcentagem) ex: 20
    :param anos: Número de anos do investimento
    :return: Valor final do investimento após os anos
    """
    return investimento_inicial * ((1 + taxa_juros / 100) ** anos)


def calcular_taxa_retorno(investimento_inicial, valor_final):
    """
    Calcula a taxa de retorno de um investimento.

    :param investimento_inicial: Valor inicial do investimento
    :param valor_final: Valor final do investimento após os anos
    :param anos: Número de anos do investimento
    :return: Taxa de retorno anual (em porcentagem)
    """
    return (valor_final - investimento_inicial) / investimento_inicial * 100


def calcular_juros_compostos(investimento_inicial, taxa_juros, periodo):
    """
    Calcula o montante final de um investimento com juros compostos.

    :param investimento_inicial: Valor inicial do investimento
    :param taxa_juros: Taxa de juros anual (em porcentagem) ex: 20
    :param anos: Número de anos do investimento
    :return: Montante final do investimento após os anos
    """
    return investimento_inicial * ((1 + taxa_juros / 100) ** periodo)


def converter_taxa_anual_para_mensal(taxa_anual):
    """
    Converte uma taxa de juros anual para mensal.

    :param taxa_anual: Taxa de juros anual (em porcentagem) ex: 20
    :return: Taxa de juros mensal (em porcentagem)
    """
    return ((1 + taxa_anual / 100) ** (1 / 12) - 1) * 100


def calcular_cagr(investimento_inicial, investimento_retorno, periodo):
    """
    Calcula a CAGR (Taxa Anual de Retorno) de um investimento.

    :param investimento_inicial: Valor inicial do investimento
    :param investimento_retorno: Valor final do investimento após o período
    :param periodo: Número de anos do investimento
    :return: CAGR (em porcentagem)
    """
    return ((investimento_retorno / investimento_inicial) ** (1 / periodo) - 1) * 100
