import socket
import re

s=socket.socket()
s.connect(('127.0.0.1',9999))
while True:
	mensaje = s.recv(1024)
	if(mensaje == "turno"):
            movimientoValido = True
            while (movimientoValido == True):
                sintaxisValida = False
                while (sintaxisValida == False):
                    movimiento = raw_input('Movimiento>>>')
                    patron = re.compile('^[A-H][1-8]-[A-H][1-8]')
                    if (patron.match(movimiento)):
                        sintaxisValida = True
                        s.send(movimiento)
                        validacion = s.recv(1024)
                        if (validacion == 'True'):
                            mensaje == 'no turno'
                            movimientoValido = False
                        else:
                            print 'Jugada invalida'
                    else:
                        print 'movimiento invalido'
            
	elif(mensaje=="closing"):
		print "adios"
		break
	else:
		print mensaje
s.close()    