def Monster_leveling(lvl, max_level, cost):
    summa = 0
    for x in range(lvl, max_level):
        print(f'для апа {x+1} уровня потребуется {cost*4} еды')
        summa += cost * 4
        cost *= 2

    print(f'{summa} еды всего, это {summa*10} голды')


Monster_leveling(int(input('лвл\n')), int(input('нужный левел\n')), int(input('цена апа\n')))