
import operations_rational as op
import sys
import fractions
def x():
    global firstnum
    firstnum = fractions.Fraction(int(input('Выберите числитель первого числа : ')),
                                  int(input('Выберите знаменатель первого числа : ')))
    return firstnum

def y():
    global secondnum
    secondnum = fractions.Fraction(int(input('Выберите числитель второго числа : ')),
                                  int(input('Выберите знаменатель второго числа : ')))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выберите тип операции: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный формат знака операции')


def res():
    if operation == '+':
        res = firstnum + secondnum
        return res
    elif operation == '-':
        res = firstnum - secondnum
        return res
    elif operation == '*':
        res = firstnum * secondnum
        return res
    elif operation == '/':
        res = firstnum / secondnum
        return res
    else:
        print('Неверный формат знака операции')


def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res()
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Результат от {x} {oper} {y} = {res}\n')
        print(f'Результат от {x} {oper} {y} = {res}\n(записан в txt file)')
        again = input('Желаете посчитать другие числа? Y/N: ').lower()
        if again == 'y':
            useresult = input('Желаете видеть результат последних вычислений? (Y/N): ').lower()
            if useresult == 'y':
                # x = res
                print(f' Последний Результат - теперь это первое число {res}')
                continue
            elif useresult == 'n':
                break
            else:
                sys.exit()
        else:
            sys.exit()

