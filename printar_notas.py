#Funçao que recebe a quantidade de notas necessárias
#para sacar o dinheiro solicitado.

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