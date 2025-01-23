"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    letter_count = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            col_2_value = int(line.strip().split("\t")[1])
            col_4_letters = line.strip().split("\t")[3].split(",")
            for letter in col_4_letters:
                if letter in letter_count:
                    letter_count[letter] += col_2_value
                else:
                    letter_count[letter] = col_2_value

    sorted_letter_count = dict(sorted(letter_count.items()))
    return sorted_letter_count
print(pregunta_11())