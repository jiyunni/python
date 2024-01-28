import Object_hw3


# 문제2 : 쇼핑카트에 추가
p1 = Object_hw3.Product('제주 삼다수 그린 2L', 1200, 5)
p2 = Object_hw3.Product('신라면(120g*5입)', 4100, 2)
p3 = Object_hw3.Sales_Product('CJ 햇반(210g*12입)', 13980, 1)
p4 = Object_hw3.Clearance_Product('노스페이스 올라운드 폴로 NT7PN00B', 65000, 1)


s = Object_hw3.ShoppingCart()
s.add(p1)   # 삼다수 추가
s.add(p2)   # 신라면 추가
s.add(p3)   # 햇반 추가
s.add(p4)   # 노스페이스 추가

# 문제3 : 영수증 출력
print(s.billing())