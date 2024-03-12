import socket

ip = input("Ingrese la IP a escanear: ")
#Los puertos de un pc son estos, por lo que en el bucle for, va a ir probando uno a uno de los puertos de la ip dada.
for puerto in range(1,65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, puerto))

    if result == 0: 
        print("Puerto " + str(puerto) + " abierto.")
        sock.close()

    else:
        print("Puerto " + str(puerto) + " cerrado.")
