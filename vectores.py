

"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Juan Camilo De Los Ríos
    


    
"""


# from vectors import *


class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other



# Part a realitzar 

    
    # Sobrecarreguem l'operador (*) per implementar la multiplicació d'un vector per una constant o altre vector
        
        def __mul__(self, other):
            if isinstance(other, (int,float,complex)):
                return Vector([item * other for item in self])
            else:
                return Vector([item * otro for item, otro in zip(self,other)])


        __rmul__ = __mul__


    # Sobrecarreguem l'operador @ per implementar el productw escalar de dos vectors
    
        def __matmul__(self, other):
            ini = 0
            mul = Vector([item * otro for item, otro in zip(self, other)])
            for i in range(len(mul)):
                ini += mul[i]
            return ini


        __rmatmul__ = __matmul__


    # Sobrecarreguem l'operador // per que proporcioni la component tangencial

        def __floordiv__(self, other):
            suma = 0
            for x in range(len(other)):
                suma += other[x]**2
            v_tang = ((self @ other)/suma)*other
            return v_tang

    
        __rfloordiv__ = __floordiv__

    
    # Sobrecarreguem l'operador % per que proporcioni la component normal

        def __mod__(self,other):          
            v_tang = self // other
            v_perp = self - v_tang
            return v_perp


        __rmod__= __mod__


import doctest
doctest.testmod()




# Tests Unitari

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

v1 * v2

# Vector([4, 10, 18])

v1 * 2

# Vector([2, 4, 6])

v1 @ v2

# 32

v1 = Vector([2, 1, 2])
v2 = Vector([0.5, 1, 0.5])
v1 // v2

# Vector([1.0, 2.0, 1.0])

v1 % v2

# Vector([1.0, -1.0, 1.0])
    

