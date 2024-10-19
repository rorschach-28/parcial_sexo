from package_funciones_parcial import *
from package_matrices import *
from package_inputs import *
from package_arrays import calcular_rango, dar_max, dar_min, validar_lista_creada, ordenar_lista

def parcial_ez_pz():
    lista = []
    
    while True:
        menu = get_int("Bienvenido al parcial Sr. Benitez/Corsaro. Seleccione que punto del examen quiere probar primero: \n [1] Generar lista de números aleatorios \n [2] Ordenar la lista de numeros generada amteriormente. \n [3] Buscar números en rango. \n [4] Obtener número máximo y mínimo del item anterior. \n [5] Generar matriz de caracteres alfanuméricos, utilizando la función desarrollada en el punto 2.")
        
        match menu:
            case 1:
                lista = generar_lista_random()
                print(f'La lista generada es: {lista}')
            case 2:
                if validar_lista_creada(lista):
                    sentido = get_str('Ingresa si querés que el sentido de la lista sea:\n (ascendente)ASC\n (Descendente) DESC\n ','Error, opción inexistente',4).upper()
                    print(f'La lista fue ordenada es tal manera: {ordenar_lista(lista, sentido)}')
            case 3:
                if validar_lista_creada(lista):
                    parte_inf = get_int(f'Ingrese la orientación de la parte inferior en el rango de 1 - 200: ','Error el valor tiene que estar entre 1 y 200',1,200,10)
                    parte_sup = get_int(f'Ingrese la orientación de la parte superior en el rango de 1 - 200: ','Error el valor tiene que estar entre 1 y 200',1,200,10)
                    print(f'CANTIDAD DE NÚMEROS EN EL RANGO: \n[{parte_inf}]-[{parte_sup}]: \n{calcular_rango(parte_inf, parte_sup, lista)}')
            case 4:
                if validar_lista_creada(lista):
                    print(f'El valor máximo es: {dar_max(calcular_rango(parte_inf, parte_sup, lista))}. \nEl valor mínimo es: {dar_min(calcular_rango(parte_inf, parte_sup, lista))}')
            case 5:
                generar_una_matriz(lista)
                print(imprimir_matriz(generar_una_matriz))
            case 6:
                break
            
parcial_ez_pz()