def main(turnos: list[tuple[int, int]]) -> tuple[list[int], int]:
    beneficio_total = 0
    turnos_guardados = []
    indices_entrada = {}

    # Inicializamos el diccionario de indices de entrada.
    indice = 0
    for turno in turnos:
        indices_entrada[indice] = turno
        indice+=1

    # Ordenamos los turnos por el mayor beneficio que nos dan de mayor a menor.
    # Obtenemos una lista ordenada con las claves ordenadas de los respectivos turnos.
    turnos_ordenados = sorted(indices_entrada, key= lambda x: indices_entrada[x][1], reverse=True)
    
    # Creamos un diccionario para ir guardando los turnos en su lugar y chequear si 
    # ya hay otro turno cargado en ese horario.
    horarios_ocupados = {}
    for i in range(len(turnos_ordenados)):
        horarios_ocupados[i] = None
    
    # Iteramos sobre los indices de los turnos ordenados.
    # Guardamos el turno en el lugar más cercano a su tiempo limite (elección greedy) 
    # para llegar a la solución optima global.
    # Si intentamos guardar el turno y ya hay otro en ese mismo horario 
    # intentamos buscar si hay lugar en horarios anteriores utilizando el diccionario
    # "horarios_ocupados".
    for indice in turnos_ordenados:
        horario_limite = indices_entrada[indice][0]
        max_horario_posible = horario_limite-1

        while max_horario_posible >= 0 and horarios_ocupados[max_horario_posible] != None:
            max_horario_posible -= 1

        if max_horario_posible < 0:
            continue

        horarios_ocupados[max_horario_posible] = "horario ocupado"
        
        beneficio_total += indices_entrada[indice][1]
        turnos_guardados.append(indice)

    return turnos_guardados,beneficio_total

if __name__ == "__main__":
    print(main([(1,20),(1,10),(5,30),(5,30),(5,30),(5,30)]))
    print(main([(1, 10), (2, 10)]))
    
