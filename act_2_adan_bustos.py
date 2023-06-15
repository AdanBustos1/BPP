# Función 1: Suma de dos números
def sumar(a, b):
    return a + b

# Pruebas para la función sumar
def test_sumar():
    # Prueba 1
    resultado = sumar(2, 3)
    assert resultado == 5, f"Error: Se esperaba 5 pero se obtuvo {resultado}"

    # Prueba 2
    resultado = sumar(-1, 1)
    assert resultado == 0, f"Error: Se esperaba 0 pero se obtuvo {resultado}"

    # Prueba 3
    resultado = sumar(10, -5)
    assert resultado == 5, f"Error: Se esperaba 5 pero se obtuvo {resultado}"

    # Prueba 4
    resultado = sumar(0, 0)
    assert resultado == 0, f"Error: Se esperaba 0 pero se obtuvo {resultado}"

    # Prueba 5
    resultado = sumar(2.5, 1.75)
    assert resultado == 4.25, f"Error: Se esperaba 4.25 pero se obtuvo {resultado}"

# Función 2: Verificar si un número es par
def es_par(num):
    return num % 2 == 0

# Pruebas para la función es_par
def test_es_par():
    # Prueba 1
    resultado = es_par(4)
    assert resultado == True, f"Error: Se esperaba True pero se obtuvo {resultado}"

    # Prueba 2
    resultado = es_par(7)
    assert resultado == False, f"Error: Se esperaba False pero se obtuvo {resultado}"

    # Prueba 3
    resultado = es_par(0)
    assert resultado == True, f"Error: Se esperaba True pero se obtuvo {resultado}"

    # Prueba 4
    resultado = es_par(-2)
    assert resultado == True, f"Error: Se esperaba True pero se obtuvo {resultado}"

    # Prueba 5
    resultado = es_par(3.5)
    assert resultado == False, f"Error: Se esperaba False pero se obtuvo {resultado}"

# Ejecutar las pruebas
test_sumar()
test_es_par()