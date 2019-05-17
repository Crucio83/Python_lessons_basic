# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Side:
    @staticmethod
    def LengthSide(X1, Y1, X2, Y2):
        return round(sqrt((X2 - X1)**2 + (Y2 - Y1)**2))


class Triangle(Side):
    def __init__(self, XA, YA, XB, YB, XC, YC):
        self.XA = XA
        self.YA = YA
        self.XB = XB
        self.YB = YB
        self.XC = XC
        self.YC = YC
        self.AB = self.LengthSide(self.XA, self.YA, self.XB, self.YB)
        self.BC = self.LengthSide(self.XB, self.YB, self.XC, self.YC)
        self.CA = self.LengthSide(self.XC, self.YC, self.XA, self.YA)


    def Perimeter(self):
        self.Perimeter = round(self.AB + self.BC + self.CA)
        return self.Perimeter

    def P(self):
        self.P = int(self.Perimeter/2)
        return self.P

    def Square(self):
        self.Square = round(sqrt(self.P*(self.P - self.AB)*(self.P - self.BC)*(self.P - self.CA)))
        return self.Square

    def Height(self):
        self.Height = round(2*self.Square/self.CA)
        return self.Height

MyTriangle = Triangle(-8, -3, 4, -12, 8, 10)
print("класс Треугольника")
print(f'Длины строн Треугольника: АВ = {MyTriangle.AB}, ВС = {MyTriangle.BC}, СА = {MyTriangle.CA}\n'
      f'Периметр Треугольника равен: {MyTriangle.Perimeter()}\n'
      f'Полупериметр Треугольника равен: {MyTriangle.P()}\n'
      f'Площадь Треугольника равна: {MyTriangle.Square()}\n'
      f'Высота Треугольника равна: {MyTriangle.Height()}\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Side):
    def __init__(self, XA, YA, XB, YB, XC, YC, XD, YD):
        self.XA = XA
        self.YA = YA
        self.XB = XB
        self.YB = YB
        self.XC = XC
        self.YC = YC
        self.XD = XD
        self.YD = YD
        self.AB = self.LengthSide(self.XA, self.YA, self.XB, self.YB)
        self.BC = self.LengthSide(self.XB, self.YB, self.XC, self.YC)
        self.CD = self.LengthSide(self.XC, self.YC, self.XD, self.YD)
        self.DA = self.LengthSide(self.XD, self.YD, self.XA, self.YA)
        self.AC = self.LengthSide(self.XA, self.YA, self.XC, self.YC)
        self.BD = self.LengthSide(self.XB, self.YB, self.XD, self.YD)

    def CheckTrapezium(self):
        return("Да! =)" if self.AC == self.BD else "увы, нет =(")

    def Perimeter(self):
        self.Perimeter = round(self.AB + self.BC + self.CD + self.DA)
        return self.Perimeter

    def Square(self):
        if self.CheckTrapezium():
            h = sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            self.Square = round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.Perimeter() / 2
            self.Square =round((self.BC + self.DA)/abs(self.DA - self.BC) *
                         sqrt((p-self.DA)*(p-self.BC) *
                                   (p-self.DA-self.AB) *
                                   (p-self.DA-self.CD)), 2)
        return self.Square


MyTrap = Trapezium(-4, 1, -2, 3, 3, 3, 5, 2)

print()
print("класс Трапеции")
print(f'Трапеция является равнобочной: {MyTrap.CheckTrapezium()}\n'
      f'Длины строн Трапеции: АВ = {MyTrap.AB}, ВС = {MyTrap.BC}, CD = {MyTrap.CD}, DA = {MyTrap.DA}\n'
      f'Длины диагоналей Трапеции: AC = {MyTrap.AC}, ВD = {MyTrap.BD}\n'
      f'Периметр Трапеции равен: {MyTrap.Perimeter()}\n'
      f'Прощадь Трапеции равна: {MyTrap.Square()}')


