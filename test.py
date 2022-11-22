class Human:
    def __init__(self, name):
        self.name = name
    def hola(self):
        print(f"Hola, {self.name}")
class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp=xp
    def __str__(self):
        return f"STR : {self.name}"
class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


alpha = Player("ASDF", 1000)
alpha.hola()
beta = Fan("FDSA", "DD")
beta.hola()
print(alpha.name, beta.name)
print(alpha)
print(dir(beta))