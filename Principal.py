#%% 1. Cabecera
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:09:22 2024

@author: vctr23
"""

#%% 2. Imports
import requests
import random
import customtkinter as ctk
from multiprocessing import Process
from API import iniciar_aplicacion
import GUI

#%% 3. Código
def leer_api():
    # Busco la respuesta
    url = "http://127.0.0.1:5000/lista"
    respuesta = requests.get(url)
    lista = respuesta.json()
    return lista
           
def palabra_a_buscar():
    """
    Método que transforma la api en una lista, la lee 
    y me devuelve una palabra aleatoria para el juego
    
    Returns -> Devuelve la posicion de la lista 
    """
    lista = leer_api()  
    posicion_lista = random.randint(0, len(lista) -1)
    
    return lista[posicion_lista]

def pasar_a_asteriscos(palabra):
    """
    Método que sustituye la palabra por * y la devuelve
    
    Returns -> palabra_encriptada : str 
    """   
    # Imprime asterisco si el caracter es una letra sino imprime ese caracter
    return "".join("*" if asterisco.isalpha() else asterisco for asterisco in palabra)

def juego():
    """
    Método que añade toda la funcionalidad del juego ahorcado

    Returns -> None.
    """
    #Genero la palabra y asigno una variable a cada parte del diccionario a leer
    palabra = palabra_a_buscar()
    pais = palabra["pais"]
    pista = palabra["pista"]
    # Llamo a la funcion para encriptar la palabra
    palabra_encriptada = pasar_a_asteriscos(pais)
    
    # Funcionalidades para el juego
    intentos_restantes = 5
    letras_falladas = []
    mensaje = ""
       
    def adivinar(letra, actualizar_gui, entrada):
        """
        Método que añade la funcionalidad para poder adivinar la palabra

        Returns -> None.
        """
        nonlocal intentos_restantes, palabra_encriptada, letras_falladas, mensaje
        
        # Mensaje de error si el usuario repite letras
        if letra in letras_falladas or letra in palabra_encriptada:
            actualizar_gui("Esa letra ya ha sido usada.", palabra_encriptada, intentos_restantes, letras_falladas)
            entrada.delete(0, "end") # Limpio el entry
            return
        
        # Mensaje de error si no se introduce una letra o se pone más de 1 caracter
        if not letra.isalpha() or len(letra) != 1:
            actualizar_gui("Debes escribir una letra.", palabra_encriptada, intentos_restantes, letras_falladas)
            entrada.delete(0, "end")
            return
        
        # Lower para evitar errores con mayusculas
        if letra in pais.lower():
            # Añado las letras a la palabra encriptada si son correctas
            palabra_encriptada = "".join(
                # Imprimo la letra si existe en esa posicion de la palabra
                # sino imprimo la letra encriptada
                letra if pais[i].lower() == letra else palabra_encriptada[i] 
                for i in range(len(pais))
            )
            actualizar_gui(mensaje, " ".join(palabra_encriptada), intentos_restantes, letras_falladas)
            entrada.delete(0, "end")
            
            # Compruebo si ya se han adivinado todas las letras y muestro mensaje de victoria
            if palabra_encriptada.lower() == pais.lower():
                actualizar_gui("¡Has ganado!", palabra_encriptada, intentos_restantes, letras_falladas) 

        else: # La letra no existe en la palabra
            intentos_restantes -= 1
            letras_falladas.append(letra)
            actualizar_gui(mensaje, palabra_encriptada, intentos_restantes, letras_falladas)
            entrada.delete(0, "end")

            if intentos_restantes == 0:     # Mensaje de derrota si quedan 0 intentos
                actualizar_gui(f"Has perdido. El país era {pais}.", palabra_encriptada, intentos_restantes, letras_falladas)
     
    def mostrar_pista(label_pista):
        """
        Método que actualiza el label para mostrar la pista

        Returns -> None.
        """
        label_pista.configure(text = f"Pista: {pista}")
        
    return {"adivinar": adivinar, 
            "mostrar_pista": mostrar_pista,
            "palabra_encriptada": palabra_encriptada,
            "pista": pista, 
            "intentos_restantes": intentos_restantes, 
            "letras_falladas": letras_falladas}

def encriptación_cesar():
    """
    Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada 
    por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto (Wikipedia)
    
    Formula cifrado C(resultado) = P(posicion cada letra en la palabra) + K(posiciones a desplazar)
    """
    palabra = palabra_a_buscar()["pais"]
    
    letras = "abcdefghijklmnñopqrstuvwxyz"
    k = random.randint(1, 10)
    palabra_encriptada = ""
    
    for letra in palabra.lower():
        # Busco la posicion de la letra en el string y le sumo el desplazamiento
        suma = letras.find(letra) + k
        # Le digo que la posicion de la letra devuelta no puede ser mayor que la longitud de letras(abecedario)
        modulo = suma % len(letras)
        # Construyo la palabra encriptada añadiendo las letras 
        palabra_encriptada = palabra_encriptada + letras[modulo]
    
    return palabra, palabra_encriptada
 
#%% 4. Main
if __name__ == "__main__":
    # Crear el proceso de la API e iniciarlo
    process = Process(target=iniciar_aplicacion)
    process.start()

    # Abrir el GUI de customtkinter
    root = ctk.CTk()
    app = GUI.Root(root)
    root.mainloop()

    # Destruir el proceso cuando la ventana se cierra
    process.kill()