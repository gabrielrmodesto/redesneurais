# passo 3 inicializar os pesos dos valores entre -1 e +1
# passo 4 loop treinamento
# for(t=1;t<=150;i++) selecionar um par de treino
#   linha = aleatorio()%150
def main():
    #passo 1 leitura
    try:
        file = open('dataset_iris.csv', 'r')
    except IOError as erro:
        print("Erro na leitura %s" % erro)

    dados[][]
    dados_l = []
    dados_c = []
    classe =[]
    j=0

    for linha in range(150):
        for coluna in range(4):
            dados_l.append(linha)
            dados_c.append(coluna)
        dados[dados_l][dados_c]  

    print(dados)

    file.close()
    print(classe)
    #passo 2 altera valores classe
    for i in range(1,151):
        if classe != 1:
            classe[i] = -1

    print(classe)
        
