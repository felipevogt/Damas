import socket
import threading
import time
from JuegoDamas import JuegoDamas

class Server():

    def __init__(self):
        self.host='localhost'
        self.port=9999
        self.maxcon=10

    def start(self):

        self.s = socket.socket()
        self.s.bind((self.host,self.port)) 
        self.s.listen(self.maxcon) 
        print "Esperando Jugadores"
        while True:
            (sc1,addr1)=self.s.accept()
            sc1.send("Esperando oponente")
            (sc2,addr2)=self.s.accept()
            sc1.send("Oponente, listo.")
            sc2.send("Oponente, listo.")
            print "Jugadores listos" 
            cliente = Client((sc1,addr1),(sc2,addr2))
            cliente.start()


class Client(threading.Thread): 
    
    def __init__(self,(sc,addr),(sc2,addr2)):
        threading.Thread.__init__(self)
        self.sc1=sc
        self.addr1=addr
        self.sc2=sc2
        self.addr2=addr2
    def run(self):
        self.juego = JuegoDamas(self.sc1, self.sc2)
        self.sc1.send("closing")
        self.sc2.send("closing")
if __name__ == '__main__':
    server =Server()
    server.start()