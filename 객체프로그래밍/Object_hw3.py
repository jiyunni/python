# 문제1 : Class정의
class Product:
    rate = 0.0

    def __init__(self, name: str, regular_price: int, quantity: int):
        self.__name = name
        self.__regular_price = regular_price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def regular_price(self):
        return self.__regular_price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def get_price(self):
        return int(self.__regular_price * self.__quantity)

    def __str__(self):
        info = f'{self.__name}    {self.__quantity}개    {self.__regular_price}'
        return info


class Sales_Product(Product):
    rate = 0.2

    def __init__(self, name: str, regular_price: int, quantity: int):
        super().__init__(name, regular_price, quantity)

    @property
    def get_price(self):
        return int(self.regular_price * self.quantity * (1 - self.rate))


class Clearance_Product(Product):
    rate = 0.5

    def __init__(self, name: str, regular_price: int, quantity: int):
        super().__init__(name, regular_price, quantity)

    @property
    def get_price(self):
        return int(self.regular_price * self.quantity * (1 - self.rate))


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    def add(self, product):
        self.__shop_list.append(product)

    def delete(self, product, qty):
        for shop_list in self.__shop_list:
            if shop_list == product:
                shop_list.quantity -= qty  # qty 갯수만큼 제거

                if shop_list.quantity <= 0:  # 수량이 0개면
                    self.__shop_list.remove(product)  # 카트에서 제거(remove)

    @property
    def total_price(self):
        sum = 0  # 총 가격
        for i in self.__shop_list:
            sum += i.get_price
        return sum

    def billing(self):
        info = '구입 품목 :\n'
        info += f'품목명                                 수량             정가           할인가\n'
        for j in self.__shop_list:
            info += f'{j.name:30s} {j.quantity:3d} {(j.quantity * j.regular_price):15,d} {j.get_price:15,d}\n'

        info += '--------------------------------------------------------------------------\n'
        info += f'합계                                                       {self.total_price:15,d}'

        return info

    def __str__(self):
        info = f'{self.__shop_list}'
        return info