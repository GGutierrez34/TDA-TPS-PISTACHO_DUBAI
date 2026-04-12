# TDA Turno:

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


# Funciones auxiliares:     

# Inicializamos un array con datos de tipo Turno.
def inicializar_turnos(turnos):
    turnos_iniciados = []
    indice = 0
    for turno_i in turnos:
        horario_limite = turno_i[0]
        beneficio = turno_i[1]
        turno = Turno(indice,beneficio,horario_limite)
        turnos_iniciados.append(turno)
        indice += 1    
        
    return turnos_iniciados
    
# Iteramos sobre los turnos ordenados por su beneficio de mayor a menor.
# Intentamos guardar el turno en el lugar más cercano a su tiempo limite (elección greedy) 
# para llegar a la solución optima global.
# Si el horario limite es mas grande que la cantidad de turnos, lo limitamos a la cantidad de turnos.  
# Mientras esté ocupado el lugar donde intentamos guardar el turno le restamos 1 al horario ideal.
# Si el horario ideal está disponible lo guardamos.
def elegir_turnos(turnos_ordenados, horarios_ocupados):
    turnos_elegidos = []
    beneficio_total = 0
    
    for turno in turnos_ordenados:
        horario_limite = turno.ver_horario_limite()  
        
        if horario_limite > len(horarios_ocupados):
            horario_limite = len(horarios_ocupados)
        
        horario_ideal = horario_limite-1
        
        while horario_ideal >= 0 and horarios_ocupados[horario_ideal] != None:
            horario_ideal -= 1

        if horario_ideal < 0:
            continue

        horarios_ocupados[horario_ideal] = turno
        
        beneficio_total += turno.ver_beneficio()
        turnos_elegidos.append(turno.ver_indice_entrada())
        
    return turnos_elegidos,beneficio_total
    
    
# Main:

def main(turnos: list[tuple[int, int]]) -> tuple[list[int], int]:    
    turnos_iniciados = inicializar_turnos(turnos)

    # Ordenamos los turnos por el mayor beneficio que nos dan de mayor a menor.
    turnos_ordenados = sorted(turnos_iniciados, key= lambda turno: turno.ver_beneficio(), reverse=True)
    
    # Creamos una lista para ir guardando los turnos en su lugar y poder chequear si 
    # ya hay otro turno ocupando ese horario.
    horarios_ocupados = [None] * len(turnos)
    
    turnos_elegidos, beneficio_total = elegir_turnos(turnos_ordenados,horarios_ocupados)
    
    turnos_elegidos = sorted(turnos_elegidos, key=lambda indice: turnos[indice][0])

    return turnos_elegidos,beneficio_total
