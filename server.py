#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))
            print('Dir_ip_cliente:', self.client_address[0])
            print('Puerto_cliente:', self.client_address[1], '\n')            

if __name__ == "__main__":
    Puerto_serv = int(sys.argv[1])  # El pasado por terminal en cliente
    serv = socketserver.UDPServer(('', Puerto_serv), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
