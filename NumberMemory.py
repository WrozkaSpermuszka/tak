import random
import Game

class NumberMemory(Game.Game):
    def __init__(self):
        super().__init__()
        self.__randomNumber = 0
    def Play(self):
        print("Score: " + str(self._score))
    def GenerateRandomNumber(self):
        self.__randomNumber = random.randint(0, 10)
        return self.__randomNumber

        