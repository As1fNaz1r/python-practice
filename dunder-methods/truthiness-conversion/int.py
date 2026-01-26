# __int__ - Convert to Integer
# __int__ is called when you use int(obj) on your object.

class GameScore:
    def __init__(self, points, multiplier=1):
        self.points = points
        self.multiplier = multiplier

    def __int__(self):
        return self.points*self.multiplier


score = GameScore(100,2)
print(int(score))