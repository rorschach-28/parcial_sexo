def dar_max(lista):
    maximo = float("-inf")                                                          
    for i in range(len(lista)):                 
        if lista[i] > maximo:
            maximo = lista[i]  
    return maximo   

def dar_min(lista):
    minimo = float("inf")                                                         
    for i in range(len(lista)):                 
        if lista[i] < minimo:
            minimo = lista[i] 
        
    return minimo

def lista_str(lista):
    string = ""
    for i in range(len(lista)):
        string += lista[i]
    return string

def printear_todo(lista) -> list:
    for i in range(len(lista)):
        print(lista[i])

def validar_lista(lista):
    return lista != []

def validar_lista_creada(lista):
    if validar_lista(lista):
        return True
    else:
        print("\n Error, antes de hacer esto tenés que iniciar la lista (seleccionar opción 1) \n")
        return False


def calcular_rango(parte_inf, parte_sup, lista):
    lista_nueva = [] #inicializa la lista donde va a ir an
    for i in range(len(lista)):
        if parte_inf <= lista[i] <= parte_sup:
            lista_nueva += [lista[i]]
    if validar_lista(lista_nueva):
        return lista_nueva
    else:
        return "no hay numeros en ese rango"

