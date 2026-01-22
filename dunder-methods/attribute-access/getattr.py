class Robot:
    def __init__(self):
        self.name = "R2D2"
    def __getattr__(self, name):
        return f"I doon't have '{name}', but here's a default message"


r = Robot()
print(r.name)
print(r.weapon)