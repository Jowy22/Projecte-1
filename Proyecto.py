#1 oros, 2 copas, 3 bastos i 4 espadas
mazo=[
[(1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),
        (6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,0.5),
        (11,1,0.5),(12,1,0.5)],

[(1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),
        (6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,0.5),
        (11,2,0.5),(12,2,0.5)],

[(1,3,1),(2,3,2),(3,3,3),(4,3,4),(5,3,5),
        (6,3,6),(7,3,7),(8,3,8),(9,3,9),(10,3,0.5),
        (11,3,0.5),(12,3,0.5)],

[(1,4,1),(2,4,2),(3,4,3),(4,4,4),(5,4,5),
        (6,4,6),(7,4,7),(8,4,8),(9,4,9),(10,4,0.5),
        (11,4,0.5),(12,4,0.5)]
]
import random
maximo = 0
participantes = 0
jugadores = []
total_puntos = 0
flg_menu0 = False
opc_menu0 = 0
menu_principal = True

maximo = int(input("Cuantos jugadores jugaran?\n"))
while participantes != maximo:
        jugadores.append(input("Jugador : "))
        participantes = participantes+1
        print(jugadores)
for i in range(participantes):
        palo = (random.choice(mazo))
        carta = (random.choice(palo))
        print(f"{jugadores[i]} tiene {carta[2]} puntos")
        total_puntos = 0
        total_puntos = carta[2]+total_puntos
        flg_menu0 = False
        while menu_principal:
            opc_menu0 = 0
            while not flg_menu0:
                    while not (opc_menu0 == 1 or opc_menu0 == 2):
                            opc_menu0 = int(input("1) Pedir carta\n2) Plantarse\n"))
                    if (opc_menu0 == 1):
                            palo = (random.choice(mazo))
                            carta = (random.choice(palo))
                            total_puntos = carta[2] + total_puntos
                            print(f"{jugadores[i]} tiene {carta[2]} puntos")
                            print(total_puntos)
                            if(total_puntos > 7.5):
                                    print("TE HAS PASADO DE 7.5")
                                    flg_menu0 = True
                                    break
                            break
                    if (opc_menu0 == 2):
                            print(f"Puntos de {jugadores[i]}: {total_puntos}")
                            puntos_totales1 = total_puntos
                            flg_menu0 = True
                            break
            if (flg_menu0 == True):
                    break

        i = i+1