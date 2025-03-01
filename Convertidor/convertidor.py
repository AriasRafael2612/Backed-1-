
def es_romano_valido(romano):
    romano = romano.upper()  # Convertir a mayúsculas para que acepte minúsculas
    romano_regex = (
        '^'           # Inicio de la cadena
        '(M{0,3})'    # Miles (0-3000)
        '(CM|CD|D?C{0,3})'  # Centenas (900, 400, 0-300)
        '(XC|XL|L?X{0,3})'   # Decenas (90, 40, 0-30)
        '(IX|IV|V?I{0,3})'    # Unidades (9, 4, 0-3)
        '$'           # Fin de la cadena
    )
    import re
    return re.match(romano_regex, romano) is not None

# Función para convertir números romanos a enteros
def romano_a_entero(romano):
    if not es_romano_valido(romano):
        raise ValueError(f"{romano} no es un número romano válido.")
    
    romano = romano.upper()  # Convertir a mayúsculas para el procesamiento
    valores_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    resultado = 0
    for i in range(len(romano) - 1):
        if valores_romanos[romano[i]] < valores_romanos[romano[i + 1]]:
            resultado -= valores_romanos[romano[i]]
        else:
            resultado += valores_romanos[romano[i]]
    
    resultado += valores_romanos[romano[-1]]
    return resultado

# Función para verificar si un número entero es válido para convertir a romano
def es_entero_valido(num):
    return isinstance(num, int) and 1 <= num <= 3999

# Función para convertir números enteros a romanos
def entero_a_romano(num):
    if not es_entero_valido(num):
        raise ValueError("El número debe ser un entero entre 1 y 3999.")
    
    valores_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    romano = ''
    for valor, simbolo in valores_romanos:
        while num >= valor:
            romano += simbolo
            num -= valor
    return romano

# Función principal con verificación de entrada y menú interactivo
def convertir():
    while True:
        print("\nMenu de Conversión:")
        print("1. Convertir número romano a número entero")
        print("2. Convertir número entero a número romano")
        
        opcion = input("Selecciona una opción (1-2): ").strip()
        
        if opcion == '1':
            # Convertir de romano a entero
            numero_romano = input("Ingresa un número romano: ").strip()
            try:
                numero_entero = romano_a_entero(numero_romano)
                print(f"El número romano {numero_romano} es {numero_entero} en entero.")
                break  # Terminar ejecución después de la conversión
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == '2':
            # Convertir de entero a romano
            try:
                numero_entero = int(input("Ingresa un número entero (1-3999): ").strip())
                numero_romano = entero_a_romano(numero_entero)
                print(f"El número entero {numero_entero} es {numero_romano} en romano.")
                break  # Terminar ejecución después de la conversión
            except ValueError as e:
                print(f"Error: {e}")
        
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 2.")

# Ejecutar la función de conversión
convertir()
