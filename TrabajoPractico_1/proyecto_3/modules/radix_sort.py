def radix_sort(lista):
    """
    PRE:
    La lista debe contener enteros positivos.
    POST:
    Devuelve la lista ordenada de menor a mayor.
    
    """
    if len(lista) == 0:
        return lista
    numero_maximo = max(lista)
    exponente = 1
    while numero_maximo // exponente > 0:
        buckets = [[] for _ in range(10)]
        for numero in lista:
            digito = (numero // exponente) % 10
            buckets[digito].append(numero)
        lista = []
        for bucket in buckets:
            lista.extend(bucket)
        exponente *= 10
    return lista