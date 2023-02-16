place = int(input("Введите место: "))

if place%2 == 0 and place >= 1 and place <=36:
    print("Купе верхнее")
elif place%2 == 1 and place >= 1 and place <=36:
    print("Купе нижнее")
elif place%2 == 0 and place >= 37 and place <=53:
    print("Боковое верхнее")
elif place%2 == 1 and place >= 37 and place <=53:
    print("Боковое нижнее")
else:
    print("Неверно указано место")