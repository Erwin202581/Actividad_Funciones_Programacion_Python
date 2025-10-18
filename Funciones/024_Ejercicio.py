# Combinar obligatorio y *args

def resumen_productos(categoria, *productos):

    print("\n---Ejercicio 24---")
    print(f"Resumen de la Categoria: {categoria}")
    print(f"Total productos: {len(productos)}")
    print(f"Lista: {productos}\n")
    

resumen_productos("Electrónica", "TV", "Movil", "Tablet")
