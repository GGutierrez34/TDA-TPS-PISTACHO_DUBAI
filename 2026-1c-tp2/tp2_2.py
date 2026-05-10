from typing import List, Tuple, Set

class Producto:
    def __init__(self, tamaño: int, valor: int, indice: int):
        self.tamaño = tamaño
        self.valor = valor
        self.indice = indice
    
    def relacion(self) -> float:
        return self.valor / self.tamaño if self.tamaño > 0 else 0


class SolucionBranchBound:
    def __init__(self, productos: List[Producto], k: int, C: int, a: float):
        self.productos_ordenados = productos.copy()
        self.k = k
        self.C = C
        self.a = a
        self.n = len(productos)
        
        self.mejor_ganancia = float('-inf')
        self.mejor_asignacion = None
    
    def resolver(self) -> Tuple[float, List[Set[int]]]:
        self.productos_ordenados.sort(key=lambda p: p.relacion(), reverse=True)
        
        espacio_libre = [self.C] * self.k
        asignacion = [set() for _ in range(self.k)]
        contenedores_usados = set()
        
        self._branch_and_bound(
            nro=0,
            ganancia_actual=0.0,
            espacio_libre=espacio_libre,
            asignacion=asignacion,
            contenedores_usados=contenedores_usados
        )
        
        if self.mejor_ganancia == float('-inf'):
            self.mejor_ganancia = 0.0
            self.mejor_asignacion = [set() for _ in range(self.k)]
            
        return self.mejor_ganancia, self.mejor_asignacion
    
    def _branch_and_bound(self, nro: int, ganancia_actual: float, 
                          espacio_libre: List[int], asignacion: List[Set[int]],
                          contenedores_usados: Set[int]) -> None:
        
        cota = self._cota_superior(nro, ganancia_actual, espacio_libre, contenedores_usados)
        
        if cota <= self.mejor_ganancia:
            return
        
        if nro == self.n:
            if ganancia_actual > self.mejor_ganancia:
                self.mejor_ganancia = ganancia_actual
                self.mejor_asignacion = [conjunto.copy() for conjunto in asignacion]
            return
        
        producto_actual = self.productos_ordenados[nro]
        
        self._branch_and_bound(nro + 1, ganancia_actual, espacio_libre, 
                              asignacion, contenedores_usados)
        
        for c in range(self.k):
            if producto_actual.tamaño <= espacio_libre[c]:
                
                espacio_antes = espacio_libre[c]
                c_usado_antes = c in contenedores_usados
                
                nueva_ganancia = ganancia_actual + producto_actual.valor
                
                if c_usado_antes:
                    nueva_ganancia = nueva_ganancia + espacio_antes * self.a - (espacio_antes - producto_actual.tamaño) * self.a
                else:
                    nueva_ganancia = nueva_ganancia - (espacio_antes - producto_actual.tamaño) * self.a
                
                asignacion[c].add(producto_actual.indice)
                espacio_libre[c] -= producto_actual.tamaño
                contenedores_usados.add(c)
                
                self._branch_and_bound(nro + 1, nueva_ganancia, espacio_libre,
                                      asignacion, contenedores_usados)
                
                asignacion[c].remove(producto_actual.indice)
                espacio_libre[c] = espacio_antes
                if not c_usado_antes:
                    contenedores_usados.discard(c)
    
    def _cota_superior(self, nro: int, ganancia_actual: float, 
                       espacio_libre: List[int], contenedores_usados: Set[int]) -> float:
        
        penalizacion_actual = sum(espacio_libre[c] * self.a for c in contenedores_usados)
        espacio_disponible = sum(espacio_libre)
        cota = ganancia_actual + penalizacion_actual
        
        for i in range(nro, self.n):
            prod = self.productos_ordenados[i]
            if prod.tamaño <= espacio_disponible:
                cota += prod.valor
                espacio_disponible -= prod.tamaño
                
        return cota

def main(productos: List[Tuple[int, int]], k: int, C: int, a: float) -> Tuple[float, List[Set[int]]]:
    productos_obj = [
        Producto(tamaño, valor, idx)
        for idx, (tamaño, valor) in enumerate(productos)
    ]
    
    solver = SolucionBranchBound(productos_obj, k, C, a)
    ganancia, asignacion = solver.resolver()
    
    return ganancia, asignacion

if __name__ == '__main__':
    # Ejemplo del enunciado
    n1 = [(2, 10), (5, 10), (7, 20)]
    ganancia1, asignacion1 = main(n1, k=2, C=8, a=5)
    print("Ejemplo 1:")
    print(f"Entrada: n={n1}, k=2, C=8, a=5")
    print(f"Ganancia: {ganancia1}")
    print(f"Asignación: {asignacion1}")
