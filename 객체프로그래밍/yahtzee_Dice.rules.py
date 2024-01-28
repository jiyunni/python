from abc import ABC, abstractmethod
from 객체프로그래밍.yahtzee_Dice import *


class Rule(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def points(self, dice: YahtzeeDice) -> int:
        ...


class SameValue(Rule):
    def __init__(self, value: int, name: str):
        super().__init__(name)
        self.__value = value  # 1,2,3,4,5,6

    def points(self, dice: YahtzeeDice) -> int:
        return dice.count_faces(self.__value) * self.__value


class ThreeOfAKind(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) >= 3:
                return dice.sum_faces()
        return 0


class FourOfAKind(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) >= 4:
                return dice.sum_faces()
        return 0


class FullHouse(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) == 3:
                for face2 in range(1, 7):
                    if (face != face2) and (dice.count_faces(face2) == 2):
                        return 25
        return 0


class Yahtzee(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        for face in range(1, 7):
            if dice.count_faces(face) >= 5:
                return dice.sum_faces()
        return 0


class Chance(Rule):
    def points(self, dice: YahtzeeDice) -> int:
        return dice.sum_faces()


class Straight(Rule):
    def is_straight(self, target_dice: [int]) -> bool:

        sorted_dice = sorted(target_dice.faces)
        set_result = set(sorted_dice)   # 중복제거를 위해 set 사용
        sorted_dice = list(set_result)  # 다시 list로 변환



        return (sorted_dice == [1, 2, 3, 4, 5] or   # Large
                sorted_dice == [2, 3, 4, 5, 6] or   # Large
                sorted_dice == [1, 2, 3, 4] or      # 아래는 모두 Small인 경우
                sorted_dice == [1, 2, 3, 4, 6] or
                sorted_dice == [2, 3, 4, 5] or
                sorted_dice == [3, 4, 5, 6] or
                sorted_dice == [1, 3, 4, 5, 6])


class SmallStraight(Straight):
    def points(self, dice: YahtzeeDice) -> int:
        if Straight.is_straight(self, dice):
            return 30
        return 0


class LargeStraight(Straight):
    def points(self, dice: YahtzeeDice) -> int:
        if Straight.is_straight(self, dice):
            sorted_dice = sorted(dice.faces)
            if sorted_dice == [1, 2, 3, 4, 5] or sorted_dice == [2, 3, 4, 5, 6]:
                return 40
            return 0
        return 0


if __name__ == '__main__':
    rules = [SameValue(1, 'Aces'),
             SameValue(2, 'Twos'),
             SameValue(3, 'Threes'),
             SameValue(4, 'Fours'),
             SameValue(5, 'Fives'),
             SameValue(6, 'Sixes'),
             ThreeOfAKind('ThreeOfAKind'),
             FourOfAKind('FourOfAKind'),
             FullHouse('FullHouse'),
             Chance('Chance'),
             SmallStraight('SmallStraight'),
             LargeStraight('LargeStraight')]

    yahtzee_dice = YahtzeeDice()

    target_dice = list(range(1, 6))
    yahtzee_dice.roll_dice(target_dice)
    print(yahtzee_dice)

    for rule in rules:
        score = rule.points(yahtzee_dice)
        print(f'Score for {rule.name:13s} : {score:2d} points')