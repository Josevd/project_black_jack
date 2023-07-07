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

"""def aleatorio(): #numero aleatorio entre 1 y 52 pero como las listas empiezan en 0 se cambia a 0, 51
    return random.randint(0, 51)"""

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


def primer_mano(deck,player): #Saca las primeras 2 cartas de cada ronda
    for x in range(2):
        player.append(saca_carta(deck))

    return player

def siguiente_ronda(deck,player):
    player=primer_mano(deck,player)
    return player


def suma_de_puntos_por_ronda(player):
    suma=0
    for x in player:
        suma+=x
    return suma
 

def evaluacion_de_puntos(player_1_puntos,player_2_puntos,player_1,player_2):
    if(suma_de_puntos_por_ronda(player_1) == suma_de_puntos_por_ronda(player_2) == 21):
        player_1_puntos = 3
        player_2_puntos = 3
    elif(suma_de_puntos_por_ronda(player_2) == 21):
        player_1_puntos = 6
    elif(suma_de_puntos_por_ronda(player_2) == 21):
        player_2_puntos = 6
    

    return player_1_puntos, player_2_puntos


"""---------------------------pruebas-----------------------"""

index = 0    #si lo tienen que poner
player_1_puntos = 0
player_2_puntos = 0
cartas=crea_deck()

pj1=[]
print(cartas)
print(pj1)


