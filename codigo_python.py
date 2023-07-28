#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.​
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;​
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
#uma nota de 5 e quatro notas de 1.

def printar_atm(notas_100, notas_50, notas_10, notas_5, moeda_1):
    if notas_100 > 0:
        print("Notas de 100: {}".format(notas_100))
    if notas_50 > 0:
        print("Notas de 50: {}".format(notas_50))
    if notas_10 > 0: 
        print("Notas de 10:{}".format(notas_10))
    if notas_5 > 0:
        print("Notas de 5:{}".format(notas_5))
    if moeda_1 > 0:
        print("Moedas de 1 real:{}\n".format(moeda_1))