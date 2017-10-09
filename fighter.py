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


def is_quit(first, second):
    if first == 0 and second == 0:
        print('Боец 1: сдался')
        print('Боец 2: сдался')
        print('Ничья!')
        return False

    if first == 0:
        print('Боец 1: сдался')
        print('Боец 2: Победил!')
        return False

    if second == 0:
        print('Боец 2: сдался')
        print('Боец 1: Победил!')
        return False

    return True    


def is_block(h_first, f_first, h_second, f_second):
    if h_first == 4 and h_second == 4:
        print('Оба бойца поставили блок')
        return True

    if h_first == 4:
        if f_first > f_second:
            print('Боец 1: заблокировал удар')
            return True
        else:
            print('Боец 1: неудачный блок')
            return False

    if h_second == 4:
        if f_second > f_first:
            print('Боец 2: заблокировал удар')
            return True
        else:
            print('Боец 2: неудачный блок')
            return False

    return False


def hit_status(fighter, _hit, _fortune):
    if _hit == 4:
        return 0

    if _fortune < 5:
        print('Боец ' + str(fighter) + ': неудачный удар')
        return 0

    if 5 <= _fortune <= 8:
        if _hit == 1:
            print('Боец ' + str(fighter) + ': удар левой рукой')
            return 1
        if _hit == 2:
            print('Боец ' + str(fighter) + ': удар правой рукой')
            return 2
        if _hit == 3:
            print('Боец ' + str(fighter) + ': неудачный удар')
            return 0

    if _fortune > 8:
        if _hit == 1:
            if _fortune == 12:
                print('Боец ' + str(fighter) + ': критический удар левой рукой')
                return 2
            print('Боец ' + str(fighter) + ': удар левой рукой')
            return 1
        if _hit == 2:
            if _fortune == 12:
                print('Боец ' + str(fighter) + ': критический удар правой рукой')
                return 3
            print('Боец ' + str(fighter) + ': удар правой рукой')
            return 2
        if _hit == 3:
            if _fortune == 12:
                print('Боец ' + str(fighter) + ': критический удар ногой')
                return 4
            print('Боец ' + str(fighter) + ': удар ногой')
            return 3


def is_ko(first, second):
    if first <= 0 and second <= 0:
        print('Оба бойца повержены')
        print('Ничья!')
        return True

    if first <= 0:
        print('Боец 1: повержен')
        print('Боец 2: Победил!')
        return True

    if second <= 0:
        print('Боец 2: повержен')
        print('Боец 1: Победил!') 
        return True

    return False


def main():
    health1 = 10
    hit1 = 0
    fortune1 = 0

    health2 = 10
    hit2 = 0
    fortune2 = 0

    print('[0] - сдаться')
    print('[1] - удар левой рукой (1 урона)')
    print('[2] - удар правой рукой (2 урона)')
    print('[3] - удар ногой (3 урона)')
    print('[4] - поставить блок')

    while True:
        for i in range(1, 3):
            h = hit(i)
            f = fortune(i)
            if i == 1:
                hit1 = h
                fortune1 = f
            else:
                hit2 = h
                fortune2 = f

        fight = is_quit(hit1, hit2)
        if not fight:
            break
        if is_block(hit1, fortune1, hit2, fortune2):
            continue

        for n in range(1, 3):
            if n == 1:
                damage = int(hit_status(n, hit1, fortune1))
                health2 -= damage
            else:
                damage = int(hit_status(n, hit2, fortune2))
                health1 -= damage

        out = is_ko(health1, health2)
        if out:
            break

        print('Боец 1: ' + str(health1) + ' здоровья')
        print('Боец 2: ' + str(health2) + ' здоровья')


while True:
    string = input('Чтобы начать игру нажмите Enter')

    if not string:
        main()
    else:
        break
