#%% 1. Cabecera
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:05:10 2024

@author: vctr23
"""
#%% 2. Imports
import tkinter as tk
import customtkinter as ctk
from Principal import encriptación_cesar, juego


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
    Clase que contiene la parte gráfica en tkinter
    Solo tiene el root que lleva al resto de funciones

    Returns
    -------
    None.

    """
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        self.root = root
        self.root.title("Cifrador")
        centrar_ventana(self.root, 500)
        self.root.resizable(0, 0)

        self.root.grid_rowconfigure([0, 1, 2], weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)

        

        self.cesar = ctk.CTkButton(self.root, text = "Encriptación Cesar", command = encriptación_cesar, corner_radius = 30,
                            border_width = 1, border_color = "#FFCC70", fg_color = "transparent")
        self.cesar.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = tk.EW)
        
        self.ahorcado = ctk.CTkButton(self.root, text = "Juego ahorcado", command = juego, corner_radius = 30,
                            border_width = 1, border_color = "#FFCC70", fg_color = "transparent")
        self.ahorcado.grid(row = 1,  column = 0, padx = 20, pady = 20, sticky = tk.EW)

        self.salir = ctk.CTkButton(self.root, text = "Salir", command= lambda: root.destroy() , corner_radius = 30,
                            border_width = 1, border_color = "#FFCC70", fg_color = "transparent")
        self.salir.grid(row = 2, column = 0, sticky = tk.EW, padx = 50, pady = 20)

class EncriptaciónCesar():
    """
    Para commits futuros
    """
    def __init__(self):
        pass

class JuegoAhorcado():
    """
    Para commits futuros
    """
    def __init__(self) -> None:
        pass

#%% 5. Main
