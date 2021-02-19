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
#Importar la libreria OS y math
import os
import math
#Obtener la ruta donde esta alojado el archivo python

cwd = os.getcwd()

#Variable para almacenar los nombres de lor archivos .AS
AS_files = []
#Recorrer la carpeta con cada archivo
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".AS"):
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
#Excentridades
def excentricidad (a, b): 
    num = math.pow(a,2) - math.pow(b,2)
    e = num/ math.pow(a,2)
    e2 = num/ math.pow(b,2)
    return [e, e2]
a = 6378137
b= 6356752.314
ext = excentricidad (a,b)
#Codigo para seleccionar la linea 10 de los archivos .o y solo mostrar las coordenadas x, y, z
O_files = []

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".o"):
            O_files.append(file)
for oFile in O_files:
    with open(oFile) as f:
        line = f.readlines()[9] 
        X= float(line.strip().split(" ")[0])
        Y= float(line.strip().split(" ")[1])
        Z= float(line.strip().split(" ")[3])
        # Radio de los paralelos
        P = math.sqrt( math.pow(X,2) + math.pow(Y,2) )
        #encontrar lamda 
        LAM= math.atan(Y/X)
        #encontrar Thetha
        THETHA = math.atan((Z*a) / (P*b))
        #encontrar phi
        #PHI = math.atan( (Z + ( math.pow(ext[0], 2)*b*math.pow( math.sin(THETHA),3) ) )/(P - (math.pow(ext[1],2) * a * math.pow(math.cos(THETHA),3))) )
        PHI = math.atan((Z + ext[1] *b*math.pow( math.sin(THETHA),3) )/(P - ext[0] * a * math.pow(math.cos(THETHA),3)))
        #encontrar el gran normal
        #N = ( (a) / (math.sqrt( 1 - ( math.pow(ext[1], 2) * math.pow(math.sin(PHI),2) ) ) ) ) ##Esta fórmula está mala
        N = a / (math.sqrt(1-(ext[0])*(math.sin(PHI)**2)))
        #encontrar altura
        H = ( ( P / math.cos(PHI) ) - N)
        #Convertir a grados
        LAM_deg = math.degrees(LAM)
        PHI_deg = math.degrees(PHI)
        print("----------------------------------------")
        #print("Radio:", P)
        print("Lamda:", LAM_deg)
        #print("Thetha", THETHA)
        print("Phi:", PHI_deg)
        #print("N", N)
        print("Altura:", H)
        print("X: ", X, "Y: ", Y, "Z:", Z)
        print("----------------------------------------")
        





