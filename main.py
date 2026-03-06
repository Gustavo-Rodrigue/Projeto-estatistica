
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

def obter_extremos (dados) :
    menor = min(dados)
    maior = max(dados)
    return menor, maior

dados = limpar_dados ( dados_sujos )
menor, maior = obter_extremos(dados)
media = calcular_media(dados)
variancia = calcular_variancia(dados_sujos)

print ( f" Dados processados : { dados }")
print(f"Extremo menor: {menor} ")
print(f"Extremo maior: {maior} ")
print(f"A média dos dados é: {media}")
print("Variancia: ", variancia)

print ("Verificado por : Gustavo(owner)")
print("Verificado por: Gustavo de Farias")
print("Função media verificado por: Felipe")
print("Verificado por: Thomás Stoianov")
