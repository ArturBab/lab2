from lab_python_oop.Abstr_Figure import Abstr_Figure
from lab_python_oop.Color_Figure import Color_Figure

class Triangle(Abstr_Figure):
    """
    Класс «Треугольник» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Triangle | Треугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side1_param, side2_param, footing_param):
        """
        Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
        """
        self.side1 = side1_param
        self.side2 = side2_param
        self.footing = footing_param
        self.fc = Color_Figure()
        self.fc.colorproperty = color_param

    def square(self):
        """
        Класс должен переопределять метод, вычисляющий площадь фигуры.
        """
        return (self.side1*self.footing) / 2

    def __repr__(self):
        return 'Дана фигура => {}\nЦвет фигуры => {}\nДлинна = {}\nЕще одна длинна = {}\nОснование треугольника = {}\nS = {}.'.format(
            Triangle.get_figure_type(),
            self.fc.colorproperty,
            self.side1,
            self.side2,
            self.footing,
            self.square()
        )



