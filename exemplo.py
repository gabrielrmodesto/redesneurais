import csv

file = csv.reader(open('dataset_iris.csv'), delimiter=',')

dado = []

for [x1,x2,x3,x4,classe] in file:
	#print(x1,x2,x3,x4,classe)
	if classe is not '1':
		classe = '-1'

	print(classe)