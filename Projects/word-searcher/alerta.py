import os
import json
from functools import reduce
import sys



SEARCH = ["md"]  # Add file extensions to analyze.

# Corregir programa para no pedir esto por consola
nombre_carpeta_revisada = sys.argv[1]

with open("keywords.json") as file:
    KEYWORDS = json.load(file)["keywords"] 

root_dir = os.getcwd()

usernames = list()
for root, dirs, files in os.walk(root_dir, onerror=None):
    #Itera sobre todas las carpetas, subcarpetas y archivos
    for filename in files:
        file_path = os.path.join(root, filename)
        lines = list()
        extension = file_path.split(os.sep)[-1].split(".")[-1] #obtiene la extensión del archivo
        if extension in SEARCH:
            #Revisamos solamente las extensiones que declaramos en la lista SEARCH, línea 10.
            try:
                with open(file_path, "r") as f:
                    for line in f.readlines():
                        lines.append(line.strip().split(" "))
                    lines = reduce(lambda x, y: x + y, lines, [])
                    intersection = [_ for _ in lines if _ in KEYWORDS]
                    if intersection:
                        #Si la lista no está vacía significa que el archivo tenía alguna keyword en él.
                        
                        file_path_list = file_path.split(os.sep)
                        index = file_path_list.index(nombre_carpeta_revisada)
                        
                        #Como los archivos tienen ruta "/TXX/Username", buscamos index de TXX
                        # y el elemento siguiente(index + 1) es su username. Lo agrego a una lista de
                        # usernames "sospechosos"
                        usernames.append(file_path_list[index + 1])
                        
            except (IOError, OSError, UnicodeDecodeError):  
                #Por si las moscas
                pass


usernames = set(usernames)
with open("_filenames.txt", "w") as file:
    #Creamos el archivo _usernames.txt y lo llenamos con los usernames que nos interesan
    file.write("\n".join(usernames))
print("Found", len(usernames), "matching words")
