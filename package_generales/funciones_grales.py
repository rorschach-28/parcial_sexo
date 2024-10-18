import random

'''
largo: 50
cant: 0 - 100
EJECUCIÓN: 
1) crear variable lista e inicializarla (listo)
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
2) cargarle los elementos (Se requiere RECORRIDO -> bucle for )
3)cada elemento tiene que ser un número aleatorio
4) devolverme esa lista

'''
def lista_aleatorios():
    lista = [0] * 50
    for i in range(len(lista)):
        lista[i] = random.randint(1, 100)

    return lista



import random
from package_matrices import iniciar_matriz,cargar_codigos_random

def biblioteca():
    
    biblio = iniciar_matriz(6,15,"")
    cargar_codigos_random(biblio)

    return biblio




def ordenar_vector(lista,orientacion = "ASC"):
    if orientacion == "ASC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] > lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
        return lista
    elif orientacion == "DESC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] < lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
    return lista

'''
VALIDAR: 

                        Ver si hay error
-> si no hay                                    ->si hay
    no pasa nada                                    modificarlo

'''
## TRUE elemento = alpha, elemento = num, elemento = alnumeric 
def validar_ingreso_alfnum(elemento):
    return tiene_numero(elemento) and tiene_string(elemento)

def tiene_numero(elemento):
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isnumeric():
            flag = True
    return flag

def tiene_string(elemento):
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isalpha():
            flag = True
    return flag