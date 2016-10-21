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
    Users = {}

    def handle(self):
        
        Mensaje = self.rfile.read().decode('utf-8')
        print('\n' + "El cliente nos manda:" + '\n' + Mensaje)
        print(Mensaje.split(' '))
        Usuario = Mensaje.split(' ')[1][4:]
        T_exp = Mensaje.split(' ')[-1][:Mensaje.split(' ')[-1].find('\r')]
        print(Usuario)
        print(T_exp)
        if Mensaje.split(' ')[0] == 'REGISTER':
            self.wfile.write(b'SIP/2.0 OK\r\n\r\n')            
            if T_exp == '0':
                try:
                    del self.Users[Usuario]

                except KeyError:
                    print('Error: User to delete not found in REGISTER')
                    self.wfile.write(b'Error: User to delete not found\r\n')
            else:
                self.Users[Usuario] = self.client_address[0] 


        

            
        print('\n' + 'Usuarios:')
        print(self.Users)
        print('\r\n' + '----------------------------------')
       
        
        #    try:

           # except:
            #print('Error: client.py <IP> <Port> register <User>')
           # self.wfile.write(bytes('Error: client.py <IP> <Port> register <User>', 'utf-8') + b'\r\n')    
            
     
            
if __name__ == "__main__":
    Puerto_serv = int(sys.argv[1])  # El pasado por terminal en cliente
    serv = socketserver.UDPServer(('', Puerto_serv), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
