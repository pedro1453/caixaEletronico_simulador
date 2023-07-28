#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.​
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;​
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
#uma nota de 5 e quatro notas de 1.
from codigo_python import *

dinheiro = int(input("Informe o valor a ser sacado: R$"))
print("Para sacar a quantia de R$ {}, será necessário:".format(dinheiro))
if dinheiro > 10 and dinheiro <= 600:
    notas_100 = int(dinheiro/100)
    notas_50 = int((dinheiro % 100)/50)
    notas_10 = int(((dinheiro % 100) % 50)/ 10)
    notas_5 = int((((dinheiro % 100) % 50) % 10)/5)
    moeda_1 = int(dinheiro - (notas_100*100 + notas_50*50 + notas_10*10 + notas_5*5))

printar_atm(notas_100, notas_50, notas_10, notas_5, moeda_1)
