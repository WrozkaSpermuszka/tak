import Game
import time, random
class ReactionTime(Game.Game):
    def __init__(self):
        super().__init__()

print("when I say 'GO!' hit Enter")
time.sleep(3)
print("ready?")
time.sleep(1)
print("steady")
time.sleep(random.randint(2,5))
print("GO!")
tic = time.time()
a = input()
toc = time.time()

TimeSpent = toc-tic 
print("your reaction is:" + str(TimeSpent)+ 'seconds')