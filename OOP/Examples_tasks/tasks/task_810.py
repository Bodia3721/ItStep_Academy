class Rectangle(object):

    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height


    def __str__(self):
        return f'Прямокутник з шириною {self.__width} та висотою {self.__height}'


    def rectangle_square(self) -> float:
        return self.__width * self.__height


if __name__ == '__main__':

    width = 2
    height = 3
    rectangle = Rectangle(width, height)
    square = round(rectangle.rectangle_square(), 2)
    print(f'Площа прямокутника: {square}')