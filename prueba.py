
def potenciacion(base, exponente):
    resultado = 0
    for i in range(exponente):
        resultado = resultado * base
    return resultado

    print(potenciacion(2, 3))