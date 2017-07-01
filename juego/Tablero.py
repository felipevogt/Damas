import time

class Tablero():
    def __init__(self):
	self.matriz = [['#'] * 8 for i in range(8)]
        self.posicionesIniciales1()
        self.posicionesIniciales2()
    
    def posicionesIniciales2(self):
        self.matriz[0][0] = 'n'
        self.matriz[0][2] = 'n'
        self.matriz[0][4] = 'n'
        self.matriz[0][6] = 'n'
        self.matriz[1][1] = 'n'
        self.matriz[1][3] = 'n'
        self.matriz[1][5] = 'n'
        self.matriz[1][7] = 'n'
        self.matriz[2][0] = 'n'
        self.matriz[2][2] = 'n'
        self.matriz[2][4] = 'n'
        self.matriz[2][6] = 'n'
        
    def posicionesIniciales1(self):
        self.matriz[7][1] = 'b'
        self.matriz[7][3] = 'b'
        self.matriz[7][5] = 'b'
        self.matriz[7][7] = 'b'
        self.matriz[6][0] = 'b'
        self.matriz[6][2] = 'b'
        self.matriz[6][4] = 'b'
        self.matriz[6][6] = 'b'
        self.matriz[5][1] = 'b'
        self.matriz[5][3] = 'b'
        self.matriz[5][5] = 'b'
        self.matriz[5][7] = 'b'
        
    
    def mostrarTablero(self, sc):
        sc.send('    a    b    c    d    e    f    g    h')
        for i in range (8):
            numeroFila = str(8 - i) + ' '
            fila = str(self.matriz[i])
            sc.send(numeroFila + fila)
            time.sleep(0.01)
        
    def getFicha(self, i, j):
        return self.matriz[i][j]
    def setFicha(self, i, j, color):
        self.matriz[i][j] = color            
            
        
