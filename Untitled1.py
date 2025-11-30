## 📐 Código en Python para calcular el Área de un Triángulo

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    Argumentos:
    base (float): La longitud de la base del triángulo.
    altura (float): La altura perpendicular a la base.

    Retorna:
    float: El área calculada del triángulo.
    """
    # Fórmula del área: (base * altura) / 2
    area = (base * altura) / 2
    return area

# --- EJEMPLO DE USO ---

# Definir los valores de la base y la altura
base_ejemplo = 10.0
altura_ejemplo = 5.0

# Llamar a la función
area_calculada = calcular_area_triangulo(base_ejemplo, altura_ejemplo)

# Mostrar el resultado
print(f"La base del triángulo es: {base_ejemplo}")
print(f"La altura del triángulo es: {altura_ejemplo}")
print(f"El área del triángulo es: {area_calculada}")