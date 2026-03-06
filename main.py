
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

def calcular_mediana(dados):
    sorted(dados)
    m = len(dados) / 2
    if not m.is_integer(): # Se esse valor não for um int
        mCerto = int(m) #Ele transforma em int
        result = (dados[mCerto] + dados[mCerto+1]) / 2 #calcula a media desses dois
    else: result = m; pass
    return result

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
mediana = calcular_mediana(dados)

print (f"Dados processados : { dados }")
print(f"Extremo menor: {menor} ")
print(f"Extremo maior: {maior} ")
print(f"A média dos dados é: {media}")
print("Variancia: ", variancia)
print(f"A mediana destes dados é, {mediana} \n")

print ("Verificado por : Gustavo(owner)")
print("Verificado por: Gustavo de Farias")
print("Função media verificado por: Felipe")
print("Verificado por: Thomás Stoianov")
print(f"Arquivo auditado por: Matheus-Pieroni")
