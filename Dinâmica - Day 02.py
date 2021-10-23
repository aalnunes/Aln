import  math

gravidade = 9.81
beta = 1.589

variacao_alfa = range(15,76,1)

def distancia(a, b):
    lista = []
    lista_distancia =[]
    lista_alfa= []
    lista_velocidade = []
    lista_final = []
    for i in b:
        x = math.tan(math.radians(i)) * (2 * (a ** 2) * (math.cos(math.radians(i)) ** 2)) / (gravidade * beta)
        dicionario = {'alcance': x, 'alfa': i, 'velocidade': a}
        lista.append(dicionario)
        lista_distancia.append(x)
        lista_alfa.append(i)
        lista_velocidade.append(a)
        maior = (max(lista_distancia))
    ind = lista_distancia.index(maior)
    ind_alfa = lista_alfa.index(ind)
    print('A maior distancia para velocidade {} é {} com um alfa de "XX"'.format(a, maior))
    ###Infelizmente não consegui percorrer o indice do alfa.



velocidade = 250
distancia(velocidade,variacao_alfa)

velocidade = 300
distancia(velocidade,variacao_alfa)

velocidade = 350
distancia(velocidade,variacao_alfa)