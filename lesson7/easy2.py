# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapezoid:
   
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        '''Ищем длинну сторон трапеции'''
        self.AB = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
        self.BC = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
        self.CD = math.sqrt((D[0] - C[0])**2 + (D[1] - C[1])**2)
        self.AD = math.sqrt((D[0] - A[0])**2 + (D[1] - A[1])**2)
        '''Ищем длинну диагоналей трапеции'''
        self.AC = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)
        self.BD = math.sqrt((D[0] - B[0])**2 + (D[1] - B[1])**2)
        
    '''Проверяем является ли фигура равнобочной трапецией'''
    def figure(self):
        if self.AB == self.CD and self.AC == self.BD:
            return 'Эта фигура является равнобочной трапецией'
        else:
            return 'Это фигура не является равнобочной трапецией'
    ''' Ищем периметр трапеции '''
    def perimetr(self):
        return self.AB + self.BC + self.CD + self.AD
    ''' Ищем площадь трапеции '''    
    def S_trapezoid(self):        
        return ((self.AD + self.BC)/4) * math.sqrt((4 * (self.AB**2)) - ((self.AD - self.BC)**2))
    def sides(self):
        return self.AB, self.BC, self.CD, self.AD
        
tr = Trapezoid((1, 1), (5, 3), (5, 7), (1, 9))
print(tr.figure())
print(tr.perimetr())
print(tr.S_trapezoid())
print(tr.sides())