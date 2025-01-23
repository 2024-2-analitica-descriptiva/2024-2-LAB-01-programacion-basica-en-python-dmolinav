"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    values_by_key = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) < 5:
                continue  
            dictionary_str = columns[4]
            pairs = dictionary_str.split(",")
            for pair in pairs:
                current_key, value = pair.split(":")
                value = int(value)
                if current_key in values_by_key:
                    values_by_key[current_key][0] = min(
                        values_by_key[current_key][0], value)
                    values_by_key[current_key][1] = max(
                        values_by_key[current_key][1], value)
                else:
                    values_by_key[current_key] = [value, value]
   
    result = [
        (key, values[0], values[1])
        for key, values in sorted(values_by_key.items())
    ]
    return result

print("[")
for key, min_val, max_val in pregunta_06():
    print(f"('{key}', {min_val}, {max_val}),")
print("]")

