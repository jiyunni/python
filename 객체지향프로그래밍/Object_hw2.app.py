import Object_hw2


# 문제2 : 쇼핑카트에 추가
p1 = Object_hw2.Product('제주 삼다수 그린 2L', 1200, 5)
p2 = Object_hw2.Product('신라면(120g*5입)', 4100, 2)
p3 = Object_hw2.Product('CJ 햇반(210g*12입)', 13980, 1)
p4 = Object_hw2.Product('몽쉘크림(12입)', 4780, 1)

s = Object_hw2.ShoppingCart()
s.add(p1)   # 삼다수 추가
s.add(p2)   # 신라면 추가
s.add(p3)   # 햇반 추가
s.add(p4)   # 몽쉘 추가

# 문제3 : 몽쉘크림 취소하고 구운감자 추가
s.delete(p4, 1)     # 쇼핑카트에서 몽쉘을 1개 제거
p5 = Object_hw2.Product('해태 구운감자(135g*5입)', 3580, 2) # 구운감자 생성
s.add(p5)           # 구운감자추가

# 문제4 : 전품목 10% 할인
for i in s.shop_list:
    i.discount_rate = 0.1

# 문제5 : 영수증 출력
print(s.billing())
