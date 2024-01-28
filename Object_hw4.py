# 문제1 : Die, YahtzeeDice 클래스 정의
import random


class Die:
    def __init__(self, face: int):
        self.__face = face

    def roll(self) -> None:
        self.__face = random.randrange(1, 7)

    @property
    def face(self):
        return self.__face


class YahtzeeDice:
    def __init__(self):
        self.__dice = [0, 0, 0, 0, 0]

    def roll_dices(self, dices: list) -> None:
        for i in range(len(dices)):
            die = Die(0)
            die.roll()
            if dices[i] == 1:
                self.__dice[0] = die.face
            elif dices[i] == 2:
                self.__dice[1] = die.face
            elif dices[i] == 3:
                self.__dice[2] = die.face
            elif dices[i] == 4:
                self.__dice[3] = die.face
            elif dices[i] == 5:
                self.__dice[4] = die.face

    def show_faces(self):
        print(self.__dice)

    def get_faces(self):
        return self.__dice


    def count_faces(self, num):
        same_num_cnt = 0
        for i in range(5):
            if self.__dice[i] == num:
                same_num_cnt += 1

        return str(same_num_cnt)


    def sum_faces(self):
        total = 0
        for n in range(5):
            total += self.__dice[n]
        return str(total)


if __name__ =='__main__':
    game = YahtzeeDice()
    game.roll_dices([1, 2, 3, 4, 5])


    # 5개의 주사위를 던져 나온 눈의 결과
    game.show_faces()


    # 1~6 눈이 나온 수
    for n in range(1,7):
        print(f'{n}이 나온 주사위 갯수: {game.count_faces(n)}')


    # 눈의 합
    print(f'모든 주사위 눈의 합 : {game.sum_faces()}')