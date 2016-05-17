# -*- coding: Latin-1 -*-
import sys
import itertools
import random
from funcoes import *


m = input("Digite o primeiro elemento da rela��o:") #Pegando para M(Primeiro elemento da rela��o)
n = input("Digite o ultimo elemento da rela��o:")#Pegando um valor para N(Ultimo elemento da rela��o)
q = input("Quantidade de elementos da rela��o:")#Pegando um valor para Q(quantidade de elementos da rela��o)

if m < 0 or n > 100 or q < 1 or q > 10000: #validando as variaves 
    print "Valores Invalidos!!"
    sys.exit(0)

listaNumeros = range(m, n + 1) #criando o conjunto com numeros de "m" a "n+1"
#product
listaCunjuntos = itertools.product(listaNumeros, repeat=2) #conbinando elementos de 2 em 2

lista = [] #criando uma lista  

for n in listaCunjuntos: # convertendo todos os elementos de objetos intertols para lista
    lista.append(n)
    
if q>len(lista):
    q=len(lista)

listaConjuntosorteados = random.sample(lista, q) #sorteando um numero de "q"



for elemento in listaConjuntosorteados :#mostrando elemendos sorteados
    print "{0}\n".format(elemento)

arquivoSaida = open('arquivo_saida.txt','w')#criando um arquivo

if (verificarSimeria(listaConjuntosorteados))==1: #verificando se h� simetria no conjunto sorteado 
    texto='1'
else: 
    listaSimetrica = parteSimetrica(lista) # pegando a parte simetrica do conjunto
    texto='Fecho Sim�trico=\n{'
    for x in listaSimetrica : #arrumando "string" para adcionar no arquivo 
       texto=texto + '{0},'.format(x)
       
    texto=texto + '}\n'
   
texto= texto.replace(',}','}\n 0',1) #removendo valor indesejado da "string"

texto=ordenar(listaSimetrica,texto)
arquivoSaida.writelines(texto) #escrevendo no arquivo
arquivoSaida.close() #fechando o arquivo

print texto
