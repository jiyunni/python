import math

print('이차 방정식 ax^2 + bx + c = 0 에 대한 근 판별과 근을 구하는 프로그램입니다.')
a = int(input('계수a:'))
b = int(input('계수b:'))
c = int(input('계수c:'))

d = b**2-4*a*c


if d > 0:
    x1 = (-b+(math.sqrt(b**2-4*a*c)))/(2*a)
    x2 = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
    print(f'{a}x^2 + {b}x + {c} = 0은 2개의 실근이 존재')
    print(f'근 : x1 = {x1:.4f}, x2 = {x2:.4f}')

elif d == 0:
    x = -b/(2*a)
    print(f'{a}x^2 + {b}x + {c} = 0은 1개의 실근(중근)이 존재')
    print(f'근 : x = {x:.4f}')

else:
    print(f'{a}x^2 + {b}x + {c} = 0은 실근이 존재하지 않음')
