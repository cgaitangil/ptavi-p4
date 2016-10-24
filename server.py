#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class. Método activado con cada petición
    """
    Users = {}

    def handle(self):
        '''Método que se ejecutará cada vez que enviemos petición'''

        self.json2registered()
        Mensaje = self.rfile.read().decode('utf-8')
        print("El cliente nos manda:" + '\n' + Mensaje)
        Usuario = Mensaje.split(' ')[1][4:]
        T_exp = Mensaje.split(' ')[-1][:Mensaje.split(' ')[-1].find('\r')]
        if Mensaje.split(' ')[0] == 'REGISTER':
            self.wfile.write(b'SIP/2.0 OK\r\n\r\n')
            if T_exp == '0':
                try:
                    del self.Users[Usuario]

                except KeyError:
                    print('Error: User to delete not found in REGISTER')
                    self.wfile.write(b'Error: User to delete not found\r\n')
            else:
                expires = str(time.strftime('%Y-%m-%d %H:%M:%S',
                              time.gmtime(time.time()))) + ' +' + T_exp
                self.Users[Usuario] = {'address': self.client_address[0],
                                       'expires': expires}

        self.register2json()
        print('Usuarios:')
        print(self.Users)
        print('\r\n' + '-----------------Siguiente petición-----------------')

    def register2json(self):
        '''Actualiza el archivo JSON'''

        json.dump(self.Users, open('registered.json', 'w'), indent=4)

    def json2registered(self):
        '''Carga del fichero registered.json si lo hay'''

        with open('registered.json') as fich:
            try:
                self.Users = json.load(fich)
            except:
                pass

if __name__ == "__main__":
    Puerto_serv = int(sys.argv[1])  # El pasado por terminal en cliente
    serv = socketserver.UDPServer(('', Puerto_serv), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco..." + '\n')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
