def es_romano_valido(romano):
    romano = romano.upper()
    numeros_romanos_validos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    for char in romano:
        if char not in numeros_romanos_validos:
            return False
    
    conteo = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
    prev_char = ''
    
    for i in range(len(romano)):
        char = romano[i]
        conteo[char] += 1

        if conteo[char] > 3:  # Solo se pueden repetir hasta 3 veces
            return False

        if char == prev_char:
            if char in ['V', 'L', 'D']:  # V, L, D no se deben repetir
                return False

        if i < len(romano) - 1:
            next_char = romano[i + 1]
            if char == 'I' and next_char not in ['V', 'X']: return False
            if char == 'X' and next_char not in ['L', 'C']: return False
            if char == 'C' and next_char not in ['D', 'M']: return False
            if char == 'I' and next_char == 'L': return False
            if char == 'I' and next_char == 'D': return False

        prev_char = char
    return True

def romano_a_entero(romano):
    if not es_romano_valido(romano):
        raise ValueError(f"{romano} no es un número romano válido.")
    
    romano = romano.upper()
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

def es_entero_valido(num):
    return isinstance(num, int) and 1 <= num <= 3999

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

def convertir():
    while True:
        print("\nMenu de Conversión:")
        print("1. Convertir número romano a número entero")
        print("2. Convertir número entero a número romano")
        
        opcion = input("Selecciona una opción (1-2): ").strip()
        
        if opcion == '1':
            numero_romano = input("Ingresa un número romano: ").strip()
            try:
                numero_entero = romano_a_entero(numero_romano)
                print(f"El número romano {numero_romano} es {numero_entero} en entero.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == '2':
            try:
                numero_entero = int(input("Ingresa un número entero (1-3999): ").strip())
                numero_romano = entero_a_romano(numero_entero)
                print(f"El número entero {numero_entero} es {numero_romano} en romano.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 2.")

convertir()
