from Functione import *

if __name__ == '__main__':
    main = {'1': attack(), '2': sleep(), '3': statChec()}
    while True:
        comand = input('1.Атака\n2.Сон\n3.Статы\n\nВведите команду')
        if comand in main.keys(): print(main.get(comand))




##ты лох
