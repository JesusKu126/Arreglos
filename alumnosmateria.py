def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

def main():
    num_alumnos = 100
    num_materias = 6
    matriz = crear_matriz(num_alumnos, num_materias)
    for i in range(num_alumnos):
        for j in range(num_materias):
            matriz[i][j] = i * 10 + j  
    alumno_buscado = 95
    materia_buscada = 5
    nota = matriz[alumno_buscado - 1][materia_buscada - 1]
    print(f"La nota del alumno {alumno_buscado} en la materia {materia_buscada} es: {nota}")

if __name__ == "__main__":
    main()
