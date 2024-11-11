from typing import List
import csv
#Funcion que lee el archivo .csv
def leer_csv(ruta_archivo: str) -> List[List[str]]:
    with open(ruta_archivo, mode='r', newline='', encoding='latin-1') as archivo:
        lector = list(csv.reader(archivo))
        #Solo solo agarra las columnas de pregunta, respuesta y categoria
        lector=list(map(lambda x: [x[5], x[6],x[3]], lector))
        return lector
