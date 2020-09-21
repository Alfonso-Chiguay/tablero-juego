import jugador
import enemigo
import os
import random

'''
0: LIBRE
1: JUGADOR
2: ENEMIGO
3: CURA
4: META
'''

class Tablero():

    def __init__(self, filas, columnas, jugador, listaEnemigos):
        self.filas=filas
        self.columnas=columnas
        self.jugador=jugador
        self.enemigos=listaEnemigos
        self.curas = []
        self.tablero = {}


        for i in range(filas):
            temp = []
            for j in range(columnas):
                temp.append(0)
            self.tablero[i]=temp
        self.tablero[filas-1][columnas-1]=4



    def setJugador(self, jugador):
        self.jugador=jugador
    def getJugador(self):
        return self.jugador

    def setEnemigos(self, listaEnemigos):
        self.enemigos=listaEnemigos
    def getEnemigos(self):
        return self.enemigos

    def getLimites(self):
        return [self.filas-1,self.columnas-1]

    def posicionarJugador(self, jugador):
        posicionJugador = jugador.getPosicion()
        self.tablero[posicionJugador[0]][posicionJugador[1]]=1

    def posicionarEnemigos(self, listaEnemigos):
        for enemigo in listaEnemigos:
            logrado = False
            while logrado == False:
                fila = random.randint(0,self.filas-1)
                columna = random.randint(0, self.columnas-1)
                if [fila,columna] not in [[1,0],[0,1],[1,1]]:
                    if self.tablero[fila][columna]==0:
                        self.tablero[fila][columna]=2
                        enemigo.setPosicion([fila,columna])
                        logrado = True

    def cantidadCuras(self):
        return len(self.curas)

    def posicionarEnemigo(self, enemigo):
        pos = enemigo.getPosicion()
        self.tablero[pos[0]][pos[1]] = 2

    def posicionesCuras(self, listaCuras):
        self.curas = listaCuras

    def posicionarMeta(self):
        self.tablero[self.filas-1][self.columnas-1]=4

    def posicionarCuras(self, curas):
        listaCuras = []
        for i in range(curas):
            logrado = False
            while logrado == False:
                fila = random.randint(0,self.filas-1)
                columna = random.randint(0, self.columnas-1)
                if [fila,columna] not in [[1,0],[0,1],[1,1]]:
                    if self.tablero[fila][columna]==0:
                        self.tablero[fila][columna]=3
                        listaCuras.append([fila,columna])
                        logrado = True
        self.posicionesCuras(listaCuras)

    def limpiarPosicion(self, posicion):
        self.tablero[posicion[0]][posicion[1]]=0

    def eliminarEnemigo(self, posicion):
        for enemigo in self.enemigos:
            if enemigo.getPosicion() == posicion:
                self.enemigos.remove(enemigo)
                break

    

    def verificarCura(self, jugador):
        if jugador.getPosicion() in self.curas:
            self.curas.remove(jugador.getPosicion())            
            return True
        else:
            return False


    def mostrarTablero(self, jugador):
        os.system('cls')
        print("Juego para jugadores que quieren jugar version Alfa 1.1")
        print("W: Arriba; S: Abajo; A: Izquieda; D: Derecha")
        print("Vida: {0}".format(jugador.showVida()))
        print("Intentos disponibles: {0}".format(jugador.getMuertes()))
        print('\n')
        for i in self.tablero:
            linea = ""
            for j in self.tablero[i]:

                if j == 0:
                    linea+="[ ]"
                elif j == 1:
                    linea+="[O]"
                elif j == 2:
                    linea+="[☻]"
                elif j == 3:
                    linea+="[+]"
                elif j == 4:
                    linea+="[▼]"
            print(linea)
