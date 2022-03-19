
#Douce german 17-3-2022 
#para el programa de encuestas

def escribir_nuevo_archivo(NOMBRE_NUEVO_ARCHIVO: str, nuevo_archivo:list):
    with open(NOMBRE_NUEVO_ARCHIVO, "w", encoding="UTF-8") as archivo:
        for rengon in nuevo_archivo:
            archivo.write(rengon+"\n")


def cambiar_delimitador(linea: str) -> str:
    
    linea = linea.replace(",",";")

    return linea


def leer_archivo(NOMBRE_ARCHIVO: str,nuevo_archivo: list) -> bool:
    
    res = True
    try:
        with open(NOMBRE_ARCHIVO, newline='') as archivo:

            for linea in archivo:
                linea = linea.strip()

                linea = cambiar_delimitador(linea)

                nuevo_archivo.append(linea)

    except FileNotFoundError:
        res = False
        print("\n\t\t\t","NO SE PUDO ABRIR EL ARCHIVO",NOMBRE_ARCHIVO,"\n")
    
    return res


def main():
    
    nombre_archivo = input("ingrese el nombre del archivo cuyos separadores desea cambiar de coma a punto y coma: ")
    NOMBRE_ARCHIVO_CSV = nombre_archivo
    NOMBRE_NUEVO_ARCHIVO = "nuevo"+"_"+NOMBRE_ARCHIVO_CSV


    nuevo_archivo = list()

    res = leer_archivo(NOMBRE_ARCHIVO_CSV, nuevo_archivo)
    while not res:
        print("No se pudo abrir el archio. coloquelo en el mismo directorio que este script. Luego presione enter\n")
        input()
        res = leer_archivo(nuevo_archivo)
    
    escribir_nuevo_archivo(NOMBRE_NUEVO_ARCHIVO,nuevo_archivo)


main()