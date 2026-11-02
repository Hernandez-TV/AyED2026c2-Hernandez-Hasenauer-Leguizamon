from modules.arbol_avl import ArbolAVL

def main():
    """Función principal de prueba de Árbol AVL."""
    print("=== TEST AVL ===\n")

    avl = ArbolAVL()

    avl.insertar(30, "A")
    avl.insertar(20, "B")
    avl.insertar(40, "C")
    avl.insertar(10, "D")
    avl.insertar(25, "E")

    print("Buscar 30:")
    print(avl.obtener(30))

    print("\nBuscar 10:")
    print(avl.obtener(10))

    print("\nBuscar 25:")
    print(avl.obtener(25))

    print("\nCantidad de nodos:")
    print(avl._tamanio)

    print("\nActualizando clave 30")

    avl.insertar(30, "MODIFICADO")

    print(avl.obtener(30))

    print("\nTEST FINALIZADO")


if __name__ == "__main__":
    main()