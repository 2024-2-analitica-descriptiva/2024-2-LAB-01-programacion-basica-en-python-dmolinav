"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    record={}
    with open ('files/input/data.csv','r',encoding='utf-8') as file:
        for line in file:
            letter= line.strip().split('\t')[0]
            if letter in record:
                record[letter] += 1
            else:
                record[letter]= 1
    q= sorted (record.items())
    return q\
    
print(pregunta_02())