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

    dados = []
    classe = []
    line = []
    j = 0

    for line in file:
        dados_str = []
        dados_str.append(line.strip('\n').split(','))
        line = []
        for j in range(len(dados_str)):
            line.append(dados_str[j])

        dados.append(line)
        classe.append(dados_str[len(dados_str) - 1])
    file.close()

    print(classe)
    #passo 2 altera valores classe
    # for i in range(1,151):
    #     if classe != 1:
    #         classe[i] = -1

    # print(classe)
        
if __name__ == '__main__':
    main()