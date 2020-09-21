import enemigo
import random
import tablero
import jugador
import os
import time

def modo():
    juego={}
    elegido = False
    while elegido == False:
        os.system('cls')
        print("BIENVENIDO A ESTE JUEGO")
        print("DEBES ELEGIR LA DIFICULTAD")
        print("1 - FACIL")
        print("2 - NORMAL")
        print("3 - DIFICIL")
        eleccion=input("->  ")

        if eleccion == "1":
            listaEnemigos = generarEnemigos(10,1)
            juego["tablero"]=tablero.Tablero(6,6,jugador.Jugador([6,6]),listaEnemigos)
            juego["curas"]=6
            juego["tablero"].posicionarJugador(juego["tablero"].getJugador())
            juego["tablero"].posicionarEnemigos(juego["tablero"].getEnemigos())
            juego["tablero"].posicionarCuras(juego["curas"])
            elegido = True
        elif eleccion == "2":
            listaEnemigos = generarEnemigos(18,2)
            juego["tablero"]=tablero.Tablero(7,7,jugador.Jugador([7,7]),listaEnemigos)
            juego["curas"]=8
            juego["tablero"].posicionarJugador(juego["tablero"].getJugador())
            juego["tablero"].posicionarEnemigos(juego["tablero"].getEnemigos())
            juego["tablero"].posicionarCuras(juego["curas"])
            elegido = True
        elif eleccion == "3":
            listaEnemigos = generarEnemigos(25,3)
            juego["tablero"]=tablero.Tablero(8,8,jugador.Jugador([8,8]),listaEnemigos)
            juego["curas"]=10
            juego["tablero"].posicionarJugador(juego["tablero"].getJugador())
            juego["tablero"].posicionarEnemigos(juego["tablero"].getEnemigos())
            juego["tablero"].posicionarCuras(juego["curas"])
            elegido = True

    return juego


def generarEnemigos(cantidad, dificultad):
    lista = []
    for i in range(cantidad):
        enemy = enemigo.Enemigo()
        if dificultad == 1:
            enemy.setAtaque(random.randint(1,6))
            enemy.setVida(random.randint(1,12))
            lista.append(enemy)
        elif dificultad == 2:
            enemy.setAtaque(random.randint(2,8))
            enemy.setVida(random.randint(3,15))
            lista.append(enemy)
        elif dificultad == 3:
            enemy.setAtaque(random.randint(4,11))
            enemy.setVida(random.randint(6,20))
            lista.append(enemy)
    return lista


def instrucciones():
    print("JUEGO PARA JUGADORES QUE QUIEREN JUGAR VERSION ALFA 1.1\n\nEL JUEGO CONSTA 3 NIVELES: FACIL, NORMAL Y DIFICIL\n")
    print("POR CADA NIVEL, TIENES DISTINTA CANTIDAD DE ENEMIGOS Y CURAS\nSOLO TIENES 5 VIDAS")
    print("\nTU: O")
    print("ENEMIGO: ☻")
    print("CURA: +")
    print("META: ▼\n")
    print("TEN CUIDADO, A MAYOR NIVEL, LOS ENEMIGOS ATACAN MAS FUERTE\n")
    print("MIENTRAS MAS ENEMIGOS DERROTES, MAYOR DAÑO PUEDES LLEGAR A HACER\n")
    time.sleep(2.5)

    print("CADA VEZ QUE PASES POR UNA CURA, SE TE REGENERARA 10 DE VIDA, HASTA MAX. 25")
    print("SI TE QUEDAS SIN VIDA, VOLVERAS AL INICIO CON TU VIDA RESTAURADA AL MAXIMO\n")

    time.sleep(2.5)

    print("EL JUEGO TERMINA UNA VEZ QUE DERROTAS A TODOS LOS ENEMIGOS")
    print("Y LLEGAS A LA META '▼', O CUANDO TE QUEDAS SIN VIDAS\n\n")
    print("BUENA SUERTE!!")
    print("PRESIONA [ENTER] PARA CONTINUAR")
