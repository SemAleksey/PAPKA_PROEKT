# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
        self.BC = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
        self.AC = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)
    """ Считаем периметр треугольника """
    def perimetr(self):
        per = self.AB + self.BC + self.AC
        return per
    """ Считаем площадь треугольника """
    def Striangle(self):
        semiper = self.perimetr() / 2
        return math.sqrt((semiper * (semiper - self.AB)*(semiper - self.BC)*(semiper - self.AC)))
    """ Считаем высоту треугольника """    
    def height_triangle(self):
        return (self.Striangle() * 2) / self.AB
        
tr = Triangle((1, 1), (8, 3), (5, 7))
print(tr.perimetr())
print(tr.Striangle())
print(tr.height_triangle())

