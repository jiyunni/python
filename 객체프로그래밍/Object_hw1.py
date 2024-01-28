#문제1. 클래스 정의

class Product:
    def __init__(self, name, price1, quantity):
        self.name = name
        self.price1 = price1
        self.quantity = quantity

    def price(self):
        return self.price1 * self.quantity

    def __str__(self):
        info = f'{self.name}    {self.quantity}개    {self.price1}'
        return info


class ShoppingCart:
    def __init__(self):
        self.shop_list = []

    def add(self, product):
        self.shop_list.append(product)

    def delete(self, product, qty):
        if qty == 0:
            self.shop_list.remove(product)

    def total_price(self):
        sum = 0     # 총 가격
        for i in self.shop_list:
            sum += i.price()
        return sum

    def billing(self):
        print('구입 품목 :')
        for j in self.shop_list:
            print(j.name.ljust(20) + str(j.quantity).rjust(5)+'개' + '{0: >10,}'.format(j.price()))
        print('------------------------------------------')
        print('합계                           {0: >10,}'.format(self.total_price()))

    def __str__(self):
        pass


if __name__ == '__main__':
    # 문제2 : 쇼핑카트에 추가
    p1 = Product('제주 삼다수 그린 2L', 1200, 5)
    p2 = Product('신라면(120g*5입)', 4100, 2)
    p3 = Product('CJ 햇반(210g*12입)', 13980, 1)
    p4 = Product('몽쉘크림(12입)', 4780, 1)

    s = ShoppingCart()
    s.add(p1)
    s.add(p2)
    s.add(p3)
    s.add(p4)

    # 문제3 : 몽쉘크림 취소하고 구운감자 추가
    s.delete(p4, 0)     # 몽쉘취소
    p5 = Product('해태 구운감자(135g*5입)', 3580, 2)
    s.add(p5)           # 감자추가

    # 문제4 : 영수증 출력
    s.billing()
