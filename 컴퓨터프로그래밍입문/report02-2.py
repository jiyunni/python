'''
문제2
'''

string = input('문자열 입력:')

for n in range(len(string)):
    rotated_string = string[n:] + string[:n]
    print(rotated_string)