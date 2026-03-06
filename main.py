
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados (dados) :
    dados_limpos = []
    for i in range(len(dados)):
        if type(dados[i]) == int or type(dados[i]) == float:
            dados_limpos.append(dados[i])
        else:
            continue
    return dados_limpos

def calcular_media(dados_limpos): #Colocar a lista (dados_limpos)
    soma = sum(dados_limpos)
    quantidade = len(dados_limpos)
    media = soma / quantidade
    return media

def calcular_mediana () :
    pass

def calcular_variancia () :
    pass

def obter_extremos (dados) :
    menor = min(dados)
    maior = max(dados)
    return menor, maior

dados = limpar_dados ( dados_sujos )
menor, maior = obter_extremos(dados)
media = calcular_media(dados)

print ( f" Dados processados : { dados }")
print(f"Extremo menor: {menor} ")
print(f"Extremo maior: {maior} ")
print(f"A média dos dados é: {media}")

print ("Verificado por : Gustavo(owner)")
print("Verificado por: Gustavo de Farias")
print("Função media verificado por: Felipe")
