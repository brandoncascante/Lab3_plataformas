#!/usr/bin/python3
'''Autores:
María Gutiérrez Pol- B83679
Susan Moraga López - B75140
Brandon Cascante Rodríguez - B71732.'''
# Curso:IE-0117 Programación Bajo Plataformas Abiertas.
# III ciclo 2021.
# Laboratorio 3 python.
'''Creación de la clase para representar una matrices nxm, las cuales se
representarán como un string, además, se accede y se definen los valores
mediante paréntesis cuadrados. Asimismo, se realizan operaciones de matrices'''

# Clase para el levantamiento de excepciones.


class Vector():
    def __init__(self, m):
        # Cantidad de columnas
        self.m = m
        # Se comprueba que la cantidad de columnas sea mayor a 0.
        if self.m <= 0:
            raise Exception('Error')
        # Se crea un vector en el que se guarda los valores de la matrices.
        self.vector = [0 for x in range(self.m)]

    ''' Métodos getitem y setitem para levantar excepciones de los paréntesis
    cuadrado correspondientes a las columnas'''
    def __getitem__(self, indice):
        # Levantamiento de excepción índice negativo
        if indice < 0:
            raise Exception('error, índice negativo')
        # Levantamiento de excepción fuera del rango.
        elif indice >= self.m:
            raise Exception('error, índice fuera del rango')
        return self.vector[indice]

    # Se utiliza el método setitem para reemplazar los valores de la matriz

    def __setitem__(self, indice, valor):
        if indice < 0:
            raise Exception('error, índice negativo')
        elif indice >= self.m:
            raise Exception('error, fuera del índice')
        self.vector[indice] = valor


class Matriz():
    def __init__(self, n, m):
        # Se define la cantidad de filas n.
        self.n = n
        # Se define la cantidad de columnas m
        self.m = m
        '''Se obtiene una lista de listas. Es decir, una lista con las filas
        de la matiz'''
        self.lista = []
        for i in range(self.n):
            self.lista.append(Vector(m))

    def __str__(self):
        '''Se crea una lista de cadenas llamada matriz, en la cual las cadenas
        corresponden a las filas de la matriz. Y mediante el método .join se
        realiza la separación de dichas cadenas con salto de línea, con la
        finalidad de imprimir la matriz'''
        matriz = []
        impresion = None
        for y in self.lista:
            filas = []
            for columnas in range(self.m):
                x = y[columnas]
                filas.append(str('{}'.format(x)))
            matriz.append(' '.join(filas))
            impresion = '\n'.join(matriz)
        return '{}'.format(impresion)

    def __getitem__(self, indice):
        # Levantamiento de excepción índice negativo
        if indice < 0:
            raise Exception('error, índice negativo')
        # Levantamiento de excepción fuera del rango.
        elif indice >= self.m:
            raise Exception('error, índice fuera del rango')
        return self.lista[indice]

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
                for j in range(self.m):
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
        if self.n == other.n and self.m == other.m:
            '''Se realiza el algrotimo de resta de matrices mediante los
             siguientes for, en el cual se resta entrada por entrada'''
            for i in range(self.n):
                for j in range(self.m):
                    resta[i][j] = self.lista[i][j]-other.lista[i][j]

        elif self.n != other.n and self.m != other.m:
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
            '''Se crea el algoritmo para la realización de la multiplicación.Se
            realiza el for para un rango de la cantidad de filas de la matriz
            resultante y un for para un rango de la cantidad de columnas de la
            matriz resultante'''
            for x in range(self.n):
                for y in range(other.m):
                    for z in range(other.n):
                        producto[x][y] += self.lista[x][z] * other.lista[z][y]
        else:
            producto = 'No se puede realizar la multiplicación de matrices'

        return producto
    pass



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

