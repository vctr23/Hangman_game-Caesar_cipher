#%% 1. Cabecera
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:21:02 2024

@author: vctr23
"""

#%% 2. Imports
from flask import Flask, jsonify

#%% 3. Código
app = Flask(__name__)

# Ruta de flask que contiene la lista y la convierte a json
@app.route("/lista", methods = ["GET"])
def leer_lista():
        lista_paises = [
            {"pais": "España", "pista": "toros"},
            {"pais": "Francia", "pista": "torre"},
            {"pais": "Italia", "pista": "pizza"},
            {"pais": "Alemania", "pista": "cerveza"},
            {"pais": "Portugal", "pista": "fado"},
            {"pais": "Reino Unido", "pista": "islas"},
            {"pais": "Irlanda", "pista": "trebol"},
            {"pais": "Grecia", "pista": "mitos"},
            {"pais": "Suiza", "pista": "alpes"},
            {"pais": "Belgica", "pista": "chocolate"},
            {"pais": "Austria", "pista": "vals"},
            {"pais": "Suecia", "pista": "vikingos"},
            {"pais": "Noruega", "pista": "fiordos"},
            {"pais": "Dinamarca", "pista": "lego"},
            {"pais": "Paises Bajos", "pista": "tulipanes"},
            {"pais": "Finlandia", "pista": "sauna"},
            {"pais": "Polonia", "pista": "pierogi"},
            {"pais": "Hungria", "pista": "goulash"},
            {"pais": "Rusia", "pista": "matrioska"},
            {"pais": "Ucrania", "pista": "trigo"},
            {"pais": "Rumania", "pista": "dracula"},
            {"pais": "Bulgaria", "pista": "rosa"},
            {"pais": "Serbia", "pista": "balcanes"},
            {"pais": "Croacia", "pista": "playas"},
            {"pais": "Eslovenia", "pista": "cuevas"},
            {"pais": "Eslovaquia", "pista": "castillos"},
            {"pais": "Estonia", "pista": "balti"},
            {"pais": "Letonia", "pista": "riga"},
            {"pais": "Lituania", "pista": "vilna"},
            {"pais": "Monaco", "pista": "casino"},
            {"pais": "Luxemburgo", "pista": "banco"},
            {"pais": "Malta", "pista": "isla"},
            {"pais": "Chipre", "pista": "afrodita"},
            {"pais": "Bosnia y Herzegovina", "pista": "puente"},
            {"pais": "Macedonia del Norte", "pista": "alejandria"},
            {"pais": "Montenegro", "pista": "adriatico"},
            {"pais": "Albania", "pista": "aguila"},
            {"pais": "Islandia", "pista": "volcanes"},
            {"pais": "Kosovo", "pista": "independencia"},
            {"pais": "Republica Checa", "pista": "praga"},
            {"pais": "San Marino", "pista": "microestado"},
            {"pais": "Vaticano", "pista": "papa"},
            {"pais": "Liechtenstein", "pista": "principe"},
            {"pais": "Andorra", "pista": "pirineos"}
        ]
        return jsonify(lista_paises)
        

#%% 4. Main
def iniciar_aplicacion():
    app.run(debug = True, use_reloader = False)

