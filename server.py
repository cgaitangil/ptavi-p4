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
        
        print('')
        for line in self.rfile:
        
            try:
                Mensaje = line.decode('utf-8')
                Mensaje.split(' ')[-1] = Mensaje.split(' ')[-1][:-4]
                print(Mensaje.split(' '))                
                print(Mensaje.split(' ')[-1])
                print("El cliente nos manda:", Mensaje)
                
                self.wfile.write(line)  # Mandamos por socket el mensaje recib.
                print('Enviando eco:', line.decode('utf-8'))  # Server eco
                          


                Usuario = Mensaje.split(' ')[1]   # Quitamos \r\n
                
                if Mensaje.split(' ')[0] == 'REGISTER':
                    self.wfile.write(bytes('SIP/2.0 OK', 'utf-8') + b'\r\n\r\n')
                    self.Users[Usuario] = self.client_address[0]
                
                print('Usuarios:')
                print(self.Users, '\n')
            except:
                print('Error: client.py <IP> <Port> register <User>')
                self.wfile.write(bytes('Error: client.py <IP> <Port> register <User>', 'utf-8') + b'\r\n')    
            
     
            
if __name__ == "__main__":
    Puerto_serv = int(sys.argv[1])  # El pasado por terminal en cliente
    serv = socketserver.UDPServer(('', Puerto_serv), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
