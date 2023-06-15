"""import pdb

def obtener_maximos(listas):
    pdb.set_trace()
    return [max(sublista) for sublista in listas]

listas = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]

maximos = obtener_maximos(listas)
print(maximos)
"""


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, numeros))
print(primos)