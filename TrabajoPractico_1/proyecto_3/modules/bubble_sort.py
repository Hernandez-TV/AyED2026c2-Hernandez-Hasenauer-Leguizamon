def bubble_sort(list):
    """PRE:
    lista debe contener elementos comparables.
    POST:
    devuelve la lista ordenada de menor a mayor.
    """
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = (
                list[j + 1],
                list[j]
                )
    return list