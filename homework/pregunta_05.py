"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    letter_max_min = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            letter = columns[0]
            value = int(columns[1])
            if letter in letter_max_min:
                letter_max_min[letter][0] = max(letter_max_min[letter][0], value)
                letter_max_min[letter][1] = min(letter_max_min[letter][1], value)
            else:
                letter_max_min[letter] = [value, value]

    result = [
        (letter, values[0], values[1])
        for letter, values in sorted(letter_max_min.items())
    ]
    return result

print(pregunta_05())
