class Tamagotchi(object):
    def __init__(self):
        self.hungriness = 5
        self.fullness = 5
        self.happiness = 5
        self.tiredness = 5

    def eat(self):
        self.hungriness -= 1
        self.fullness += 1

    def play(self):
        self.happiness += 1
        self.tiredness += 1

    def toBed(self):
        self.tiredness -= 1

    def poop(self):
        self.fullness -= 1

    def timePasses(self):
        self.hungriness += 1
        self.tiredness += 1
        self.happiness -= 1