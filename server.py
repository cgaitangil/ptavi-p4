#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
#    def __init__(self):
 #       self.users = {}
    

    def handle(self):
        
        print('')
        for line in self.rfile:
            print("El cliente nos manda:", line.decode('utf-8'))
            self.wfile.write(line)  # Escribimos en socket el mensaje recibido
            print('Enviando eco:', line.decode('utf-8'))  # Server eco
            print('')
            print('Dir_ip_cliente:', self.client_address[0])
            print('Puerto_cliente:', self.client_address[1], '\n')
            
            
if __name__ == "__main__":
    Puerto_serv = int(sys.argv[1])  # El pasado por terminal en cliente
    serv = socketserver.UDPServer(('', Puerto_serv), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
        
    Usuarios = {}
