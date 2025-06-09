import random
import timeit

# Funcion encargada de generar una lista de determinado tamaño
def generate_list(length):
    return [ random.randint(1, length) for _ in range(length) ]

# Testeador de metodo de ordenmiento
def tester(tipo_ordenamiento, lista_chica, lista_grande):

# Testeamos lista chica
    start = timeit.default_timer()

    tipo_ordenamiento(lista_chica)

    end = timeit.default_timer()

    print(f"Tiempo lista chica: {(end - start):.6f} ms")

# Testeamos lista grande
    start = timeit.default_timer()

    tipo_ordenamiento(lista_grande)

    end = timeit.default_timer()

    print(f"Tiempo lista grande: {(end - start):.6f} ms")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento mínimo
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        arr[i], arr[min_index] = arr[min_index], arr[i]



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ingresamos tamaños de listas
lista_chica_size = int(input("Ingrese el tamaño de la lista chica: "))
lista_grande_size = int(input("Ingrese el tamaño de la lista grande: "))
print("\n")

# GENERAMOS LISTAS
lista_chica = generate_list(lista_chica_size)
lista_grande = generate_list(lista_grande_size)


# TESTEAMOS
print("Bubble Sort")
tester(bubble_sort, lista_chica.copy(), lista_grande.copy())
print("\n")

print("Insertion")
tester(insertion_sort, lista_chica.copy(), lista_grande.copy())
print("\n")

print("Selección")
tester(insertion_sort, lista_chica.copy(), lista_grande.copy())
print("\n")

print("Quicksort")
tester(quicksort, lista_chica.copy(), lista_grande.copy())
print("\n")

print("Merge Sort")
tester(quicksort, lista_chica.copy(), lista_grande.copy())
print("\n")



lista_size = int(input("Ingrese el tamaño de a lista que desea: "))

# Generamos lista con elementos únicos
lista = random.sample(range(1, lista_size * 2), lista_size)

# Busqueda lineal
start = timeit.default_timer()

resultado_lineal = busqueda_lineal(lista, 10)

end = timeit.default_timer()

print(f"Lineal: pos: {resultado_lineal} en {(end - start):.6f} ms")

# Ordenamos
insertion_sort(lista)

# Busqueda binaria
start = timeit.default_timer()

resultado_binaria = busqueda_binaria(lista, 10)

end = timeit.default_timer()

print(f"Binaria: pos: {resultado_binaria} en {(end - start):.6f} ms")


print("\n")


# El club cuenta con 60.000 carnets emitidos, en el estadio ingresaron 55_541 personas
ingresos_estadio = random.sample(range(1, 60_000), 55_541)
copia_ingresos_estadio = ingresos_estadio.copy()

# Encargado ingresa ID brindado por el padre
id_buscado = int(input("ID buscado: "))

# Primero realizará un ordenamiento de los IDs de las personas ingresadas ese día
merge_sort(ingresos_estadio)

start = timeit.default_timer()

# Luego realizará una búsqueda
resultado = busqueda_binaria(ingresos_estadio, id_buscado)

end = timeit.default_timer()

print(f"Tiempo estimado sort y binaria {(end-start):.6f} ms")


start = timeit.default_timer()

# Luego realizará una búsqueda
resultado = busqueda_lineal(copia_ingresos_estadio, id_buscado)

end = timeit.default_timer()

print(f"Tiempo estimado lineal {(end-start):.6f} ms")

print("\n")

print(f"Posicion {resultado}")

# Comprobamos, en caso de haber ingresado, que esa posición es el ID
if resultado > 0:
    print(f"La persona ha ingresado al estadio: {ingresos_estadio[resultado]}")
else:
    print("La persona ese día no ha ingresado al estadio.")

