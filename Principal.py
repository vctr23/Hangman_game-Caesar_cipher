#%% 1. Cabecera
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:09:22 2024

@author: vctr23
"""

#%% 2. Imports
import requests
import random
import tkinter as tk
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
    
    Salida: Devuelve la posicion de la lista 
    """
    lista = leer_api()
    
    # Por si se necesita imprimir los datos de la lista
    # for country in lista:
    #     print(f"Pais: {country['pais']}, Pista: {country['pista']}")
     
    # Genero un numero aleatorio que será el pais de la lista a leer 
    posicion_lista = random.randint(0, len(lista) -1 )
    
    # Devuelvo la posición del pais a adivinar
    return lista[posicion_lista]

def pasar_a_asteriscos(palabra):
    """
    Método que sustituye la palabra por * y la devuelve
    
    Salida
    -------
    palabra_encriptada : str | Devuelve la palabra encriptada
    """
    # Para reemplazarla por *, hago replace de la palabra e imprimo len(palabra) asteriscos
    # palabra_encriptada = palabra.replace(palabra, "*" * len(palabra))
    # return palabra_encriptada
    
    # Lo he modificado para poder imprimir las letras ya adivinadas
    # Imprime asterisco si el caracter es una letra sino imprime ese caracter
    return "".join("*" if asterisco.isalpha() else asterisco for asterisco in palabra)

def juego():
    """
    Método que añade toda la funcionalidad del juego ahorcado

    Salida: None.
    """
    # Me creo la pantalla de juego
    root3 = tk.Toplevel()
    root3.title("Juego ahorcado")
    root3.geometry("400x300")
    root3.configure(bg = "#201E1E")
    
    #Genero la palabra y asigno una variable a cada parte del diccionario a leer
    palabra = palabra_a_buscar()
    pais = palabra["pais"]
    pista = palabra["pista"]
    # Llamo a la funcion para encriptar la palabra
    palabra_encriptada = pasar_a_asteriscos(pais)
    
    # Funcionalidades para el juego
    intentos_restantes = 5
    letras_falladas = []
    
    # Label que muestra la palabra encriptada a resolver 
    label_palabra = tk.Label(root3, text = f"{palabra_encriptada}")
    label_palabra.pack(pady = 15)
    
    # Label que muestra la pista
    label_pista = tk.Label(root3, text = "", fg = "Green")
    label_pista.pack()
    
    # Entrada de texto para adivinar
    entrada = tk.Entry(root3)
    entrada.pack(side = "bottom", pady = 5, expand = False)
    
    def adivinar():
        """
        Método que añade la funcionalidad para poder adivinar la palabra

        Salida: None.
        """
        # Llamo a estas variables ya creadas anteriormente para usarlas
        nonlocal intentos_restantes, palabra_encriptada
        
        # Recojo el input de texto 
        letra = entrada.get().lower()
        # Elimino el texto que hubiese antes para poder escribir uno nuevo
        entrada.delete(0, tk.END)
        
        # Muestro mensaje de error si el usuario repite letras
        if letra in letras_falladas or letra in palabra_encriptada:
            label_mensaje.config(text="Esa letra ya ha sido usada.")
            return
        
        # Muestro mensaje de error si no se introduce una letra o se pone más de 1 caracter
        if not letra.isalpha() or len(letra) != 1:
            label_mensaje.config(text="Debes escribir una letra.")
            return
        
        # Trato la palabra como lower para evitar errores con mayusculas
        if letra in pais.lower():
            # Añado las letras a la palabra encriptada si son correctas
            palabra_encriptada = "".join(
                # Imprimo la letra si existe en esa posicion de la palabra
                # sino imprimo la letra encriptada
                letra if pais[i].lower() == letra else palabra_encriptada[i] 
                for i in range(len(pais))
            )
            label_palabra.config(text=" ".join(palabra_encriptada))
            
            # Compruebo si ya se han adivinado todas las letras y muestro mensaje de victoria
            if palabra_encriptada.lower() == pais.lower():
                label_mensaje.config(text="¡Has ganado!")
                # Desactivo el botón para que no se pueda seguir adivinando 
                boton_adivinar.config(state = tk.DISABLED)
                
        else: # La letra no existe en la palabra
            # Resto un intento 
            intentos_restantes -= 1
            # Añado la letra a la lista de falladas
            letras_falladas.append(letra)
            # Actualizo el número de intentos en el label 
            label_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
            # Muestro la nueva letra de error en el label
            label_fallos.config(text="Letras incorrectas: " + ", ".join(letras_falladas))
        
            # Verifico si quedan 0 intentos y muestro mensaje de derrota
            if intentos_restantes == 0:
                label_mensaje.config(text=f"Has perdido. El país era {pais}.")
                # Desactivo el botón para que no se pueda seguir adivinando
                boton_adivinar.config(state=tk.DISABLED)
    
    
    def mostrar_pista():
        """
        Método que actualiza el label para mostrar la pista

        Salida: None.
        """
        label_pista.config(text = f"Pista: {pista}")
        
    # Boton de juego que mostrará el label con la pista
    boton_pista = tk.Button(root3, text="Mostrar pista", command = mostrar_pista)
    boton_pista.pack()

    # Label que muestra información del juego
    label_mensaje = tk.Label(root3, text = "")
    label_mensaje.pack(pady = 25)
    
    # Label que muestra los intentos restantes
    label_intentos = tk.Label(root3, text = f"Intentos restantes: {intentos_restantes}", fg = "Red")
    label_intentos.pack()
    
    # Label que muestra las letras que no están en la palabra
    label_fallos = tk.Label(root3, text = f"Letras falladas: {letras_falladas}", fg = "Red")
    label_fallos.pack(pady = 15)
    
    # Boton que genera el evento de adivinar con la entrada de texto
    boton_adivinar = tk.Button(root3, text = "Adivinar", command = adivinar)
    boton_adivinar.pack()    

def encriptación_cesar():
    """
    Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada 
    por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto (Wikipedia)
    
    Formula cifrado C(resultado) = P(posicion cada letra en la palabra) + K(posiciones a desplazar)
    """
    
    #Creo una nueva ventana en tkinter
    root2 = tk.Toplevel()
    root2.title("Resultado encriptación cesar")
    root2.geometry("300x200")
    root2.configure(bg = "#201E1E")
    
    palabra = palabra_a_buscar()["pais"]
    
    # Label de la nueva ventana que mostrará la palabra
    sin_cifrar = tk.Label(root2, text = f"Palabra sin cifrar: {palabra}")
    sin_cifrar.pack(
        ipadx=5,
        ipady=5,
        expand=True
        )
    
    letras = "abcdefghijklmnñopqrstuvwxyz"
    k = random.randint(1, 10)  # K es el desplazamiento del cifrado 
    palabra_encriptada = ""
    
    for letra in palabra.lower():
        # Busco la posicion de la letra en el string y le sumo el desplazamiento
        suma = letras.find(letra) + k
        # Le digo que la posicion de la letra devuelta no puede ser mayor que la longitud de letras(abecedario)
        modulo = suma % len(letras)
        # Construyo la palabra encriptada añadiendo las letras 
        palabra_encriptada = palabra_encriptada + letras[modulo]
    
    
    # Label de la nueva ventana que mostrará la palabra cifrada
    resultado = tk.Label(root2, text = f"Palabra cifrada: {palabra_encriptada}")
    resultado.pack(ipadx=5, ipady=5, expand=True)

    
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
    

    
    


    


    