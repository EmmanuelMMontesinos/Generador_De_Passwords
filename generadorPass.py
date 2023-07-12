"""Generador de contraseñas by Emmanuel M Montesinos"""

from random import randint, choice, shuffle
import PySimpleGUI as sg

LETRAS = ["a", "b", "c", "d", "e", "f", "g",
          "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
NUMEROS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ESPECIALES = ["!", "@", "#", "$", "%"]

layout = [[sg.Text("Nº de Contraseñas"), sg.Input(default_text="1", key="-input-", justification="right")],
          [sg.Text("Longitud"), sg.Input(default_text="17",
                                         key="-input2-", justification="right")],
          [sg.Button("Generar"), sg.Button("Copiar"), sg.Checkbox(
              "Caracteres especiales", key="-especiales-")],
          [sg.Multiline(key="-output-", size=(70, 5))]]


def generadorsin(numero, longitud):
    longitud = int(longitud)
    numero = int(numero)
    passwords = []
    for num in range(numero):
        password = ""
        fpassword = ""
        for log in range(longitud + 1):
            if log == longitud - 2:
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
    claves = ""
    for contra in passwords:
        claves = claves + contra + "\n"

    return claves


def generador(numero, longitud):
    longitud = int(longitud)
    numero = int(numero)
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
    claves = ""
    for contra in passwords:
        claves = claves + contra + "\n"

    return claves


def solicitud():
    numero = int(
        input("Bienvenido al Generador de Contraseñas, cuantas desea generar?: "))
    longitud = int(input("De cuanta longitud: "))
    return longitud, numero


def main():
    ventana = sg.Window("Generador de Contraseñas by Emmanuel M Montesinos",
                        layout=layout, icon="icono.ico")
    while True:
        eventos, valores = ventana.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "Generar":
            nume = valores["-input-"]
            if valores["-especiales-"] == True:
                resultado = generador(valores["-input-"], valores["-input2-"])
                ventana["-output-"].update(resultado)
            else:
                resultado = generadorsin(
                    valores["-input-"], valores["-input2-"])
                ventana["-output-"].update(resultado)
        elif eventos == "Copiar":
            texto = valores["-output-"]
            sg.clipboard_set(texto)
            sg.popup("Copiado en portapapeles")
    ventana.close()


if __name__ == "__main__":
    main()
