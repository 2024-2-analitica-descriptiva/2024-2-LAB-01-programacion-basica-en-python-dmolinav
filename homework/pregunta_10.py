"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    result = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            letter = line.strip().split("\t")[0]
            col_4_elements = line.strip().split("\t")[3].split(",")
            col_4_count = len(col_4_elements)
            col_5_elements = line.strip().split("\t")[4].split(",")
            col_5_count = len(col_5_elements)
            result.append((letter, col_4_count, col_5_count))
        return result
print(pregunta_10())
