"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    records = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            dictionary = line.strip().split("\t")[4]
            pairs = dictionary.split(",")
            for pair in pairs:
                key, _ = pair.split(":")
                if key in records:
                    records[key] += 1
                else:
                    records[key] = 1
        return records
    
print(pregunta_09())