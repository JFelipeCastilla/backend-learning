"""Lenguaje dinamico: Se refiere a que las variables pueden 
cambiar pore ejemplo, de string a int.
"""

"""Las variables son datos que se almacenan y determinan su 
función en base a el tipo de variable.
"""

# Tipos de datos:
# Tipo texto - Str
# Tipo numerico - int, float, complex
# Tipo secuencia - List, tuple, range
# Tipo mapeo - dict
# Tipo conjunto - set, frozenset
# Tipo boleano - bool
# Tipo binario - bytes, bytearray, memoryview

cadena = input("Type your full name: ")

print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.replace("l", "p"))
print(f"Hola {cadena:50}<---")
print(f"Hola {cadena:^50}<---")
print(f"Hola {cadena:<50}<---")
print(f"Hola {cadena:>50}<---")

"""Python permite tres tipos de base númericas, decimal, binaria,
octal, hexadecimal.
"""

# Operaciones matemáticas de izquierda a derecha cuando son semejantes
# Operaciones de asignación y potenciación son de derecha a izquierda

# Conversión de tipos
cadena = "52"

num = int(cadena)

print(num)
print(type(num))

# Formato de valores numéricos
raiz = 2 **0.5

print(f"Raíz de 2: {raiz:.6f}")