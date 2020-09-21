import random

class Enemigo():
    def __init__(self):
        self.vida = 0
        self.ataque = 0
        self.posicion = [0,0]
        self.vivo = True

    def setVida(self, vida):
        self.vida=vida

    def setAtaque(self,ataque):
        self.ataque=ataque

    def setPosicion(self, posicion):
        self.posicion=posicion

    def matar(self):
        self.vivo=False

    def quitarVida(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.matar()

    def atacar(self):
        return random.randint(1,self.ataque)

    def getPosicion(self):
        return self.posicion

    def getInfo(self):
        return [self.vida, self.ataque, self.posicion, self.vivo]

    def isVivo(self):
        return self.vivo

    def showVida(self):
        pantalla = "♥ "*self.vida
        pantalla += " ({0})".format(self.vida)
        return pantalla
