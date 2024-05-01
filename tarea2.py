def abrir_archivo(archivo):
    with open(archivo, 'r') as file:
        automata = file.readlines()
    return automata

def identificar_estados(automata):
    #encontrar estado inicial
    for linea in automata:
        if linea[0] == '>':
            estado_inicial = linea[1]
    return estado_inicial



abrir = input("Indique el archivo que contiene al automata: ")
print(abrir_archivo(abrir))