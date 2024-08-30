import socket
import random
import string
import sys
import os
import time

# Definir constantes
MAX = 80


def menu_inicial():
    repite = True
    while repite:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\t\t\tMENU\n")
        print("\t\t\t============")
        print("\n\t\t[1]. Generar Usuario")
        print("\t\t[2]. Generar contrase\u00f1a")
        print("\t\t[0]. Salir")
        opcion = int(input("\n\t\tIngrese su opcion: "))

        if opcion == 1:
            generar_usuario()
        elif opcion == 2:
            generar_contrasenia()
        elif opcion == 0:
            repite = False


def generar_usuario():
    print("\n\nGenerador de usuarios\n\n")
    tamanio = int(input("Indique la cantidad de caracteres que desea para su usuario: "))
    if tamanio < 5 or tamanio > 15:
        print("El usuario deseado debe estar compuesto entre 5 y 15 caracteres.")
    else:
        usuario_aleatorio(tamanio)


def generar_contrasenia():
    print("\n\nGenerador de contrase\u00f1as\n\n")
    tamanio = int(input("Indique la cantidad de caracteres que desea para su contrase\u00f1a: "))
    if tamanio < 8 or tamanio > 50:
        print("La contrase\u00f1a deseada debe estar compuesta entre 8 y 50 caracteres.")
    else:
        contrasenia_aleatoria(tamanio)


def usuario_aleatorio(tamanio):
    random.seed(int(time.time()))
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    usuario = []

    aux = -1
    for _ in range(tamanio):
        aleatorio = random.randint(0, 1)
        if aleatorio == 1 and aux != aleatorio:
            usuario.append(random.choice(vocales))
            aux = aleatorio
        elif aleatorio == 1 and aux == aleatorio:
            usuario.append(random.choice(consonantes))
            aux = aleatorio
        elif aleatorio == 0 and aux != aleatorio:
            usuario.append(random.choice(consonantes))
            aux = aleatorio
        else:
            usuario.append(random.choice(vocales))
            aux = aleatorio

    print(f"\nEl usuario es: {''.join(usuario)}")


def contrasenia_aleatoria(tamanio):
    random.seed(int(time.time()))
    numeros = "0123456789"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    contrasenia = []
    for _ in range(tamanio):
        aleatorio = random.randint(0, 2)
        if aleatorio == 0:
            contrasenia.append(random.choice(numeros))
        elif aleatorio == 1:
            contrasenia.append(random.choice(minuscula))
        else:
            contrasenia.append(random.choice(mayuscula))

    print(f"La contrase\u00f1a es: {''.join(contrasenia)}")


def my_atoi(s):
    try:
        return int(s)
    except ValueError:
        return 0


def main():
    while True:
        # Crear el socket
        print("Inicializando socket...")
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        puerto = int(input("Ingrese puerto: "))
        server_address = ('127.0.0.1', puerto)

        try:
            skt.connect(server_address)
            print("Conexion exitosa.")
        except socket.error as e:
            print(f"Error de conexion: {e}")
            sys.exit(-1)

        opcion = -1
        while opcion != 0:
            try:
                mensaje = skt.recv(2000).decode('utf-8')
                print(f"\nServer - {mensaje}")

                mensaje = input()
                opcion = my_atoi(mensaje)

                skt.sendall(mensaje.encode('utf-8'))

                if opcion != 0:
                    menu_inicial()
            except socket.error as e:
                print(f"Error en la comunicacion: {e}")
                break

        print("\n\nElegiste salir! Adios!")
        skt.close()


if __name__ == "__main__":
    main()