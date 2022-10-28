from lib.models import Shop, Discount


if __name__ == '__main__':

    # a
    shop1 = Shop('Store', 'food')
    shop1.describe_shop()
    shop1.open_shop()

    # b
    s1 = Shop('Auchan', 'food', 1235)
    s2 = Shop('SportMaster', 'sport', 340)
    s3 = Shop('Zara', 'clothes', 678)

    shops = [s1, s2, s3]
    for i in shops:
        i.describe_shop()

    # c
    shop2 = Shop('Store-2', 'books', 120)
    print(f'Numbers of units: {shop2.numbers_of_units}')
    shop2.numbers_of_units -= 15
    print(f'Numbers of units: {shop2.numbers_of_units}')

    # d
    shop2.set_numbers_of_units(135)
    print(f'Numbers of units: {shop2.numbers_of_units}')

    # e
    store_discount = Discount('Flowers shop', 'flowers', ['Roses', 'Violets', 'Chrysanthemum', 'Chamomile'], 80)
    store_discount.get_discount_products()
