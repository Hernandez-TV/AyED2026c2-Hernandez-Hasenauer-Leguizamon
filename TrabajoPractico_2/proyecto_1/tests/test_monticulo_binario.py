from modules.MonticuloBinario import MonticuloBinario 

monticulo = MonticuloBinario()

monticulo.insertar(5)
monticulo.insertar(3)
monticulo.insertar(8)
monticulo.insertar(1)

while not monticulo.esta_vacio():
    print(monticulo.eliminar_minimo())