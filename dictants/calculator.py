is_exit = False

operations = ('+', '-', '*', '**', '/', '//')

while not is_exit:
    try:
        num1 = int(input("Введите 1 число: "))
        num2 = int(input("Введите 2 число: "))
        oper = input("Введите операцию: ")
        if oper not in operations:
            raise Exception

        if oper == '+':
            print(f"{num1} + {num2} = {num1+num2}")
        elif oper == '-':
            print(f"{num1} - {num2} = {num1-num2}")
        elif oper == '*':
            print(f"{num1} * {num2} = {num1*num2}")
        elif oper == '**':
            print(f"{num1} ** {num2} = {num1**num2}")
        elif oper == '/':
            print(f"{num1} / {num2} = {num1/num2}")
        else:
            print(f"{num1} // {num2} = {num1//num2}")

        if input('Вы хотите выйти (y/n)? ').lower() == 'y':
            is_exit = True

    except ZeroDivisionError:
        print("На 0 делить нельзя!")
    except ValueError:
        print("Введите число!")
    except Exception:
        print("Такой операции нет!")
