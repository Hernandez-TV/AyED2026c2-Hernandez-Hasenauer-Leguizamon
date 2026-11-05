from ayedfiuner.estructuras.arbol_avl import ArbolAVL


def main():

    avl = ArbolAVL()

    avl.insertar(10, "A")
    avl.insertar(20, "B")
    avl.insertar(30, "C")

    print("Raíz esperada: 20")

    print(avl._raiz.clave)


if __name__ == "__main__":
    main()