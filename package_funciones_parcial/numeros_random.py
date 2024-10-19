import random
'''1.Generar una lista de números enteros aleatorios: Desarrollar
una función que genere de manera aleatoria una lista de 50 
números enteros positivos entre 1 y 100.'''

def generar_lista_random():
    lista = [0] * 50
    for i in range(len(lista)):
        lista[i] = random.randint(1, 100)
    
    return lista