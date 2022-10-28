class Rectangle(object):

    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'Прямокутник із шириною: {self.__width} та довжиною: {self.__height}'

    def calc_square(self) -> float:
        return self.__width * self.__height


if __name__ == '__main__':

    w = 2
    h = 3

    rectangle = Rectangle(w, h)
    square = round(rectangle.calc_square(), 2)

    print(rectangle)
    print(square)
