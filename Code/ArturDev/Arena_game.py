import random


class Hero:
    clas = None
    name = 'Goge'

    def present(self):
        print(f'я {self.name}, мой класс {self.clas}, статы:{self.hp,self.dmg}')


class Ranger(Hero):
    clas = 'Ranger'

    def __init__(self):
        self.hp = 90 - random.randint(1, 20)
        self.dmg = 20 + random.randint(1, 5)


class Knight(Hero):
    clas = 'Knight'

    def __init__(self):
        self.hp = 200 - random.randint(1, 20)
        self.dmg = 10


class Paladin(Hero):
    clas = 'Paladin'

    def __init__(self):
        self.hp = 100 + random.randint(1, 20)
        self.dmg = 10 + random.randint(1, 5)


def generate_hero():
    return [Ranger(), Paladin(), Ranger(), Knight(), Knight()]


while True:
    hero_list = generate_hero()
    print(Hero.present(hero_list[int(input('prosmotr'))]))