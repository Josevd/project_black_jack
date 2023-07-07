import random

def crea_segmento(): #crea un segmento del deck osea las cartas del 2 al As de un solo simbolo
    segmento=[]
    for x in range(2,10):
        segmento.append(x)

    for x in range(4):
        segmento.append(10)
    segmento.append(11)
    return segmento

def crea_deck(): #crea el deck repitiendo el metodo crea segmento 4 veces
    deck=[]
    for x in range(4):
        deck+=crea_segmento()
    mezclar(deck)
    return deck

def aleatorio(): #numero aleatorio entre 1 y 52 pero como las listas empiezan en 0 se cambia a 0, 51
    return random.randint(0, 51)

def mezclar(deck):
    random.shuffle(deck)

def saca_carta(deck):
    global index  #Saca una carta de adelante para atras y la remplaza por un 0
    sale=-1
    if index < 52:
        sale=deck[index]
        deck[index]=0
        index += 1
    return sale


index = 0    #si lo tienen que poner
cartas=crea_deck()

pj1=saca_carta(cartas)
pj2=saca_carta(cartas)

#print("Jugador 1: ",pj1,'        ',"Jugador 2: ",pj2)

pj1=saca_carta(cartas)
pj2=saca_carta(cartas)

##print("Jugador 1: ",pj1,'        ',"Jugador 2: ",pj2)


"""Natalia"""

def calcular_puntos(pj1, pj2):
    if pj1 == 21:
        return 6
    elif pj1 == pj2 == 21:
        return 3
    elif 17 <= pj1 <= 20 and pj1 > pj2:
        return 2
    elif pj1 < 17 and pj1 > pj2:
        return 1
    else:
        return 0

"""Natalia_FIN"""

"""SEBASTIAN """

def preguntar_valor_as():
    while True:
        respuesta = input("¿Deseas asignarle un valor de 1 o 11 al As? Ingresa '1' o '11': ")
        if respuesta == '1' or respuesta == '11':
            return int(respuesta)
        else:
            print("Respuesta inválida. Por favor, ingresa '1' o '11'.")

def imprimir_suma(pj1, pj2):
    print("Black Jack")
    print()
    suma_pj1 = sum(pj1)
    suma_pj2 = sum(pj2)
    print("             Cartas")
    print()
    print("Jugador 1:", pj1[0], "     Jugador 2:", pj2[0])
    print("Jugador 1:", pj1[1], "     Jugador 2:", pj2[1])
    #print("Total:", suma_pj1, "         Total:", suma_pj2)
    
    
    if 11 in pj1:  # Verificar si hay un As en las cartas del jugador 1
        indice_as = pj1.index(11)
        valor_as = preguntar_valor_as()
        pj1[indice_as] = valor_as
        suma_pj1 = sum(pj1)  # Actualizar el total del jugador 1
    print("Total:", suma_pj1, "         Total:", suma_pj2)
    print()

    if 11 in pj2:  # Verificar si hay un As en las cartas del jugador 2
        indice_as = pj2.index(11)
        valor_as = preguntar_valor_as()
        pj2[indice_as] = valor_as
        suma_pj2 = sum(pj2)  # Actualizar el total del jugador 2
    print("Total:", suma_pj1, "         Total:", suma_pj2)
    print()



""
pj1 = [saca_carta(cartas), saca_carta(cartas)]
pj2 = [saca_carta(cartas), saca_carta(cartas)]

imprimir_suma(pj1, pj2)

puntos_pj1 = calcular_puntos(sum(pj1), sum(pj2))
puntos_pj2 = calcular_puntos(sum(pj2), sum(pj1))

print()
print("Puntos obtenidos jugador 1:", puntos_pj1)
print("Puntos obtenidos jugador 2:", puntos_pj2)

"""SEBASTIAN_Fin"""




"""---------------------------pruebas-----------------------
index = 0
deck=crea_deck()
print(deck)
print(saca_carta(deck))  

print(deck)
print(saca_carta(deck))
print(deck)
print(saca_carta(deck))
print(deck)
print(saca_carta(deck))
print(deck)
print(saca_carta(deck))
""" 