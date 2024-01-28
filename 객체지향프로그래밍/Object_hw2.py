# 문제1 : Class정의
class Product:
    discount_rate = 0.0

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return int(self.__price * self.__quantity * (1-self.discount_rate))

    def __str__(self):
        info = f'{self.__name}    {self.__quantity}개    {self.__price}'
        return info


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    @property
    def shop_list(self):
        return self.__shop_list

    def add(self, product):
        self.__shop_list.append(product)

    def delete(self, product, qty):
        for shop_list in self.__shop_list:
            if shop_list == product:
                shop_list.quantity -= qty   # qty 갯수만큼 제거

                if shop_list.quantity <= 0: # 수량이 0개면
                    self.__shop_list.remove(product)    # 카트에서 제거(remove)

    def total_price(self):
        sum = 0     # 총 가격
        for i in self.__shop_list:
            sum += i.get_price()
        return sum

    def billing(self):
        info = '구입 품목 :\n'
        for j in self.__shop_list:
            info += f'{j.name:20s} {j.quantity:3d}개 {j.get_price():15,d}\n'    # 한글,숫자,영문의 크기가 달라 format이 일정하지 않음.
        info += '----------------------------------------------\n'
        info += f'합계                            {self.total_price():15,d}'

        return info

    def __str__(self):
        info = f'{self.__shop_list}'
        return info