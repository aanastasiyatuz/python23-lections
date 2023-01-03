# string = input("Введите строку: ")

# if string.isalpha():
#     print("строка состоит только из букв")
# elif string.isdigit():
#     print("строка состоит только из чисел")
# else:
#     flag = False
#     for symbol in string:
#         if symbol not in "~!@#$%^&*()_+-={}|:<>?":
#             flag = True
    
#     if flag:
#         print("это ASCII")
#     else:
#         print("строка состоит из символов")

# 11
# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.


# склонения слов
amount = input()
last_digit = int(amount[-1])
flag = True
if len(amount) > 1:
    last_2_digits = int(amount[-2:])
    if last_2_digits > 10 and last_2_digits < 20:
        print(f"{amount} коров")
        flag = False
if flag:
    if last_digit == 1:
        print(f"{amount} корова")
    elif last_digit < 5 and last_digit > 0:
        print(f"{amount} коровы")
    else:
        print(f"{amount} коров")


