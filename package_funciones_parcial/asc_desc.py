'''3.Ordenar una lista de números enteros: Desarrollar una 
función que ordene una lista de números enteros, recibiendo
como parámetro el criterio de ordenamiento "ASC" o "DESC" 
(ascendente o descendente).'''

def ordenar_lista(lista, sentido= "ASC"):
    if sentido == "ASC":
        for i in range(len(lista)): #inicio el for para que vaya analizando la lista 
            for it in range (0, len(lista -i -1)):
                if lista [it] > lista [it + 1]:
                    red = lista[it]
                    lista [it + 1] = red
        return lista
    elif sentido == "DESC":
        for i in range (len(lista)):
            for it in range (0, len(lista) -i -1):
                if lista [it] < lista [it + 1]:
                    red = lista[it]
                    lista [it + 1] = red
        return lista
