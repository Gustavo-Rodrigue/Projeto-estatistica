
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados (dados_sujos) :
    pass

def calcular_media () :
    pass

def calcular_mediana () :
    pass

def calcular_variancia (dados_sujos) :
    dados = []

    for valor in dados_sujos:
        if type(valor) == int or type(valor) == float:
            dados.append(valor)

    media = sum(dados) / len(dados)

    soma = 0
    for x in dados:
        soma += (x - media) ** 2
    
    variancia = soma / len(dados)

    return variancia

def obter_extremos () :
    pass

dados = limpar_dados ( dados_sujos )

print ( f" Dados processados : { dados }")

variancia = calcular_variancia(dados_sujos)
print("Variancia: ", variancia)

print("Verificado por: Thomás Stoianov")