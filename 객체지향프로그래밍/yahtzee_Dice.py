import random


class Die:
    def __init__(self):
        self.__face = random.randint(1, 6)

    @property
    def face(self):
        return self.__face

    def roll(self):
        self.__face = random.randint(1, 6)

    def __str__(self):
        return f'{self.__face}'


class YahtzeeDice:
    def __init__(self):
        self.__dice = [Die() for _ in range(5)]

    @property
    def dice(self):
        return self.__dice

    @property
    def faces(self):
        return [die.face for die in self.__dice]

    def roll_dice(self, target_dice: [int]):
        for n in target_dice:
            self.__dice[n-1].roll()

    def show_faces(self):
        for n, f in enumerate(self.faces):   #enumerate : for문에서 index와 원소를 같이 쓰기 위한 내장함수
            print(f'주사위 {n+1}의 눈: {f}')

    def count_faces(self, face):
        return self.faces.count(face)

    def sum_faces(self):
        return sum(self.faces)


    def __str__(self):
        result = ''
        for n in range(5):
            result += f'주사위 {n+1}\t'
        result += '\n'

        for f in self.faces:
            result += f'{f:5d}\t'
        result += '\n'

        return result