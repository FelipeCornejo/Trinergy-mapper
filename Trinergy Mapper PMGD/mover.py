#FELIPE IGNACIO CORNEJO ILABACA
#06/02/2020
#V4.0
#PROGRAMA ENCARGADO DE CREAR CARPPETA Y MOVER ARCHIVOS A ELLA

#Importaciones#
import datetime
import os
from os import listdir
import shutil

def mover():

    EXCEL_NAME = "Trinergy Mapper PMGD.xlsx"
    hoy = datetime.datetime.now()
    año = hoy.strftime("%Y")
    mes = hoy.strftime("%m")
    name = "PMGD Mapped " + año + "-" + mes + ".kmz"
    path = "PMGD Mapped " + año + "-" + mes
    os.mkdir(path, 0o777)
    shutil.move(name, path)
    shutil.copy(EXCEL_NAME, path)
