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

data = leer("Alimentadores_2017_Trinergy.kml")
'''
data = rompe(data[0], data[1], "<td>EMELARI</td>")
data = rompe(data[0], data[1], "<td>ELIQSA</td>")
data = rompe(data[0], data[1], "<td>ELECDA</td>")
data = rompe(data[0], data[1], "<td>EMELAT</td>")
data = rompe(data[0], data[1], "<td>CHILQUINTA</td>")
data = rompe(data[0], data[1], "<td>CONAFE</td>")
data = rompe(data[0], data[1], "<td>EMELCA</td>")
data = rompe(data[0], data[1], "<td>LITORAL</td>")
print ("borre norte")
'''
data = rompe(data[0], data[1], "<td>CHILECTRA</td>")
data = rompe(data[0], data[1], "<td>EEC</td>")
data = rompe(data[0], data[1], "<td>TIL TIL</td>")
data = rompe(data[0], data[1], "<td>EEPA</td>")
data = rompe(data[0], data[1], "<td>CGED</td>")
data = rompe(data[0], data[1], "<td>LUZANDES</td>")
data = rompe(data[0], data[1], "<td>CGED</td>")
print("borre RM")
data = rompe(data[0], data[1], "<td>COOPELAN</td>")
data = rompe(data[0], data[1], "<td>FRONTEL</td>")
data = rompe(data[0], data[1], "<td>SAESA</td>")
data = rompe(data[0], data[1], "<td>EDELAYSEN</td>")
data = rompe(data[0], data[1], "<td>EDELMAG</td>")
data = rompe(data[0], data[1], "<td>CODINER</td>")
data = rompe(data[0], data[1], "<td>EDECSA</td>")
data = rompe(data[0], data[1], "<td>CEC</td>")
data = rompe(data[0], data[1], "<td>LUZLINARES</td>")
data = rompe(data[0], data[1], "<td>LUZPARRAL</td>")
data = rompe(data[0], data[1], "<td>COPELEC</td>")
data = rompe(data[0], data[1], "<td>COELCHA</td>")
data = rompe(data[0], data[1], "<td>SOCOEPA</td>")
data = rompe(data[0], data[1], "<td>COOPREL</td>")
data = rompe(data[0], data[1], "<td>LUZOSORNO</td>")
data = rompe(data[0], data[1], "<td>CRELL</td>")
print("termine")

escribir("Alimentadores_NORTE.kml", data[0])

