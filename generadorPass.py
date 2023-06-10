"""Generador de contraseñas by Emmanuel M Montesinos"""

from random import randint, choice, shuffle


LETRAS = ["a", "b", "c", "d", "e", "f", "g",
          "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
NUMEROS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ESPECIALES = ["!", "@", "#", "$", "%"]


def generador(longitud, numero):
    passwords = []
    for num in range(numero):
        password = ""
        fpassword = ""
        for log in range(longitud):
            if log == longitud - 2:
                password = password + choice(ESPECIALES)
                password = password + choice(NUMEROS)
            elif log != longitud - 1:
                moneda = randint(1, 2)
                if moneda == 1:
                    password = password + choice(LETRAS).upper()
                else:
                    password = password + choice(LETRAS)
        lista = list(password)
        shuffle(lista)
        fpassword = "".join(lista)
        passwords.append(fpassword)
    return passwords


def solicitud():
    numero = int(
        input("Bienvenido al Generador de Contraseñas, cuantas desea generar?: "))
    longitud = int(input("De cuanta longitud: "))
    return longitud, numero


def main():
    longitud, numero = solicitud()
    passwords = generador(longitud, numero)
    print("Contraseñas generadas:")
    for i in passwords:
        print(f"{i}")


if __name__ == "__main__":
    main()
