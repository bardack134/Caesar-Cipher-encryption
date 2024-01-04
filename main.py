
# Importar los módulos encrypt y decrypt que contienen las funciones para encriptar y desencriptar el mensaje
from encrypt import *

from decrypt import *

from art import *

from instructions import *
#impormimos logo del codigo
print(logo)

should_continue = True

while should_continue:
    
    print(initial_message)
    
    # Pedir al usuario que elija si quiere encriptar o desencriptar un mensaje y asignar su respuesta a una variable llamada direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


    # Pedir al usuario que introduzca el mensaje que quiere encriptar o desencriptar y asignar su respuesta a una variable llamada text. Convertir  el mensaje a minúscula.
    text = input("Type your message:\n").lower()


    
    
    # Comprobar si el texto son solo digitos
    if text.isdigit():
       # Si es así, pedir al usuario que introduzca el mensaje de nuevo y asignarlo a la variable text
       text = input("you enter a incorrect data, please enter your message again: ")


    # Pedir al usuario que introduzca el número de posiciones que quiere desplazar las letras y asignar su respuesta a una variable llamada shift.  Convertir la respuesta a un número entero.
    shift = int(input("Type the shift number:\n"))

    #modificamos el shift para que no importa el numero que el usuario introduzca nuestro codigo pueda correr y no muestre error "item out of   Range" porque da un valor posicional de la lista mayor a la cantidad de items en nuestra lista 

    shift = shift % 27
    # Imprimir una línea vacía para separar
    print('')

    # Comprobar si el usuario eligió encriptar el mensaje
    if direction == 'encode':
        # Si es así, llamar a la función encrypt del módulo encrypt con el mensaje y el desplazamiento como argumentos
        encrypt(text, shift)

    # Comprobar si el usuario eligió desencriptar el mensaje
    elif direction == 'decode':
        # Si es así, llamar a la función decrypt del módulo decrypt con el mensaje y el desplazamiento como argumentos
        decrypt(text, shift)

    # Si el usuario no eligió ninguna de las dos opciones
    else:
        # Imprimir un mensaje de error que le dice al usuario que no introdujo 'encode' o 'decode'
        print("you didn't enter 'encode' or 'decode', please try again")
        # Pedir al usuario que elija de nuevo y asignar su respuesta a la variable direction
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        # Imprimir una línea vacía para separar
        print()
        # Crear un bucle while que se repita mientras el usuario no elija una opción válida
        while direction != 'encode' and direction != 'decode':
            # Imprimir un mensaje de error que le dice al usuario que no introdujo 'encode' o 'decode'
            print("you didn't enter 'encode' or 'decode', please try again")
            # Pedir al usuario que elija de nuevo y asignar su respuesta a la variable direction
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            # Imprimir una línea vacía para separar
            print()

            # Comprobar si el usuario eligió encriptar el mensaje
            if direction == 'encode':
                # Si es así, llamar a la función encrypt del módulo encrypt con el mensaje y el desplazamiento como argumentos
                encrypt(text, shift)

            # Comprobar si el usuario eligió desencriptar el mensaje
            elif direction == 'decode':
                # Si es así, llamar a la función decrypt del módulo decrypt con el mensaje y el desplazamiento como argumentos
                decrypt(text, shift)       

    result = input("Types 'Y' if you want to go again. Otherwise type 'N': ").lower()

    if result == 'y':
        should_continue = True
    
    else:
        should_continue = False    
