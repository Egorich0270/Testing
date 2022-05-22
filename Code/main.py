from Code.Functione import *

if __name__ == '__main__':
    main = {'1': attack, '2': sleep, '3': statChec, '4':shop}
    while True:
        HP = 100
        babki  = 1000
        while HP > 0:#Game
            comand = input('1.Атака\n2.Сон\n3.Статы\n4.В магазин\n\nВведите команду\n')
            if comand in main.keys():
                if comand == '4':
                    babki = shop(babki)
                else:
                    HP = main.get(comand)(HP)
        print('чувак ты труп')



##ты лохgv

