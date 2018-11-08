import csv
import random


# for(t=1;t<=150;i++) selecionar um par de treino
#   linha = aleatorio()%150
def main():
    #passo 1 leitura
    try:
        file = csv.reader(open('dataset_iris.csv'), delimiter=',')
    except IOError as erro:
        print("Erro na leitura %s" % erro)

    lista_classe = []
    #passo 2 altera valores classe
    for [x1,x2,x3,x4,classe] in file:
        classe = int(classe)
        if classe is not 1:
            classe = -1

        print(x1,x2,x3,x4,classe)
        lista_classe.append(classe)

    # passo 3 inicializar os pesos dos valores entre -1 e +1
    lista_pesos = []
    for i in range(4):
        lista_pesos.append(random.randrange(-1,2,1))

    print(lista_pesos)

    # passo 4 loop treinamento
    
 

if __name__ == '__main__':
    main()