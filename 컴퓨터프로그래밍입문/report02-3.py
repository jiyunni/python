'''
임의의 양의 정수를 키보드를 통해 입력받아 그 수의 역순의 수를 구하는 프로그램을 작성하시오.
'''

num = int(input('양의 정수를 입력하세요:'))
origin_num = num
re_num = 0

while num > 0 :
    re = num % 10
    re_num = re_num * 10 + re
    num //= 10

print(f'입력 값: {origin_num}, 역순의 값: {re_num}')