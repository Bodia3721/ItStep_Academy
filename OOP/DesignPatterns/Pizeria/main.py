from components import *
from decorators import *


if __name__ == '__main__':

    pizza1 = ItalianPizza()
    pizza1 = TomatoPizza(pizza1)
    print(f'{pizza1.name} - {pizza1.get_cost()}')

    pizza2 = ItalianPizza()
    pizza2 = CheesePizza(pizza2)
    pizza2 = CheesePizza(pizza2)
    print(f'{pizza2.name} - {pizza2.get_cost()}')

    pizza3 = MexicanPizza()
    pizza3 = TomatoPizza(pizza3)
    pizza3 = CheesePizza(pizza3)
    print(f'{pizza3.name} - {pizza3.get_cost()}')

    pizza4 = MexicanPizza()
    pizza4 = MeatPizza(pizza4)
    pizza4 = ChiliPizza(pizza4)
    print(f'{pizza4.name} - {pizza4.get_cost()}')

    pizza5 = NewYorkPizza()
    pizza5 = MeatPizza(pizza5)
    pizza5 = MeatPizza(pizza5)
    pizza5 = CheesePizza(pizza5)
    print(f'{pizza5.name} - {pizza5.get_cost()}')

