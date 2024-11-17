#%% 1. Cabecera
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:05:10 2024

@author: vctr23
"""
#%% 2. Imports
import tkinter as tk
import customtkinter as ctk
import Principal
from PIL import Image

#%% 3. Metodos
def centrar_ventana(root, ancho_ventana):
    alto_pantalla = root.winfo_screenheight()
    ancho_pantalla = root.winfo_screenwidth()
    alto_ventana = int((alto_pantalla * ancho_ventana)/ancho_pantalla)
    
    pos_x = int(ancho_pantalla/2 - ancho_ventana/2)
    pos_y = int(alto_pantalla/2 - alto_ventana/2)
    
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

#%% 4. Clases
class Root():
    """
    Clase que contiene el Root y sus funciones en customtkinter

    Returns -> None.
    """
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        self.root = root
        self.root.title("Cifrador")
        centrar_ventana(self.root, 500)
        self.root.resizable(0, 0)

        self.root.grid_rowconfigure([0, 1, 2], weight = 1)
        self.root.grid_columnconfigure([0, 1], weight = 1)

        self.img = ctk.CTkImage(dark_image=Image.open("Images\\bg_image.png"), size = (275, 300))
        
        self.image_lbl = ctk.CTkLabel(self.root, image = self.img, text = "")
        self.image_lbl.grid(rowspan = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)

        self.cesar = ctk.CTkButton(self.root, text = "Encriptación Cesar", command = self.abrir_encriptación, 
                                   corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                   fg_color = "transparent", font=("Roboto", 14))
        self.cesar.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = tk.EW)
        
        self.ahorcado = ctk.CTkButton(self.root, text = "Juego ahorcado", command = self.abrir_juego, 
                                      corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                      fg_color = "transparent", font=("Roboto", 14))
        self.ahorcado.grid(row = 1,  column = 1, padx = 20, pady = 20, sticky = tk.EW)

        self.salir = ctk.CTkButton(self.root, text = "Salir", command= lambda: root.destroy() , 
                                   corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                   fg_color = "transparent", font=("Roboto", 14))
        self.salir.grid(row = 2, column = 1, sticky = tk.EW, padx = 50, pady = 20)

    def abrir_encriptación(self):
        palabra, palabra_encriptada = Principal.encriptación_cesar()
        self.ventana_encriptacion = EncriptaciónCesar(self.root, palabra, palabra_encriptada)
  
    def abrir_juego(self):
        funciones = Principal.juego()
        self.ventana_juego = JuegoAhorcado(self.root, funciones["palabra_encriptada"], 
                                           funciones["intentos_restantes"],
                                           funciones["adivinar"], funciones["mostrar_pista"])

class EncriptaciónCesar():
    """
    Clase que contiene un TopLevel de encriptación_cesar

    Returns -> None.
    """
    def __init__(self, root, palabra, palabra_encriptada):
        self.root1 = ctk.CTkToplevel(root)
        self.root1.title("Resultado encriptación cesar")
        self.root1.attributes("-topmost", True)    # Fuerzo que aparezca encima de todas
        centrar_ventana(self.root1, 400)
        self.root1.resizable(0, 0)

        self.root1.grid_rowconfigure([0, 1], weight = 1)
        self.root1.grid_columnconfigure(0, weight = 1)

        self.sin_cifrar = ctk.CTkLabel(self.root1, text = f"Palabra/s sin cifrar: {palabra}",
                                    font=("Roboto", 20))
        self.sin_cifrar.grid(row = 0, column = 0, sticky = tk.EW, padx = 20)

        self.resultado = ctk.CTkLabel(self.root1, text = f"Palabra cifrada: {palabra_encriptada}",
                                      font=("Roboto", 20))
        self.resultado.grid(row = 1, column = 0, sticky = tk.EW, padx = 20)

class JuegoAhorcado():
    """
    Clase que tiene un toplevel del juego ahorcado

    Returns -> None.
    """
    def __init__(self, root, palabra_encriptada, intentos_restantes, adivinar, mostrar_pista):
        self.root2 = ctk.CTkToplevel(root)
        self.root2.title("Juego Ahorcado")
        self.root2.attributes("-topmost", True)
        centrar_ventana(self.root2, 525)
        self.root2.resizable(0, 0)

        self.root2.grid_rowconfigure([0, 1, 2, 3, 4], weight = 1)
        self.root2.grid_columnconfigure([0, 1, 2], weight = 1)

        self.label_palabra = ctk.CTkLabel(self.root2, text= f"{palabra_encriptada}", font = ("Roboto", 18))
        self.label_palabra.grid(row = 0, columnspan = 3, sticky = tk.EW)

        self.entrada = ctk.CTkEntry(self.root2, font = ("Roboto", 15))
        self.entrada.grid(row = 1, columnspan = 3, sticky = tk.EW)

        self.label_mensaje = ctk.CTkLabel(self.root2, text= "", font = ("Roboto", 16))
        self.label_mensaje.grid(row = 2, columnspan = 3, sticky = tk.EW)

        self.label_pista = ctk.CTkLabel(self.root2, text= "", font = ("Roboto", 15))
        self.label_pista.grid(row = 3, column = 1, sticky = tk.EW)

        self.label_intentos = ctk.CTkLabel(self.root2, text= f"Intentos restantes: {intentos_restantes}", 
                                           font = ("Roboto", 15))
        self.label_intentos.grid(row = 3, column = 0, sticky = tk.W, padx = 10)

        self.label_fallos = ctk.CTkLabel(self.root2, text= f"Letras falladas: ", 
                                         font = ("Roboto", 15), text_color = "#CE4848")
        self.label_fallos.grid(row = 3, column = 2, sticky = tk.E, padx = 10)

        self.boton_adivinar = ctk.CTkButton(self.root2, text= "Adivinar", 
                                            command = lambda: adivinar(self.entrada.get(), self.actualizar_gui, self.entrada), 
                                            font = ("Roboto", 15),  corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                            fg_color = "transparent")
        self.boton_adivinar.grid(row = 4, column = 1, sticky = tk.EW, padx = 10)

        self.boton_pista = ctk.CTkButton(self.root2, text= "Mostrar Pista", 
                                        command = lambda: mostrar_pista(self.label_pista), 
                                        font = ("Roboto", 15),  corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                        fg_color = "transparent")
        self.boton_pista.grid(row = 4, column = 0, sticky = tk.EW, padx = 10)

        self.boton_reiniciar = ctk.CTkButton(self.root2, text = "Reiniciar", 
                                            command= lambda: self.reiniciar(root),
                                            corner_radius = 30, border_width = 1, border_color = "#FFCC70", 
                                            fg_color = "transparent", font = ("Roboto", 15))
        self.boton_reiniciar.grid(row = 4, column = 2, sticky = tk.E, padx = 10)

    def actualizar_gui(self, mensaje, palabra_encriptada, intentos_restantes, letras_falladas):
        self.label_mensaje.configure(text=mensaje)
        self.label_palabra.configure(text=palabra_encriptada)
        self.label_intentos.configure(text=f"Intentos restantes: {intentos_restantes}")
        self.label_fallos.configure(text=f"Letras falladas: {', '.join(letras_falladas)}")

    def reiniciar(self, root):
        self.root2.destroy()
        funciones = Principal.juego()
        self.root2 = JuegoAhorcado(root, funciones["palabra_encriptada"], 
                                           funciones["intentos_restantes"],
                                           funciones["adivinar"], funciones["mostrar_pista"])

