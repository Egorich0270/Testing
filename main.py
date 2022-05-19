from Functione import *

if __name__ == '__main__':
    HP = 100
    main = {'1': attack, '2': sleep, '3': statChec}
    while True:
        HP = 100
        while HP > 0:#Game
            comand = input('1.Атака\n2.Сон\n3.Статы\n\nВведите команду')
            if comand in main.keys():
                HP = main.get(comand)(HP)
        print('чувак ты труп')



##ты лохgv
