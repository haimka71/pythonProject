#
# if type == 'c':
#     repeat = True
import calculatortype as ty
import operations_rational as op
import operations_complex as opCom
import sys


def inputcom():
    global comnum
    m = int(input('\tВыберите действительную часть числа: ').replace(',', '.'))
    y = int(input('\tВыберите мнимую часть числа: ').replace(',', '.'))
    comnum = complex (m,y)
    print(f'Комплексное число: {comnum}\n')
    return comnum



def selectoperation():
    global operation
    operation = (input(f'Выберите тип операции: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный формат знака операции')


def res_com(x,y):
    if operation == '+':
        res = x + y
        return res
    elif operation == '-':
        res = x - y
        return res
    elif operation == '*':
        res = x * y
        return res
    elif operation == '/':
        res = x / y
        return res
    else:
        print('Неверный формат знака операции')

def mainterminalcom():
    global file

    while True:
        x = opCom.inputcom()
        y = opCom.inputcom()
        oper = opCom.selectoperation()
        res = opCom.res_com(x,y)
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

