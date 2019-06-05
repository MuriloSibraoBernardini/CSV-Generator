import csv

#Funcoes de exemplo.
def func1():
    return 1

def func2():
    return 2

def func3():
    return 3

# Escrevendo ('w' write) na primaira linha da tabela.
f = open('/home/murilo/Documentos/GitHub/CSV-Generator/DataSet.csv', 'w') 
try:
    writer = csv.writer(f)
    # Controle da quntidade de coluna (no exemplo esta com 3).
    writer.writerow(('Caoluna_1','Coluna_2','Coluna_3'))
finally:
    f.close()

# Adicionando ('a' append) itens na tabela.
f = open('/home/murilo/Documentos/GitHub/CSV-Generator/DataSet.csv', 'a')
try:
    writer = csv.writer(f)
    # Controle da quntidade de linha (no exemplo esta com 3 linhas, 4-1=3).
    for i in range(1, 4):
        vet = []  
        # Adicionando dados na linhas da tabela, de acordo com as funcoes.      
        vet += [func1()]
        vet += [func2()]
        vet += [func3()]  
        writer.writerow((vet))
finally:
    f.close()
