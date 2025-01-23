"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    records = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            key = line.strip().split("\t")[0]
            column_5 = line.strip().split("\t")[4]
            values = [int(value.split(":")[1]) for value in column_5.split(",")]
            total = sum(values)
            if key in records:
                records[key] += total
            else:
                records[key] = total
        sorted_records = dict(sorted(records.items()))
        return sorted_records
print(pregunta_12())
