from funciones import *
import leer_csv
if __name__ == "__main__":

    datos = leer_csv.leer_csv('reduced_question_set.csv')
    iniciar(datos)