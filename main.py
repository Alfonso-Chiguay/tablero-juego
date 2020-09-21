import enemigo
import jugador
import tablero
import juego
import os
import pelea


os.system('cls')
juego.instrucciones()
input()
os.system('cls')
game = juego.modo()
player = game["tablero"].getJugador()
enemies = game["tablero"].getEnemigos()


finDelJuego = False

while finDelJuego == False:
    game["tablero"].mostrarTablero(player)
    print('\n')
    movimiento = input("->")
    if movimiento.lower() == "x":
        os.system('cls')
        finDelJuego = True

    player.moverJugador(movimiento)
    game["tablero"].limpiarPosicion(player.getPosicionAnterior())
    isEnemy= pelea.verificarPelea(player.getPosicion(),game["tablero"].getEnemigos())
    if game["tablero"].verificarCura(player):
        player.curar()

    if isEnemy[0]:
        ganador = pelea.comenzarPelea(player, isEnemy[1])
        if ganador == True:
            game["tablero"].posicionarJugador(player)
            game["tablero"].eliminarEnemigo(isEnemy[1].getPosicion())
            player.enemigoMatado()
        else:
            player.setPosicion([0,0])            
            game["tablero"].posicionarJugador(player)
            game["tablero"].posicionarEnemigo(isEnemy[1])
            if player.muertes == 0:
                os.system('cls')
                input("MALA SUERTE, TE QUEDASTE SIN VIDAS\n===============================\nDebería darte vergüenza")
                finDelJuego = True
    else:
        game["tablero"].posicionarJugador(player)

    


    if len(game["tablero"].getEnemigos()) == 0 and player.getPosicion() == game["tablero"].getLimites():
        os.system('cls')
        
        muertes= 5-player.getMuertes()
        
        mensaje="LO CONSEGUISTE!\n\n===============================\nSolo moriste {0} veces".format(muertes)
        if muertes == 0:
            mensaje+="\nEstas al nivel de los Dioses!!!!"
        elif muertes == 1:
            mensaje+="\nEstas al nivel de los Semi-Dioses!!"
        elif muertes == 2:
            mensaje+="\nEres un mortal aventajado!"
        elif muertes == 3:
            mensaje+="\nSi estuvieras en una guerra, no me sorprendería que no regresaras a casa"
        elif muertes == 4:
            mensaje+="\nAl menos lo intentaste, pero intentarlo no es suficiente"
        print(mensaje)    
        input("Presione [ENTER] para terminar. . .")

        finDelJuego = True
    elif player.getPosicion() == game["tablero"].getLimites() and len(game["tablero"].getEnemigos()) > 0:
        player.setPosicion(player.getPosicionAnterior())
        game["tablero"].limpiarPosicion(player.getPosicionAnterior())
        input("AUN TE QUEDAN ENEMIGOS POR DERROTAR")
        game["tablero"].posicionarJugador(player)
        game["tablero"].posicionarMeta()
