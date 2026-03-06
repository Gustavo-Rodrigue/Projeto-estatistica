
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados () :
    pass

def calcular_media(dados_limpos): #Colocar a lista (dados_limpos)
    soma = sum(dados_limpos)
    quantidade = len(dados_limpos)
    media = soma / quantidade
    return media

def calcular_mediana () :
    pass

def calcular_variancia () :
    pass

def obter_extremos () :
    pass

dados = limpar_dados ( dados_sujos )

print ( f" Dados processados : { dados }")

print("Função media verificado por: Felipe")