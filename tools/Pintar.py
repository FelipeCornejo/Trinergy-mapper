from os import listdir

def ls(ruta = '.'):
    return listdir(ruta)

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

def pinta(data, largo, tag):
    i = 0
    while i<largo:
        if tag in data[i]:
            print(i)
            print ("PINCELADA MAGISTRAL ♫")
            data.pop(i)
            largo -= 1
        i += 1
    return [data, largo]

lista_arq = ls()
tamano = len(lista_arq)
i = 0
print(lista_arq)
while i < tamano-1:
    print("encontre algo")
    data = leer(lista_arq[i])
    data = pinta(data[0], data[1], "name")
    escribir(lista_arq[i], data[0])
    i += 1
