import random

class Jugador():
    def __init__(self, limites):
        self.vida = 25
        self.ataque = 8
        self.posicionAnterior = [0,0]
        self.posicion = [0,0]
        self.limites = limites
        self.vivo = True
        self.enemigosMatados = 0
        self.muertes = 5

    def curar(self):
        if self.vida + 10 >= 25:
            self.vida = 25
        else:
            self.vida += 10

    def enemigoMatado(self):
        self.enemigosMatados += 1
        if self.enemigosMatados == 4:
            self.ataque += 1
        if self.enemigosMatados == 8:
            self.ataque += 1
        if self.enemigosMatados == 12:
            self.ataque += 1
        if self.enemigosMatados == 15:
            self.ataque += 2
        if self.enemigosMatados == 18:
            self.ataque += 1
        if self.enemigosMatados == 20:
            self.ataque += 1


    def getMuertes(self):
        return self.muertes

    def quitarVida(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.matar()

    def matar(self):
        self.muertes -= 1
        
        self.vivo = False

    def revivir(self):
        self.vida=25
        self.vivo = True

    def atacar(self):
        return random.randint(1,self.ataque)

    def isVivo(self):
        return self.vivo

    def showVida(self):
        pantalla = "♥ "*self.vida
        pantalla += " ({0})".format(self.vida)
        return pantalla

    def getPosicion(self):
        return self.posicion

    def getPosicionAnterior(self):
        return self.posicionAnterior

    def setPosicion(self, posicion):
        self.posicion = posicion
        self.posicionAnterior = posicion

    def moverJugador(self, direccion):
        self.posicionAnterior=self.posicion[:]
        if direccion.lower() == 'w':
            if self.posicion[0] != 0:
                self.posicion[0] -= 1
        if direccion.lower() == 's':
            if self.posicion[0] < self.limites[0]-1:
                self.posicion[0] += 1
        if direccion.lower() == 'a':
            if self.posicion[1] != 0:
                self.posicion[1] -= 1
        if direccion.lower() == 'd':
            if self.posicion[1] < self.limites[1]-1:
                self.posicion[1] += 1

    def getInfo(self):
        return [self.vida, self.ataque, self.posicion, self.posicionAnterior]
