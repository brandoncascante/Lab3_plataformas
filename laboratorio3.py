#!/usr/bin/python3
'''Autores:
María Gutiérrez.
Susan Moraga López - B75140
Brandon Cascante Rodríguez. B71732.'''
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
            impresion = '\n '.join(matriz)
        return '{}'.format(impresion)

    def __getitem__(self, idx):
        return self.lista.__getitem__(idx)

    def __add__(self, other):
        '''Se define la matriz vacía en la que se guardará el resultado
         obtenido al sumar las matrices.'''
        suma = Matriz(self.n, self.m)

        ''' Se comprueba que la cantidad de filas y la  cantidad de columnas de
        las matrices sean iguales mediante el if, en caso de que las filas, las
        columnas o ambas sean diferentes se imprimirá un mensaje de error'''
        if self.n == other.n and self.m == other.m:
            '''Se realiza el algrotimo de suma de matrices mediante los
             siguientes for, en el cual se suma entrada por entrada'''
            for i in range(self.n):
                for j in range(len(self.lista[i])):
                    suma[i][j] = self.lista[i][j]+other.lista[i][j]

        elif self.n != other.n and self.m != other.m:
            suma = 'Error la cantidad de filas y columnas son diferentes'

        elif self.n != other.n:
            suma = 'Error la cantidad de filas son diferentes'

        elif self.m != other.m:
            suma = 'Error la cantidad de columnas son diferentes'
        return suma

    def __sub__(self, other):
        '''Se define la matriz vacía en la que se guardará el resultado
         obtenido al restar las matrices.'''
        resta = Matriz(self.n, self.m)

        ''' Se comprueba que la cantidad de filas y la  cantidad de columnas de
        las matrices sean iguales mediante el if, en caso de que las filas, las
        columnas o ambas sean diferentes se imprimirá un mensaje de error'''
        if self.n == len(other.lista) and self.m == other.m:
            '''Se realiza el algrotimo de resta de matrices mediante los
             siguientes for, en el cual se resta entrada por entrada'''
            for i in range(self.n):
                for j in range(len(self.lista[i])):
                    resta[i][j] = self.lista[i][j]-other.lista[i][j]

        elif self.n != len(other.lista) and self.m != other.m:
            resta = 'Error la cantidad de filas y columnas son diferentes'

        elif self.n != other.n:
            resta = 'Error la cantidad de filas son diferentes'

        elif self.m != other.m:
            resta = 'Error la cantidad de columnas son diferentes'
        return resta

    def __mul__(self, other):
        '''Se define la matriz vacía en la que se guardará el resultado
         obtenido al restar las matrices.'''
        producto = Matriz(self.n, other.m)
        ''' Se comprueba que la cantidad de filas de la segunda matriz sea
        igual a la  cantidad de columnas de la primera matriz mediante el
         if, en caso de que las filas de que sean diferentes se imprimirá un
         mensaje de error'''
        if self.m == other.n:
            for x in range(self.n):
                for y in range(other.m):
                    for z in range(other.n):
                        producto[x][y] += self.lista[x][z] * other.lista[z][y]
        else:
            producto = 'No se puede realizar la multiplicación de matrices'

        return producto


if __name__ == '__main__':
    matriz = Matriz(2, 2)
    matriz[0][0] = 0
    matriz[0][1] = 1
    matriz[1][0] = 2
    matriz[1][1] = 3
    print('matriz:\n', matriz)
    matriz1 = Matriz(2, 2)
    matriz1[0][0] = 4
    matriz1[0][1] = 5
    matriz1[1][0] = 6
    matriz1[1][1] = 7
    print('matriz1:\n', matriz1)
    matriz2 = matriz+matriz1
    print('suma:\n', matriz2)
    matriz3 = matriz-matriz1
    print('resta:\n', matriz3)
    matriz4 = matriz*matriz1
    print('multiplicación:\n', matriz4)

