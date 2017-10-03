import random
    

def hit(fighter):
    while True:
        h = input('Боец ' + str(fighter) + ', выберите действие: ')
        try:
            h = int(h)
        except:
            print('Вводите только цифры')
            continue    
        if h > 4 or h < 0:
            print('Вводите только цифры из списка')
            continue
        else:
            break
    return h


def fortune(fighter):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    print('Боец ' + str(fighter) + ':  ' + str(a), str(b))
    return a + b 


def isQuit(first, second):
    if first == 0 and second == 0:
        print('Боец 1: сдался')
        print('Боец 2: сдался')
        print('Ничья!')
        return False
    elif first == 0:
        print('Боец 1: сдался')
        print('Боец 2: Победил!')
        return False
    elif second == 0:
        print('Боец 2: сдался')
        print('Боец 1: Победил!')
        return False
    return True    


def isBlock(h_first, f_first, h_second, f_second):
    if h_first == 4 and h_second == 4:
        print('Оба бойца поставили блок')
        return True
    elif h_first == 4:
        if f_first > f_second:
            print('Боец 1: заблокировал удар')
            return True
        else:
            print('Боец 1: неудачный блок')
            return False
    elif h_second == 4:
        if f_second > f_first:
            print('Боец 2: заблокировал удар')
            return True
        else:
            print('Боец 2: неудачный блок')
            return False
    return False

def hitStatus(fighter, hit, fortune):
    damage = 0
    if fortune < 5:
        print('Боец ' + str(fighter) +': неудачный удар')
        return 0
    elif fortune > 4 and hit != 3:
        if hit == 1:
            if fortune == 12:
                print('Боец ' + str(fighter) +': критический удар левой рукой')
                damage = 2
                return damage
            print('Боец ' + str(fighter) +': удар левой рукой')
            damage = 1
            return damage
        elif hit == 2:
            if fortune == 12:
                print('Боец ' + str(fighter) +': критический удар правой рукой')
                damage = 3
                return damage
            print('Боец ' + str(fighter) +': удар правой рукой')
            damage = 2
            return damage
    elif fortune > 8:
        if hit == 3:
            if fortune == 12:
                print('Боец ' + str(fighter) +': критический ногой')
                damage = 4
                return damage
            print('Боец ' + str(fighter) +': удар ногой')
            damage = 3
            return damage


def isKO(first, second):
    if first <= 0 and second <= 0:
        print('Оба бойца повержены')
        print('Ничья!')
        return True
    elif first <= 0:
        print('Боец 1: повержен')
        print('Боец 2: Победил!')
        return True
    elif second <= 0:
        print('Боец 2: повержен')
        print('Боец 1: Победил!') 
        return True
    return False


health1 = 10
hit1 = 0
fortune1 = 0

health2 = 10
hit2 = 0
fortune2 = 0

while True:
    print('[0] - сдаться')
    print('[1] - удар левой рукой (1 урона)')
    print('[2] - удар правой рукой (2 урона)')
    print('[3] - удар ногой (3 урона)')
    print('[4] - поставить блок')
    
    for i in range(1,3):
        h = hit(i)
        f = fortune(i)
        if i == 1:
            hit1 = h
            fortune1 = f
        else:
            hit2 = h
            fortune2 = f
            
    fight = isQuit(hit1, hit2)
    if not fight:
        break
    if isBlock(hit1, fortune1, hit2, fortune2):
        continue

    for n in range(1,3):
        if n == 1:
            damage = int(hitStatus(n, hit1, fortune1))
            health2 -= damage 
        else:
            damage = int(hitStatus(n, hit2, fortune2))
            health1 -= damage

    out = isKO(health1, health2)
    if out:
        break
    
    print('Боец 1: ' + str(health1) + ' здоровья')
    print('Боец 2: ' + str(health2) + ' здоровья')
