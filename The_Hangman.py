import random
import string
from Lista_Palabras import lista
from Estructura import *

def palabra_valida(*lista):
    valida= random.choice(lista)
    while "-" in valida or " " in valida:
        valida= random.choice(lista)

    return valida.upper()

def juego():
    palabra = palabra_valida(*lista)
    letras_palabra = set(palabra)
    alfabeto = set(string.ascii_uppercase)
    letras_usuario = []
    vidas = 7
   

    while len(letras_palabra)>0 and vidas>0:
    
        print(f"\n Ya usastes las siguientes letras {'-'.join(letras_usuario)}")
        print(f"Tienes {vidas} vidas restantes.")
        lista_palabra= [letter  if letter in letras_usuario else "-" for letter in palabra]
        print(f"-->  {' '.join(lista_palabra)}")
        letra_elegida = input("\nElige una letra: ").upper()
       
        if letra_elegida in letras_usuario:
            print("\n\tYa elegiste esa letra. intenta con otra.\n")
            
        elif letra_elegida in alfabeto:
            letras_usuario.append(letra_elegida)
            
            if letra_elegida in letras_palabra:
                letras_palabra.remove(letra_elegida)
                print(f"Muy bien!!")
            else:
                print("Esa letra no pertenece a la palabra.")
                vidas-=1
        else:
            print("caracter no valido. intente nuevamente.")
        pausa()
    if len(letras_palabra)==0:
        print(f"\n Felicidades!!!!\n  Adivinaste la palabra '{palabra}'.")
    elif vidas ==0:
        print(f"Te vas a la horca! :(\n La palabra que NO pudiste adivinar fue ->{palabra}<-")
    opcion=input("\n\n\t Quieres volver a jugar? (S) o (N)").upper()
    while not (opcion =="S" or opcion=="N"):
        opcion=input("\n\n\t Marca 'S' para seguir jugando ó 'N' para salir.").upper()
    if opcion=="S":
        juego()

    elif opcion=="N":
        print("\n\n\taHasta la próxima!!")


    
    



juego()

