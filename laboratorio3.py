#!/usr/bin/python3
# Autores:María Gutiérrez, Susan Moraga, Brandon Cascante Rodríguez. B71732.
# Curso:IE-0117 Programación Bajo Plataformas Abiertas.
# III ciclo 2021.
# Laboratorio 2 python.
# Clase Matriz.
'''Se crea una clase para representar matrices n x m. Donde n y m se le deben pasar al
constructor, y son valores enteros positivos. El objeto es inicializado con todos los 
elementos en 0. Se debe de acceder y modificar los valores de la matriz, además, se 
añadem métodos para la realizaciòn de sumas, restas y multiplicaciones de matrices'''

# Clase matriz, para reprensetar matrices n x m.
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
    # Método para representar como string la matriz.
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
    
    # Método para sumar matrices.
    def __add__(self, other):
        '''Se define la lista en la que se guardará las filas de la mtriz
         resultante al sumar las matrices.'''
        suma = []

        # Se obtiene la cantidad de columnas de la segunda matriz
        for x in other.lista:
            columnas_2 = len(x)
        ''' Se comprueba que la cantidad de filas y la  cantidad de columnas de
        las matrices sean iguales mediante el if, en caso de que las filas, las
        columnas o ambas sean diferentes se imprimirá un mensaje de error'''
        if self.n == len(other.lista) and self.m == columnas_2:
            for i in range(self.n):
                '''Se define una lista en la que se guardará los valores de
                cada fila de la matriz resultante.'''
                fila_resultante = []
                for j in range(len(self.lista[i])):
                    fila_resultante.append(self.lista[i][j]+other.lista[i][j])
                suma.append(fila_resultante)

        elif self.n != len(other.lista) and self.m != columnas_2:
            suma = 'Error, la cantidad de filas y columnas son diferentes'

        elif self.n != len(other.lista):
            suma = 'Error, la cantidad de filas son diferentes'

        elif self.m != columnas_2:
            suma = 'Error, la cantidad de columnas son diferentes'
        return suma
    
    # Método para restar matrices.
    def __sub__(self, other):
        '''Se define la lista en la que se guardará las filas de la matriz
        resultante al restar las matrices.'''
        resta = []
        # Se obtiene la cantidad de columnas de la segunda matriz
        for x in other.lista:
            columnas_2 = len(x)
        ''' Se comprueba que la cantidad de filas y la  cantidad de columnas de
        las matrices sean iguales mediante el if, en caso de que las filas, las
        columnas o ambas sean diferentes se imprimirá un mensaje de error'''
        if self.n == len(other.lista) and self.m == columnas_2:
            for i in range(self.n):
                '''Se define una lista en la que se guardará los valores de
                cada fila de la matriz resultante.'''
                fila_resultante = []
                for j in range(len(self.lista[i])):
                    fila_resultante.append(self.lista[i][j]-other.lista[i][j])
                resta.append(fila_resultante)

        elif self.n != len(other.lista) and self.m != columnas_2:
            resta = 'Error la cantidad de filas y columnas son diferentes'

        elif self.n != len(other.lista):
            resta = 'Error la cantidad de filas son diferentes'

        elif self.m != columnas_2:
            resta = 'Error la cantidad de columnas son diferentes'
        return resta


if __name__ == '__main__':
    matriz = Matriz(3, 3)
    print(matriz)
