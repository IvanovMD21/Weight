def nom1():
    try:
        a = int(input())
        n = a / 3
    except ValueError:
        print("это не число")
    else:
        if a == 0:
            print("при делении любого числа на 0 всегда будет 0")
        elif a % 3 == 0:
            print(n)
        else:
            print("Ошибка")




def nom2():
    try:
        a = int(input())
        n = 100 / a
    except ValueError:
        print("это не число")
    except ZeroDivisionError:
        print("введен 0")
    else:
        print(n)



def nom3():
    date = input("Формат: дд.мм.гггг: ")
    date.split(".")
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print("Magic date")
    else:
        print("Not magic date")

def nom4():
    tic = input()
    a = 0
    b = 0
    if len(tic) % 2 == 0:
        for i in tic[int(len(tic) / 2 )]:
            a = a + int(i)
        for i in tic[int(len(tic) / 2):int(len(tic)) + 1]:
            b = b + int(i)
        if a == b:
            print("Lucky ticket")
        else:
            print("Not lucky ticket")
    else:
        print("не четно")

nom1()
nom2()
nom3()
nom4()