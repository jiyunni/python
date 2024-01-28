'''
임의의 문자열을 키보드를 통해 입력받아 해당 문자열에 포함된 영어 모음의 개수를 구해 출력하는 프로그램을 작성하시오.
'''
vo = 'aeiouAEIOU'

string = str(input('문자열 입력:'))
vo_count = 0

for n in string:
    if n in vo:
        vo_count += 1

print(f'입력 문자열: {string}, 모음의 수: {vo_count}')