class Turno:
    def __init__(self,indice,beneficio,h_limite):
        self.indice_entrada = indice
        self.beneficio = beneficio
        self.horario_limite = h_limite
        
    def ver_beneficio(self):
        return self.beneficio
    
    def ver_indice_entrada(self):
        return self.indice_entrada

    def ver_horario_limite(self):
        return self.horario_limite

def main(turnos: list[tuple[int, int]]) -> tuple[list[int], int]:
    turnos_elegidos = []
    beneficio_total = 0
    
    horario_maximo = 0
    turnos_guardados = []

    # Inicializamos un array con datos de tipo Turnos.
    indice = 0
    for turno_i in turnos:
        beneficio = turno_i[0]
        horario_limite = turno_i[1]
        if horario_limite > horario_maximo:
            horario_maximo = horario_limite
        turno = Turno(indice,beneficio,horario_limite)
        turnos_guardados.append(turno)
        indice += 1

    # Ordenamos los turnos por el mayor beneficio que nos dan de mayor a menor.
    # Obtenemos una lista ordenada con los turnos ordenados según su beneficio de mayor a menor.
    turnos_ordenados = sorted(turnos_guardados, key= lambda turno: turno.ver_beneficio(), reverse=True)
    
    # Creamos una lista para ir guardando los turnos en su lugar y poder chequear si 
    # ya hay otro turno cargado en ese horario.
    horarios_ocupados = [None] * len(turnos)
    
    # Iteramos sobre los turnos ordenados por su beneficio de mayor a menor.
    # Intentamos guardar el turno en el lugar más cercano a su tiempo limite (elección greedy) 
    # para llegar a la solución optima global.
    # Si intentamos guardar el turno y ya hay otro en ese mismo horario 
    # buscamos si hay lugar en horarios anteriores utilizando
    # la lista "horarios_ocupados".
    for turno in turnos_ordenados:
        horario_limite = turno.horario_limite()
        horario_ideal = horario_limite-1

        while horario_ideal >= 0 and horarios_ocupados[horario_ideal] != None:
            horario_ideal -= 1

        if horario_ideal < 0:
            continue

        horarios_ocupados[horario_ideal] = "horario ocupado"
        
        beneficio_total += turno.ver_beneficio()
        turnos_elegidos.append(turno.ver_indice_entrada())

    return turnos_elegidos,beneficio_total

if __name__ == "__main__":
    print(main([(1,20),(1,10),(5,30),(5,30),(5,30),(5,30)]))
    print(main([(1, 10), (2, 10)]))