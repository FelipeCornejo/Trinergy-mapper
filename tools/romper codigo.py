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

def romper(data, tamanyo, tag):
    i = 0
    while i<tamanyo:
        if tag in data[i]:
            print("Es Hora del Martillo\t", i, "\tTOTAL:\t", tamanyo, "\n")
            if "Point" in data[i+9]:
                j = i-9
                print("POOOOOOOOOOOOOOOOOOOOOOOOOOOOINT!!")
                if "/Placemark" in data[i+9]:
                    while j<i+10:
                        data.pop(j)
                        i -= 1
                else:
                    while j<i+12:
                        data.pop(j)
                        i -= 1            
            elif "Polygon" in data[i+9]:
                print("POLYLYLYLYLYLYLYLYLYLYLYLYLYGOOON!!")
                j = i-9
                if "innerBoundaryIs" in data[i+9+8]:
                    while j <= i+9+8+8:
                        data.pop(j)
                        i -= 1
                else:
                    while j <= i+18:
                        data.pop(j)
                        i -= 1
                        
        tamanyo =len(data)
        i += 1
    
    return [data, tamanyo]

data = leer("Titulos_Merced_Indigena 1.kml")
data = romper(data[0],data[1], "IX")
print("\n\nlisto\n\n")
data = romper(data[0],data[1], "VIII")
print("\n\nlisto\n\n")
data = romper(data[0],data[1], "XIV")
print("\n\nlisto\n\n")
escribir ("nombrePrueba4.kml", data[0])
