#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sudoku.py
------------
Los Sudokus son unos juegos de origen Japones. El juego tiene un tablero de 9 x 9 casillas.
En cada casilla se debe asignar un número 1, 2, 3, 4, 5, 6, 7, 8 o 9.
La idea principal de juego es establecer los valores de los números en las casillas no
asignadas anteriormente si se considera que:
    a) Las casillas horizontales deben tener números diferentes entre si
    b) Las casillas verticales deben tener números diferentes entre si
    c) Las casillas que pertenecen al mismo grupo deben tener números diferentes entre si.
sea (r1, c1) el renglon y la columna de una casilla y (r2, c2) el renglon y la columna de otra casilla,
se dice que las casillas pertenecen al mismo grupo si y solo si r1/3 == r2/3 y c1/3 == c2/3
donde / es la división entera (por ejemplo 4/3 = 1 o 8/3 = 2).
Esto aplica si se considera 0 como la primer posición.
Para más información sobre sudokus, pueden googlearlo, buscarlos en wikipedia o comprar un librito
de sudokus de 8 pesos (cuidado, se puede perder mucho tiempo resolviendo sudokus).
Para revisar la tarea es necesario seguir las siguientes instrucciones:
Un Sudoku se inicializa como una lista de 81 valores donde los valores se encuentran de la manera siguiente:
    0   1   2 |  3   4   5 |  6   7   8
    9  10  11 | 12  13  14 | 15  16  17
   18  19  20 | 21  22  23 | 24  25  26
   -----------+------------+------------
   27  28  29 | 30  31  32 | 33  34  35
   36  37  38 | 39  ...
hasta llegar a la posición 81.
Los valores que puede tener la lista son del 0 al 9. Si tiene un 0 entonces es que el valor es desconocido.
"""

__author__ = 'juliowaissman'


import csp


class Sudoku(csp.GrafoRestriccion):
    """
    Esta es la clase que tienen que desarrollar y comentar. Las variables están dadas
    desde 0 hasta 81 (un vector) tal como dice arriba. No modificar nada de lo escrito
    solamente agregar su código.
    """

    def __init__(self, pos_ini):
        """
        Inicializa el sudoku
        """
        csp.GrafoRestriccion.__init__(self)

        self.dominio = {i: [val] if val > 0 else range(1, 10) for (i, val) in enumerate(pos_ini)}

        
        #=================================================================
        # 25 puntos: INSERTAR SU CÓDIGO AQUI (para vecinos)
        #=================================================================
        """
        Los vecinos de una casilla son todas aquellas que estan en su misma fila,
        columna o grupo.
        Primero se usarán las variables (x,y) para representar las coordenadas
        que ocupa la casilla dada en el tablero. Con estas se facilita la
        localización de aquellas en la misma fila, columna y grupo.
        """
        vecinos = {i: [] for i in range(0,81)}

        
        for i in range(0,81):
            x = i%9
            y = int(i/9)

            a = 3* int(x/3)
            b = 3* int(y/3)
            
            for j in range(0,9):
                #Misma fila
                #Esta condicional evita que una casilla sea vecina de sí misma
                if j != x:                     
                    vecinos[i].append(j + 9*y) 
                
                #Misma columna
                #Esta condicional evita que una casilla sea vecina de sí misma
                if j != y:
                    vecinos[i].append(x + 9*j)

            #Mismo grupo
            #La condicional evita que se repitan valores ya incluídos
            for j in range (0,3):    
                for k in range(0,3):
                    if a+j != x and b+k != y:  
                        vecinos[i].append(a+j + 9*(b+k))



    def restriccion_binaria(self, (xi, vi), (xj, vj)):
        """
        El mero chuqui. Por favor comenta tu código correctamente
        """
        #===========================================================================
        # 25 puntos: INSERTAR SU CÓDIGO AQUI (restricciones entre variables vecinas)
        #===========================================================================
        """
        La función de restricción binaria recibe 2 vecinos. Si alguno de ellos
        es 0, significa que es una casilla vacía y es compatible con cualquier otra.
        Para regresar un False, los vecinos no deben ser casillas vacías y deben
        tener los mismos valores asignados.
        """

        if vi == 0 or vj == 0 or vi != vj:
            return True
        """  
        ui, wi = xi%9, int(xi/9)
        uj, wj = xj%9, int(xj/9)

        if ui == uj or wi == wj:
            return False

        if int(ui/9) == int(uj/9) and int(wi/9) == int(wj/9):
            return False
        
        
        return True
        """
        return False

        raise NotImplementedError("¡Es parte de la tarea implementar este método!")

    def imprime_sdk(self, asignacion):
        """
        Imprime un sudoku en pantalla en forma más o menos graciosa. Esta función solo sirve para la tarea y
        para la revisión de la tarea. No modificarla por ningun motivo.
        """
        s = [asignacion[i] for i in range(81)]
        c = ''
        for i in range(9):
            c += ' '.join(str(s[9 * i + j]) + ("  |  " if j % 3 == 2 and j < 7 else "   ") for j in range(9))
            c += '\n-------------+----------------+---------------\n' if i % 3 == 2 and i < 7 else '\n'
        print c


if __name__ == "__main__":
    #===========================================================================
    # Una forma de verificar si el código que escribiste es correcto
    # es verificando que la solución sea satisfactoria para estos dos
    # sudokus.
    #===========================================================================

    s1 = [0, 0, 3, 0, 2, 0, 6, 0, 0,
          9, 0, 0, 3, 0, 5, 0, 0, 1,
          0, 0, 1, 8, 0, 6, 4, 0, 0,
          0, 0, 8, 1, 0, 2, 9, 0, 0,
          7, 0, 0, 0, 0, 0, 0, 0, 8,
          0, 0, 6, 7, 0, 8, 2, 0, 0,
          0, 0, 2, 6, 0, 9, 5, 0, 0,
          8, 0, 0, 2, 0, 3, 0, 0, 9,
          0, 0, 5, 0, 1, 0, 3, 0, 0]

    print "Solucionando un Sudoku dificil"
    sudoku1 = Sudoku(s1)
    sudoku1.imprime_sdk(s1)
    sol1 = csp.asignacion_grafo_restriccion(sudoku1)
    sudoku1.imprime_sdk(sol1)


    s2 = [4, 0, 0, 0, 0, 0, 8, 0, 5,
          0, 3, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 7, 0, 0, 0, 0, 0,
          0, 2, 0, 0, 0, 0, 0, 6, 0,
          0, 0, 0, 0, 8, 0, 4, 0, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 0,
          0, 0, 0, 6, 0, 3, 0, 7, 0,
          5, 0, 0, 2, 0, 0, 0, 0, 0,
          1, 0, 4, 0, 0, 0, 0, 0, 0]


    print "Y otro tambien dificil"
    sudoku2 = Sudoku(s2)
    sudoku2.imprime_sdk(s2)
    sol2 = csp.solucion_CSP_bin(sudoku2)
    sudoku2.imprime_sdk(sol2)
