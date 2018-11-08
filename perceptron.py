import csv
# passo 3 inicializar os pesos dos valores entre -1 e +1
# passo 4 loop treinamento
# for(t=1;t<=150;i++) selecionar um par de treino
#   linha = aleatorio()%150
def main():
    #passo 1 leitura
    try:
        file = csv.reader(open('dataset_iris.csv'), delimiter=',')
    except IOError as erro:
        print("Erro na leitura %s" % erro)

    dados = []
    line = []
    j = 0
    #passo 2 altera valores classe
    for [x1,x2,x3,x4,classe] in file:
        if classe is not '1':
            classe = '-1'

        print(classe)
        
if __name__ == '__main__':
    main()