def quick_sort(lista):
    """PRE:lista debe contener elementos comparables.
    POST:devuelve una nueva lista ordenada de menor a mayor."""
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = []
    iguales = []
    mayores = []
    for elemento in lista:
        if elemento < pivote:
            menores.append(elemento)
        elif elemento > pivote:
            mayores.append(elemento)
        else:
            iguales.append(elemento)
    return (
        quick_sort(menores)
        + iguales
        + quick_sort(mayores)
        )
