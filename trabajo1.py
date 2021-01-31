# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:00:53 2021

@author: DELL
"""

"""
------------------------------------------------
-------------------- PASO 1 --------------------
------------------------------------------------
"""
#Importar la libreria OS
import os
#Obtener la ruta donde esta alojado el archivo python
cwd = os.getcwd()
#Variable para almacenar los nombres de lor archivos .AS
AS_files = []
#Recorrer la carpeta con cada archivo
for root, dirs, files in os.walk(cwd):
    for file in files:
        if(file.split(".")[1] == "AS"):
            AS_files.append(file)
            
"""
------------------------------------------------
-------------------- PASO 2 --------------------
------------------------------------------------
"""
#Recorrer nombres de archivos .AS y convertirlos a un nuevo archivo .o
"""
for archivoAS in AS_files:
    os.system("teqc -O.dec 30 +obs {}.o {}".format(archivoAS.split("_")[0],archivoAS))
""" 

"""
------------------------------------------------
-------------------- PASO 3 --------------------
------------------------------------------------
"""
#Variable para almacenar los nombres de lor archivos .AS
O_files = []
#Recorrer la carpeta con cada archivo
for root, dirs, files in os.walk(cwd):
    for file in files:
        if(file.split(".")[1] == "o"):
            O_files.append(file)
for oFile in O_files:
    with open(oFile) as f:
        line = f.readlines()[9]
        print(line.strip().split(" ")[0], line.strip().split(" ")[1], line.strip().split(" ")[3])
        
