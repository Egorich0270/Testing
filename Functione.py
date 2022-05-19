def isezyy(a):
    flag = True
    a = int(a)
    for x in range(1, (int((a**0.5)+1))):
        if (x != 1 and x != a):
            if a%x == 0:
                flag = False
                break
    return(flag)

def simbv(num, sys=10):
    count=0
    while num // int(sys) != 0:
        count += 1
        num //= int(sys)
    return (count+1)

def attack(hp):
    demage = 12
    return hp-demage

def sleep(hp):
    heal = 20
    return hp+heal

def statChec(hp):
    print(hp)
    return (hp)

def shop(babki):
    prises = {'1': 1000, '2': 2000}
    otv = input(f'Что вы хотите купить?\n1)Доспех за {prises.get(str(1))}\n2)Кровать за {prises.get(str(2))}\n3)Ничего?\n')



