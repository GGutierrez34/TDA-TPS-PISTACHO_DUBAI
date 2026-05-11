from collections.abc import Sequence

class Grafo:
    def __init__(self):
        self.tamanio = 0
        self.lista_ady = {}
        self.capacidades = {}

    def agregar_vertice(self, v):
        self.lista_ady[v] = []
    def agregar_arista(self, v, w):
        self.lista_ady[v].append(w)
    def agregar_capacidad(self, v, w, cap):
        self.capacidades[(v, w)] = cap

    def bfs(self, s, t, padres):
        visitados = {v: False for v in self.lista_ady} 
        cola = []
        cola.append(s)
        visitados[s] = True

        while cola:
            u = cola.pop(0)
            for vecino in self.lista_ady[u]:
                capacidad_restante = self.capacidades[(u, vecino)]
                if not visitados[vecino] and capacidad_restante > 0:
                    cola.append(vecino)
                    visitados[vecino] = True
                    padres[vecino] = u
        return visitados[t]
    
    def edmonds_karp(self, fuente, sumidero):
        padres = {v: -1 for v in self.lista_ady}
        flujo_max = 0
        while self.bfs(fuente, sumidero, padres):
            flujo_camino = float("inf")
            
            aux = sumidero
            while aux != fuente:
                flujo_camino = min(flujo_camino, self.capacidades[padres[aux], aux])
                aux = padres[aux]
            
            aux = sumidero
            while aux != fuente:
                self.capacidades[padres[aux],aux] -= flujo_camino
                self.capacidades[aux, padres[aux]] += flujo_camino
                aux = padres[aux]
            
            flujo_max += flujo_camino
        return flujo_max

    def corte_minimo(self, fuente):
        alcanzables = set()
        self.corte_minimo_rec(fuente, alcanzables)

        no_alcanzables = []
        for v in self.lista_ady:
            if v not in alcanzables:
                no_alcanzables.append(v)
        
        return alcanzables, set(no_alcanzables)

    def corte_minimo_rec(self, u, visitados):
        visitados.add(u)
        for ady in self.lista_ady[u]:
            if ady not in visitados and self.capacidades[(u,ady)] > 0:
                self.corte_minimo_rec(ady, visitados)


def modelar_grafo(relaciones: list[tuple[int, int]], g):
    for v in relaciones:
        
        inicio = v[0]
        fin = v[1]
        capacidad = v[2]

        if inicio not in g.lista_ady:
            g.tamanio += 1
            g.agregar_vertice(inicio)
        
        if fin not in g.lista_ady:
            g.tamanio += 1
            g.agregar_vertice(fin)
        
        g.agregar_arista(inicio, fin)
        g.agregar_arista(fin, inicio)
        g.agregar_capacidad(inicio, fin, capacidad)
        
        if (fin,inicio) not in g.capacidades:
            g.agregar_capacidad(fin, inicio, 0)


def main(s1: int, s2: int, relaciones: list[tuple[int, int, int]]) -> tuple[set[int], set[int]]:
    g = Grafo()
    modelar_grafo(relaciones, g)
    g.edmonds_karp(s1, s2)
    list_s1, list_s2 = g.corte_minimo(s1)
    return list_s1,list_s2
    raise NotImplementedError
