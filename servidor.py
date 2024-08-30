import socket
import sys

def my_atoi(s):
    try:
        return int(s)
    except ValueError:
        return 0

def main():
    while True:

        # Inicialización de variables
        puerto = 8080

        # Crear el socket
        print("Creando socket...")
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket creado.")

        # Configuración del socket
        server_address = ('', puerto)
        skt.bind(server_address)
        print("Bind realizado.")

        # Escuchar conexiones entrantes
        skt.listen(5)
        print("Esperando conexiones entrantes...")

        # Aceptar conexión
        skt2, cliente_address = skt.accept()
        print(f"Cliente {cliente_address[0]} conectado exitosamente.")

        opcion = None
        while opcion != 0:
            try:
                skt2.sendall(b"Ingrese numero distinto de 0 para entrar al sistema: ")
                mensaje = skt2.recv(2000).decode('utf-8')
                opcion = my_atoi(mensaje)
                print("Cliente conectado exitosamente. Aguardando su salida.")
            except Exception as e:
                print(f"Error: {e}")
                break

        skt2.close()
        skt.close()

if __name__ == "__main__":
    main()