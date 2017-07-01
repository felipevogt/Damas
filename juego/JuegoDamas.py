from Jugador import Jugador
from Tablero import Tablero
import time

class JuegoDamas():
    def __init__(self, sc1, sc2):

        self.jugador1 = sc1
        self.colorJugador1 = 'n'
        self.jugador1.send('Eres el jugador 1, tus fichas son las negras')
        self.jugador2 = sc2
        self.colorJugador2 = 'b'
        self.jugador2.send('Eres el jugador 2, tus fichas son las blancas')
        self.tablero = Tablero()
        
        while True:
            
            #Turno jugador1
            self.tablero.mostrarTablero(self.jugador1)
            self.tablero.mostrarTablero(self.jugador2)
            self.jugador1.send('turno')
            self.jugador2.send("Mueve jugador 1, Espere...")
            time.sleep(0.1)
            while True:
                movimientoJugador1=self.jugador1.recv(1024)
                self.descomponerCadena(movimientoJugador1)
                if (self.validarMovimiento(self.x,self.y,self.newX,self.newY,self.colorJugador1) == True):
                    self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1)
                    print "Jugador 1: ", movimientoJugador1
                    self.jugador1.send('True')
                    break
                else:
                    self.jugador1.send('False')
            
            #Turno jugador2
            self.tablero.mostrarTablero(self.jugador1)
            self.tablero.mostrarTablero(self.jugador2)
            self.jugador1.send("Mueve jugador 2, Espere...")
            self.jugador2.send("turno")
            time.sleep(0.1)
            while True:
                movimientoJugador2=self.jugador2.recv(1024)
                self.descomponerCadena(movimientoJugador2)
                if (self.validarMovimiento(self.x,self.y,self.newX,self.newY,self.colorJugador2) == True):
                    self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador2)
                    print "Jugador 2: ", movimientoJugador2
                    self.jugador2.send('True')
                    break
                else:
                    self.jugador2.send('False')
    
        
    def isFicha(self, x, y, color):
        if (self.tablero.getFicha(x, y) == color):
            return True
        else:
            return False
        
    def validarMovimiento(self, x, y, newX, newY, color):
        if (self.isFicha(x, y, color) == True):
            if (color == 'n'):
                if (newX==x+1 and (newY==y+1 or newY==y-1)):
                    if (self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                else:
                    return False
    
            else:
                if (newX==x-1 and (newY==y+1 or newY==y-1)):
                    if(self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
            

    def moverFicha(self, x, y, newX, newY, color):

        self.tablero.setFicha(x, y, '#')
        self.tablero.setFicha(newX, newY, color)
   
    def descomponerCadena(self, movimiento):
        letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        numeros = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
        if movimiento[0] in letras:
            self.y = int(letras[movimiento[0]])
        if movimiento[1] in numeros:
            self.x = int(numeros[movimiento[1]])
        if movimiento[3] in letras:
            self.newY = int(letras[movimiento[3]])
        if movimiento[4] in numeros:
            self.newX = int(numeros[movimiento[4]])


        
