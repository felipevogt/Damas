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

        
        
        while (self.tablero.verEstadoNegras() != 0 and self.tablero.verEstadoBlancas() != 0 ):
            print 'Fichas negras: ',self.tablero.verEstadoNegras()
            print 'Fichas blancas: ',self.tablero.verEstadoBlancas()
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
                    
                    if(self.isReina(self.x, self.y, self.colorJugador1) == True):
                        if ((self.newX==self.x+1 or self.newX==self.x-1) and (self.newY==self.y+1 or self.newY==self.y-1)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1.upper())
                            print "Jugador 1: ", movimientoJugador1
                            self.jugador1.send('True')
                            break
                        elif ((self.newX==self.x+2 or self.newX==self.x-2) and (self.newY==self.y+2 or self.newY==self.y-2)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1.upper())
                            self.comerFicha(self.x,self.y,self.newX,self.newY)
                            print "Jugador 1: ", movimientoJugador1
                            self.jugador1.send('True')
                            break
                    
                    else:
                        if (self.newX==self.x+1 and (self.newY==self.y+1 or self.newY==self.y-1)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1)
                            print "Jugador 1: ", movimientoJugador1
                            self.jugador1.send('True')
                            if (self.newX == 7):
                                self.convertirReina(self.newX,self.newY,self.colorJugador1)
                            break
                        elif (self.newX==self.x+2 and (self.newY==self.y+2 or self.newY==self.y-2)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1)
                            self.comerFicha(self.x,self.y,self.newX,self.newY)
                            print "Jugador 1: ", movimientoJugador1
                            self.jugador1.send('True')
                            if (self.newX == 7):
                                self.convertirReina(self.newX,self.newY,self.colorJugador1)
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
                    if(self.isReina(self.x, self.y, self.colorJugador1) == True):
                        if ((self.newX==self.x+1 or self.newX==self.x-1) and (self.newY==self.y+1 or self.newY==self.y-1)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1.upper())
                            print "Jugador 2: ", movimientoJugador1
                            self.jugador1.send('True')
                            break
                        elif ((self.newX==self.x+2 or self.newX==self.x-2) and (self.newY==self.y+2 or self.newY==self.y-2)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador1.upper())
                            self.comerFicha(self.x,self.y,self.newX,self.newY)
                            print "Jugador 2: ", movimientoJugador1
                            self.jugador1.send('True')
                            break
                    else:
                        if (self.newX==self.x-1 and (self.newY==self.y+1 or self.newY==self.y-1)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador2)
                            print "Jugador 2: ", movimientoJugador2
                            self.jugador2.send('True')
                            if (self.newX == 0):
                                self.convertirReina(self.newX,self.newY,self.colorJugador2)
                            break
                        elif (self.newX==self.x-2 and (self.newY==self.y+2 or self.newY==self.y-2)):
                            self.moverFicha(self.x,self.y,self.newX,self.newY,self.colorJugador2)
                            self.comerFicha(self.x,self.y,self.newX,self.newY)
                            print "Jugador 2: ", movimientoJugador2
                            self.jugador2.send('True')
                            if (self.newX == 0):
                                self.convertirReina(self.newX,self.newY,self.colorJugador2)
                            break
                else:
                    self.jugador2.send('False')
        if (self.tablero.verEstadoNegras() == 0):
            self.jugador1.send('Perdiste')
            self.jugador2.send('Ganaste')
            time.sleep(2)
        else:
            self.jugador2.send('Perdiste')
            self.jugador1.send('Ganaste')
            time.sleep(2)
        
    def isFicha(self, x, y, color):
        if (self.tablero.getFicha(x, y) == color):
            return True
        else:
            return False
    
    def convertirReina(self, x,y, color):
        self.tablero.setFicha(x, y, color.upper())
    def isReina(self, x,y, color):
        if (self.tablero.getFicha(x, y) == color.upper()):
            return True
        else:
            return False
        
    def puntoMedio(self,x ,y, newX, newY):
        medioX = (x + newX)/2
        medioY = (y + newY)/2
        if (self.tablero.getFicha(medioX, medioY) == 'n'):
            return 'n'
        elif (self.tablero.getFicha(medioX, medioY) == 'b'):
            return 'b'
        elif (self.tablero.getFicha(medioX, medioY) == 'N'):
            return 'N'
        elif (self.tablero.getFicha(medioX, medioY) == 'B'):
            return 'B'
        else:
            return '#'
        
    def validarMovimiento(self, x, y, newX, newY, color):
        if (self.isFicha(x, y, color) == True):
            if (color == 'n'):
                if (newX==x+1 and (newY==y+1 or newY==y-1)):
                    if (self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                elif (newX==x+2 and (newY==y+2 or newY==y-2)):
                    if (self.puntoMedio(x,y,newX,newY) == 'b' and self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                else:
                    return False
    
            elif (color == 'b'):
                if (newX==x-1 and (newY==y+1 or newY==y-1)):
                    if(self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                elif (newX==x-2 and (newY==y+2 or newY==y-2)):
                    if (self.puntoMedio(x,y,newX,newY) == 'n' and self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:   
                        return False
                else:
                    return False
 
        elif(self.isReina(x, y, color) == True):
            if (color.upper() == 'N'):
                if ((newX==x+1 or newX==x-1) and (newY==y+1 or newY==y-1)):
                    if (self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                elif ((newX==x+2 or newX==x-2) and (newY==y+2 or newY==y-2)):
                    if ((self.puntoMedio(x,y,newX,newY) == 'b' or self.puntoMedio(x,y,newX,newY) == 'B') and self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                else:
                    return False
    
            elif (color.upper() == 'B'):
                if ((newX==x+1 or newX==x-1) and (newY==y+1 or newY==y-1)):
                    if(self.tablero.getFicha(newX, newY) == '#'):
                        return True
                    else:
                        return False
                elif ((newX==x+2 or newX==x-2) and (newY==y+2 or newY==y-2)):
                    if ((self.puntoMedio(x,y,newX,newY) == 'n' or self.puntoMedio(x,y,newX,newY) == 'N')and self.tablero.getFicha(newX, newY) == '#'):
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
        
    def comerFicha(self,x,y,newX,newY):
        medioX = (x + newX)/2
        medioY = (y + newY)/2
        self.tablero.setFicha(medioX, medioY, '#')
        
   
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


        
