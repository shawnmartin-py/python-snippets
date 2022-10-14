class Player:
    count = 0
    def __init__(self):
        self.count += 1  # self.count = self.count + 1
p1 = Player()
print(Player.count)