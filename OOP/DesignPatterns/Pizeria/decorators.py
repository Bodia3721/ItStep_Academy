from Pizeria.components import Pizza


class PizzaDecorator(Pizza):

    def __init__(self, name: str, pizza: Pizza):
        super().__init__(name)
        self._pizza = pizza

    def get_cost(self):
        return 0.0


class TomatoPizza(PizzaDecorator):

    def __init__(self, pizza: Pizza):
        super().__init__(f'{pizza.name}, із томатами', pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 3


class CheesePizza(PizzaDecorator):

    def __init__(self, pizza: Pizza):
        super().__init__(f'{pizza.name}, із сиром', pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 5


class MeatPizza(PizzaDecorator):

    def __init__(self, pizza: Pizza):
        super().__init__(f"{pizza.name}, із м'ясом", pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 7


class ChiliPizza(PizzaDecorator):

    def __init__(self, pizza: Pizza):
        super().__init__(f"{pizza.name}, із перцем чілі", pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 3