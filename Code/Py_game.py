class MainH:

    def __init__(self):
        self.HP = 100

    def attack(self):
        self.HP -= 10

    def statChec(self):
        print(self.HP)
        input()

    def sleep(self):
        self.HP+=12


if __name__ == '__main__':

    while True:
        hero = MainH()
        main = {'1': hero.attack, '2': hero.sleep, '3': hero.statChec}

        while hero.HP > 0:#Game
            comand = input('1.Атака\n2.Сон\n3.Статы\n\nВведите команду\n')
            if comand in main.keys():
               main.get(comand)()
        print('чувак ты труп')
        input()
