from enum import Enum


class PizzaSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class Pizza:
    def __init__(self, price, description, size):
        self.price, self.description = price, description
        self.size = self.parseSize(size)

    def parseSize(self, size: str) -> PizzaSize:
        size = size.lower()

        if size == 'small':
            return PizzaSize.SMALL
        elif size == 'medium':
            return PizzaSize.MEDIUM
        elif size == 'large':
            return PizzaSize.LARGE
        else:
            return PizzaSize.SMALL


class Order:
    def __init__(self):
        self.items = []
        self.total = 0
        self.discount = 0

    def addItem(self, item: Pizza):
        self.items.append(item)
        self.total += item.price


class Cart:
    def __init__(self):
        pass

    def addOrder(self, order):
        self.order = order

    def checkout(self, rules):
        for r in rules:
            self.order.addDiscount(self.parseRule(r))
        return self.order.total - self.order.discount

    def parseRule(self, rule):
        # TODO: Implement
        return 0

    # TODO: Implement functionality to add/modify rules.


class User:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.rules = []
        self.cart = Cart()

    def placeOrder(self, items):
        order = Order()
        for item in items:
            order.addItem(item)
        self.cart.addOrder(order)
        price = self.cart.checkout(rules=self.rules)
        print('Total: ' + str(price))