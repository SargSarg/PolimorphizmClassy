#(3) Импортируем class Rectangle из первой папки
from rectangle import Rectangle,Square

#(4)Дале создадим 2 прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#(5)Вывод плошадей этих прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())
#(8)Теперь добавим значения для посика площади квадратов
square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())

#
figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure,Square): #если квадрат то печать через метод гет ареа сквар
        print(figure.get_area_square())
    else: #иначе get area этот метод мы назначили для прямоугольников
        print(figure.get_area())