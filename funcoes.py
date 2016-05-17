# -*- coding: Latin-1 -*-
import operator

def verificarSimeria(conjuntos):#funcao criada para verificar se há simetria no conjunto sorteado

# Cada elemnto da variavel "conjuntos" e conparada com todos eles. Porem o valor que e selecionado para
#        ser comparado com todos não e comparada com ele mesmo.
#    Assim a cadas simetria adiciono mais um no contador(contSimetria). Se o valor do contador for igua a o
#        numeros de elentos da lista conjuntos o conjunto e simetrico

    contSimetria = 0
    for n in conjuntos:
        for x in conjuntos:
            if (all(map(operator.eq, n, x))) == 0:
                h = n[0] == x[1] and n[1] == x[0]
                if h == 1:
                    #print type(contSimetria)
                    contSimetria+=1
                    break
      
    if len(conjuntos)==contSimetria:
        return 1
    else:
        return 0

def parteSimetrica(confuntos): #selecionando a parte simetrica do conjuntos
#Apenas verifico se a parte e simetrica se for adiciono em uma lista 
#
#
    listaSimetrica=[]
    for n in confuntos:
        for x in confuntos:
            if (all(map(operator.eq, n, x))) == 0:
                h = n[0] == x[1] and n[1] == x[0]
                if h == 1:
                    if (n in listaSimetrica)==0:
                        listaSimetrica.append(n)
                        listaSimetrica.append(x)
    return listaSimetrica
     
def ordenar (lista,texto):
    lista.sort(key=lambda x:(x[0],x[1]))
    for n in lista:
        texto += '\n{0}'.format(n)
        
    return texto