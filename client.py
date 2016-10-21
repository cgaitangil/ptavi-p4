#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER = str(sys.argv[1])
    PORT = int(sys.argv[2])
    LINE = sys.argv[3:]
    Exp = 'Expires: ' + sys.argv[5] + '\r\n\r\n' # Cabecera Expires
    LINE = LINE[0].upper() + ' sip:' + LINE[1] + ' SIP/2.0' + '\r\n' + Exp
except:
    Error = 'Usage: client.py ip puerto register sip_address expires_value'
    sys.exit('\n' + Error + '\n')
    
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print('\r\n' + "Enviando:" + '\r\n' + LINE)
    my_socket.send(bytes(LINE, 'utf-8'))
    data = my_socket.recv(1024)
    print('Recibido:', data.decode('utf-8'))



   

print("Socket terminado.")
