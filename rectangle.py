#1()найти площадь прямоугольника
class Rectangle:
    def __int__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

#(2)Переходим в папку rectangle2

#(6)Добавим квадрат
class Square:
    def __int__(self,a):
        self.a = a
    def get_area_square(self):#ОБЯЗАТЕЛЬНО называем метод get подругому
        return self.a ** 2


