
from collections.abc import Sequence

# se define la estructura de las cajas
class Caja:
    def __init__(self, id_original, largo, ancho, altura):
        self.id_original = id_original
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

        self.area = largo * ancho


# funciones del programa
def generar_rotaciones(caja_tuplas):
    resultado = []
    for i in range(len(caja_tuplas)):
        x, y, z = caja_tuplas[i]
        resultado.append(Caja(
            id_original = i,
            largo = max(x, y),
            ancho = min(x, y),
            altura = z
        ))

        resultado.append(Caja(
            id_original = i,
            largo = max(x, z),
            ancho = min(x, z),
            altura = y
        ))

        resultado.append(Caja(
            id_original = i,
            largo = max(y, z),
            ancho = min(y, z),
            altura = x
        ))
    return resultado

def reconstruir_torre(opt, cajas, padres):
    resultado = []


    i = opt.index(max(opt))
    while i != -1:
        caja_actual = cajas[i]
        # formato_caja = (caja_actual.id_original, (caja_actual.ancho, caja_actual.largo))
        # resultado.append(formato_caja)

        resultado.append(caja_actual.id_original)
        resultado.append((caja_actual.ancho, caja_actual.largo))
        i = padres[i]

    return resultado


def obtener_altura_maxima(cajas):
    cajas.sort(key=lambda c: c.area)
    n = len(cajas)
    opt = []
    padres = [-1] *n
    for i in range(n):
        opt.append(cajas[i].altura)
        for j in range(i):
            if (cajas[i].largo > cajas[j].largo) and (cajas[i].ancho > cajas[j].ancho):
                # actualizamos el optimo de la base actual si es necesario (la ecuacion de recurrencia)
                if opt[i] < cajas[i].altura + opt[j]:
                    opt[i] = cajas[i].altura + opt[j]
                    padres[i] = j

    
    return (max(opt), reconstruir_torre(opt, cajas, padres))
    

def main(cajas: Sequence[tuple[float, float, float]]) -> tuple[float, list[tuple[int, tuple[float, float]]]]:
    rotaciones = generar_rotaciones(cajas)
    resultado_final = obtener_altura_maxima(rotaciones)
    
    return resultado_final