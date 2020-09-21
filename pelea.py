import jugador
import enemigo
import random
import os

clear=os.system('cls')

def verificarPelea(posicionJugador, listaEnemigos):
    for enemigo in listaEnemigos:
        if enemigo.getPosicion() == posicionJugador:
            return [True,enemigo]
    return [False, False]

def comenzarPelea(jugador, enemigo):
    continuar = True
    ganaJugador = False
    
    while continuar:
        
        mensaje = ""
        muerto = False
        esquivarEnemigo = random.randint(1,4)
        if esquivarEnemigo == 2:
            mensaje+="El enemigo ha esquivado el ataque\n"
        else:
            ataque = jugador.atacar()
            mensaje+="Has atacado y le quitaste {0} de vida\n".format(ataque)
            enemigo.quitarVida(ataque)
            if not enemigo.isVivo():
                mensaje+="Lo has derrotado\n"
                jugador.enemigoMatado()
                pos = jugador.getPosicion()
                ganaJugador = True
                continuar = False
                os.system('cls')
                portada(jugador,enemigo)
                input(mensaje)      
                
                break
        esquivarJugador = random.randint(1,4)
        if esquivarJugador == 3:
            mensaje+="Has esquivado el ataque"
        else:
            ataque = enemigo.atacar()
            mensaje+="Te han atacado y te hicieron {0} de daño\n".format(ataque)
            jugador.quitarVida(ataque)
            if not jugador.isVivo():
                mensaje+="Te han debilitado\n"                
                os.system('cls')
                portada(jugador,enemigo)
                muerto = True
                continuar = False
        os.system('cls')
        portada(jugador,enemigo)
        print(mensaje)   
        if muerto == True:
            jugador.revivir()   
        input()
    return ganaJugador
def portada(jugador, enemigo):
    print("Vida jugador: {0}".format(jugador.showVida()))
    print("Vida enemigo: {0}".format(enemigo.showVida()))
    print("--------------------------------------------")
