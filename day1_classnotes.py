class Monster:
    def __init__(self):
        self.hp = 10


class Weapon:
        def __init__(self):
            self.damage = 0
            self.durability = 0

        def attack(self):
            self.durability()
            return self.damage
# set durability is an internal

        def set_durability(self):
            self.durability -= 1
            if self.durability < 0:
                self.durability = 0
                self.damage = 0


'''class Sword(Weapon):
    def __init__(self):
        self.damage = 5
        self.durability = 10'''


class Sword(Weapon):

    def __init__(self):
        self.damage = 100
        self.durability = 10


class UnbreakableSword(Sword):
    def set_durability(self):
        pass


orc = Monster()
ok_sword = Sword
bad_sword = Weapon()
awesome_sword = UnbreakableSword()


print(orc.hp)
orc.hp -= UnbreakableSword.attack()
print(orc.hp)
