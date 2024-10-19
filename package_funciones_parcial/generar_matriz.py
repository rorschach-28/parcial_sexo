import random
from package_matrices import iniciar_matriz, cargar_codigos_random

'''2.Generar una matriz de caracteres alfanuméricos: Desarrollar 
una función que genere de manera aleatoria una matriz de 6 filas
por 15 columnas (6 listas de 15 elementos cada una),
compuesta de caracteres alfanuméricos (letras y dígitos).'''

def generar_una_matriz():
    matrix = iniciar_matriz(6,15,"")
    cargar_codigos_random(matrix)
    
    return matrix