# Hangman_game-Caesar_cipher

A github repository to upload my work on python of a Hangman game and also a Caesar Cypher, with (Custom)Tkinter and a LocalHost Flask app (API)

~~You need to run "API.py" first in order for "Principal.py" to work~~

## Changelog
V1.1 -> Changed main on class API to a function ("iniciar_aplicacion") that runs the flask app. This is routed to a process in "Principal.py". Now you don't have to run both scripts at the same time.

V1.2 -> Moved Root window to a diferent file to make "Pricipal.py" a little bit more readable. Changed root window, now uses customtkinter (tkinter is still used for some features).

V1.3 -> Made some minor changes to root window (added an image using pillow). Changed "EncriptaciónCesar" to customtkinter and moved it to "GUI". Erased some non-useful codelines on "Principal.py" (old tkinter windows and some comments)

V1.4 -> Changed "JuegoAhorcado" to customtkinter and moved it to "GUI". Tried to make the code less messy.

V1.5 -> Added a restart button to "JuegoAhorcado".

V1.6 -> Added a logo on root CTk window. Fixed some minor errors on GUI windows.

## License
This project is licensed under the [APACHE LICENSE 2.0](LICENSE).
