def leer(nombre):
    arch = open(nombre, 'r', encoding="utf-8")
    data = arch.read().split('\n')
    tamanyo = len(data)
    print(tamanyo)
    arch.close()
    return [data, tamanyo]

def escribir(nombre, data):
    arch = open(nombre, 'w', encoding="utf-8")
    dataNew = ('\n').join(data)
    arch.write(dataNew)
    arch.close()
    return 1

def rompe(data, largo, tag):
    i = 0
    while i<largo:
        if tag in data[i]:
            print ("HORA DEL MARTILLO!!\n")
            final = i
            parar = False
            while not parar:
                if "/Placemark" in data[final]:
                    parar = True
                else:
                    final += 1
            inicio = i
            parar = False
            while not parar:
                if "Placemark" in data[inicio]:
                    parar = True
                else:
                    inicio -= 1
            while not (inicio == final):
                data.pop(inicio)
                final -= 1
            print(data[inicio])
            print("NO PUEDES HUIR\n")
        largo = len(data)
        i += 1
    return [data, largo]

data = leer("Titulos Merced Araucania.kml")
'''
data = rompe(data[0], data[1], "COLLIPULLI")
data = rompe(data[0], data[1], "CURACAUTIN")
data = rompe(data[0], data[1], "LONQUIMAY")
data = rompe(data[0], data[1], "VICTORIA")
data = rompe(data[0], data[1], "ERCILLA")#tercera division
'''
data = rompe(data[0], data[1], "LUMACO")
data = rompe(data[0], data[1], "PUREN")
data = rompe(data[0], data[1], "ANGOL")
data = rompe(data[0], data[1], "RENAICO")
data = rompe(data[0], data[1], "TRAIGUEN")
data = rompe(data[0], data[1], "LOS SAUCES")#cuarta division

data = rompe(data[0], data[1], "CARAHUE")
data = rompe(data[0], data[1], "SAAVEDRA")
data = rompe(data[0], data[1], "TEODORO SCHMIDT")
data = rompe(data[0], data[1], "TOLTEN")
data = rompe(data[0], data[1], "NUEVA IMPERIAL")
data = rompe(data[0], data[1], "GALVARINO")
data = rompe(data[0], data[1], "GORBEA")
data = rompe(data[0], data[1], "LONCOCHE")
data = rompe(data[0], data[1], "TEMUCO")
data = rompe(data[0], data[1], "PADRE LAS CASAS")
data = rompe(data[0], data[1], "FREIRE")
data = rompe(data[0], data[1], "PITRUFQUEN")
data = rompe(data[0], data[1], "CHOLCHOL")#primera division
data = rompe(data[0], data[1], "PERQUENCO")
data = rompe(data[0], data[1], "LAUTARO")
data = rompe(data[0], data[1], "VILCUN")
data = rompe(data[0], data[1], "CUNCO")
data = rompe(data[0], data[1], "VILLARRICA")
data = rompe(data[0], data[1], "PUCON")
data = rompe(data[0], data[1], "CURARREHUE")
data = rompe(data[0], data[1], "MELIPEUCO")#segunda division


escribir("Titulos Merced - Region IX Cordillera Norte.kml", data[0])

data = leer("Titulos Merced Araucania.kml")
data = rompe(data[0], data[1], "COLLIPULLI")
data = rompe(data[0], data[1], "CURACAUTIN")
data = rompe(data[0], data[1], "LONQUIMAY")
data = rompe(data[0], data[1], "VICTORIA")
data = rompe(data[0], data[1], "ERCILLA")#tercera division
'''
data = rompe(data[0], data[1], "LUMACO")
data = rompe(data[0], data[1], "PUREN")
data = rompe(data[0], data[1], "ANGOL")
data = rompe(data[0], data[1], "RENAICO")
data = rompe(data[0], data[1], "TRAIGUEN")
data = rompe(data[0], data[1], "LOS SAUCES")#cuarta division
'''
data = rompe(data[0], data[1], "CARAHUE")
data = rompe(data[0], data[1], "SAAVEDRA")
data = rompe(data[0], data[1], "TEODORO SCHMIDT")
data = rompe(data[0], data[1], "TOLTEN")
data = rompe(data[0], data[1], "NUEVA IMPERIAL")
data = rompe(data[0], data[1], "GALVARINO")
data = rompe(data[0], data[1], "GORBEA")
data = rompe(data[0], data[1], "LONCOCHE")
data = rompe(data[0], data[1], "TEMUCO")
data = rompe(data[0], data[1], "PADRE LAS CASAS")
data = rompe(data[0], data[1], "FREIRE")
data = rompe(data[0], data[1], "PITRUFQUEN")
data = rompe(data[0], data[1], "CHOLCHOL")#primera division

data = rompe(data[0], data[1], "PERQUENCO")
data = rompe(data[0], data[1], "LAUTARO")
data = rompe(data[0], data[1], "VILCUN")
data = rompe(data[0], data[1], "CUNCO")
data = rompe(data[0], data[1], "VILLARRICA")
data = rompe(data[0], data[1], "PUCON")
data = rompe(data[0], data[1], "CURARREHUE")
data = rompe(data[0], data[1], "MELIPEUCO")#segunda division


escribir("Titulos Merced - Region IX Costa norte.kml", data[0])

data = leer("Titulos Merced Araucania.kml")
data = rompe(data[0], data[1], "COLLIPULLI")
data = rompe(data[0], data[1], "CURACAUTIN")
data = rompe(data[0], data[1], "LONQUIMAY")
data = rompe(data[0], data[1], "VICTORIA")
data = rompe(data[0], data[1], "ERCILLA")#tercera division
data = rompe(data[0], data[1], "LUMACO")
data = rompe(data[0], data[1], "PUREN")
data = rompe(data[0], data[1], "ANGOL")
data = rompe(data[0], data[1], "RENAICO")
data = rompe(data[0], data[1], "TRAIGUEN")
data = rompe(data[0], data[1], "LOS SAUCES")#cuarta division
'''
data = rompe(data[0], data[1], "CARAHUE")
data = rompe(data[0], data[1], "SAAVEDRA")
data = rompe(data[0], data[1], "TEODORO SCHMIDT")
data = rompe(data[0], data[1], "TOLTEN")
data = rompe(data[0], data[1], "NUEVA IMPERIAL")
data = rompe(data[0], data[1], "GALVARINO")
data = rompe(data[0], data[1], "GORBEA")
data = rompe(data[0], data[1], "LONCOCHE")
data = rompe(data[0], data[1], "TEMUCO")
data = rompe(data[0], data[1], "PADRE LAS CASAS")
data = rompe(data[0], data[1], "FREIRE")
data = rompe(data[0], data[1], "PITRUFQUEN")
data = rompe(data[0], data[1], "CHOLCHOL")#primera division
'''
data = rompe(data[0], data[1], "PERQUENCO")
data = rompe(data[0], data[1], "LAUTARO")
data = rompe(data[0], data[1], "VILCUN")
data = rompe(data[0], data[1], "CUNCO")
data = rompe(data[0], data[1], "VILLARRICA")
data = rompe(data[0], data[1], "PUCON")
data = rompe(data[0], data[1], "CURARREHUE")
data = rompe(data[0], data[1], "MELIPEUCO")#segunda division


escribir("Titulos Merced - Region IX Costa Sur.kml", data[0])

data = leer("Titulos Merced Araucania.kml")
data = rompe(data[0], data[1], "COLLIPULLI")
data = rompe(data[0], data[1], "CURACAUTIN")
data = rompe(data[0], data[1], "LONQUIMAY")
data = rompe(data[0], data[1], "VICTORIA")
data = rompe(data[0], data[1], "ERCILLA")#tercera division
data = rompe(data[0], data[1], "LUMACO")
data = rompe(data[0], data[1], "PUREN")
data = rompe(data[0], data[1], "ANGOL")
data = rompe(data[0], data[1], "RENAICO")
data = rompe(data[0], data[1], "TRAIGUEN")
data = rompe(data[0], data[1], "LOS SAUCES")#cuarta division

data = rompe(data[0], data[1], "CARAHUE")
data = rompe(data[0], data[1], "SAAVEDRA")
data = rompe(data[0], data[1], "TEODORO SCHMIDT")
data = rompe(data[0], data[1], "TOLTEN")
data = rompe(data[0], data[1], "NUEVA IMPERIAL")
data = rompe(data[0], data[1], "GALVARINO")
data = rompe(data[0], data[1], "GORBEA")
data = rompe(data[0], data[1], "LONCOCHE")
data = rompe(data[0], data[1], "TEMUCO")
data = rompe(data[0], data[1], "PADRE LAS CASAS")
data = rompe(data[0], data[1], "FREIRE")
data = rompe(data[0], data[1], "PITRUFQUEN")
data = rompe(data[0], data[1], "CHOLCHOL")#primera division
'''
data = rompe(data[0], data[1], "PERQUENCO")
data = rompe(data[0], data[1], "LAUTARO")
data = rompe(data[0], data[1], "VILCUN")
data = rompe(data[0], data[1], "CUNCO")
data = rompe(data[0], data[1], "VILLARRICA")
data = rompe(data[0], data[1], "PUCON")
data = rompe(data[0], data[1], "CURARREHUE")
data = rompe(data[0], data[1], "MELIPEUCO")#segunda division
'''

escribir("Titulos Merced - Region IX Cordillera Sur.kml", data[0])

