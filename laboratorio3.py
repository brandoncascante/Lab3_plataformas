#!/usr/bin/python3
# Autores:María Gutiérrez, Susan Moraga, Brandon Cascante Rodríguez. B71732.
# Curso:IE-0117 Programación Bajo Plataformas Abiertas.
# III ciclo 2021.
# Laboratorio 2 python.
# Programa para identificar si hay sub-strings que sean palíndromo.
class Matriz:
    def __init__(self, n, m):
        # Se define la cantidad de filas n.
        self.n = n
        # Se define la cantidad de columnas m
        self.m = m
        '''Se obtiene una lista de listas. Es decir, una lista con las filas
        de la matiz'''
        self.lista = []
        for i in range(self.n):
            self.lista.append([])
            for j in range(self.m):
                self.lista[i].append(0)

    def __str__(self):
        '''Se crea una lista de cadenas llamada matriz, en la cual las cadenas
        corresponden a las filas de la matriz. Y mediante el método .join se
        realiza la separación de dichas cadenas con salto de línea, con la
        finalidad de imprimir la matriz'''
        matriz = []
        impresion = None
        for y in self.lista:
            self.filas = []
            for x in y:
                self.filas.append(str('{}'.format(x)))
            matriz.append(' '.join(self.filas))
            impresion = '\n'.join(matriz)
        return '{}'.format(impresion)


if __name__ == '__main__':
    matriz = Matriz(3, 3)
    print(matriz)
