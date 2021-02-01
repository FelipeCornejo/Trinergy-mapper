#FELIPE IGNACIO CORNEJO ILABACA
#06/02/2020
#V4.0
#PROGRAMA ENCARGADO DE COMPRIMIR ARCHIVO .KML Y DIRECTORIO DE IMAGENES PARA KMZ

#Importaciones#
import zipfile
import datetime
import os
from os import listdir
import shutil
#funciones#
def main():
    EXCEL_NAME = "Trinergy Mapper Utility.xlsx"

    list_Logos = listdir("Logos")
    print(list_Logos)
    i = 0
    while i < len(list_Logos):
        list_Logos[i] = "Logos/"+list_Logos[i]
        i+=1
    list_Arch = ["Trinergy Utility Mapped.kml"] + list_Logos

    hoy = datetime.datetime.now()
    
    año = hoy.strftime("%Y")
    mes = hoy.strftime("%m")
    name = "Utility Mapped " + año + "-" + mes + ".kmz"
    path = "Utility Mapped " + año + "-" + mes
    with zipfile.ZipFile(name, "w") as archivo_kmz:
        for i in list_Arch:
            archivo_kmz.write(i)
    
    archivo_kmz.close()

    carpetas = listdir()
    if path in carpetas:
        shutil.rmtree(path)
