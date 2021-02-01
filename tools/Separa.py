def leer(nombre):
    arch = open(nombre, 'r', encoding="utf-8")
    data = arch.read().split('>')
    tamanyo = len(data)
    print(tamanyo)
    arch.close()
    return [data, tamanyo]

def escribir(nombre, data):
    arch = open(nombre, 'w', encoding="utf-8")
    dataNew = ('>\n').join(data)
    arch.write(dataNew)
    arch.close()
    return 1

data = leer("Comunidades Indígenas.kml")
escribir("separado3.kml", data[0])

    
