
def lab3two():
    word = []
    while (words := str(input())) != "stop":
        word.append(words)
    print(" ".join(word))


def lab3Three():
    word = str(input())
    if "Ф" in word or "ф" in word:
        print("Ого! Это редкое слово")
    else:
        print("Эх, это не очень редкое слово")


def lab3four():
    import random
    n = 0
    x = 0
    while n != 3:
        m = random.randint(0,100)
        k = random.randint(0,100)
        print(f'{m}+{k}=', end='')
        c = input()
        while not (c.isdigit() and c != "stop"):
            print("Введите число: ", end='')
            c = input()
        if c == "stop":
            break
        if m + k == int(c):
            print("Молодец!")
            x = x + 1
        else:
            print("Ты ошибся!")
            n = n + 1
    print("Игра завершена")
    print("Верных ответов: ", x)



lab3two()
lab3Three()
lab3four()



