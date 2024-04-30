def abrir_archivo(archivo):
    with open(archivo, 'r') as file:
        archivo = file.read()
    return archivo

def identificar_estados()

abrir = input("Indique el archivo que contiene al automata: ")
print(abrir_archivo(abrir))