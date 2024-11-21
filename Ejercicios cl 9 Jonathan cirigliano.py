#1 calcular promedio de notas
def calcular_promedio():
    # Pedir ingreso de notas al usuario
    notas = input("Ingresa las notas separadas por un espacio: ").split()
    
    # Convertir las notas a números
    notas = [float(nota) for nota in notas]
    
    # Calcular el promedio
    promedio = sum(notas) / len(notas)
    
    # Mostrar el resultado
    print(f"El promedio de las notas es: {promedio:.2f}")


# Llamar a la función
calcular_promedio()

#2 Colores Primarios
def verificar_color_primario(color):
    """
    Determina si un color es primario y lo indica en pantalla.
    """
    # Lista de colores primarios
    colores_primarios = ["rojo", "azul", "amarillo"]

    # Verificar si el color está en la lista
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")


# Llamar a la función
color_usuario = input("Ingresa un color: ")
verificar_color_primario(color_usuario)


#3 Numero Mayor de la Serie

def numero_mayor():
    """
    Solicita al usuario una serie de N números y determina cuál es el mayor.
    """
    try:
        # Solicitar los números al usuario separados por un espacio
        numeros = input("Ingresa una serie de números separados por un espacio: ").split()
        
        # Convertir los números a enteros o flotantes
        numeros = [float(num) for num in numeros]
        
        # Determinar el número mayor
        mayor = max(numeros)
        
        # Mostrar el resultado
        print(f"El número mayor de la serie es: {mayor}")
    
    except ValueError:
        print("Por favor, ingresa solo números válidos.")


# Llamar a la función
numero_mayor()

#4 
def dibujar_rectangulo():
    """
    Solicita al usuario el número de filas y columnas y dibuja un rectángulo con '*'.
    """
    try:
        # Solicitar dimensiones del rectángulo
        filas = int(input("Ingresa el número de filas: "))
        columnas = int(input("Ingresa el número de columnas: "))
        
        if filas <= 0 or columnas <= 0:
            print("Las filas y columnas deben ser mayores a cero.")
            return
        
        # Dibujar el rectángulo
        for _ in range(filas):
            print("*" * columnas)
    
    except ValueError:
        print("Por favor, ingresa solo números enteros.")


# Llamar a la función
dibujar_rectangulo()

#5 factorial de un numero 
def calcular_factorial():
    """
    Solicita un número entero positivo y calcula su factorial.
    """
    try:
        # Solicitar el número al usuario
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Validar que el número sea positivo
        if numero < 0:
            print("El número debe ser entero y positivo.")
            return
        
        # Calcular el factorial utilizando un bucle
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        
        # Mostrar el resultado
        print(f"El factorial de {numero} es: {factorial}")
    
    except ValueError:
        print("Por favor, ingresa un número entero válido.")


# Llamar a la función
calcular_factorial()
