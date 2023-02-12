


# Калькулятор соотношения веса и роста
weight = float(input("Ведите свой вес: "))
height = float(input("Ведите свой рост: "))
if weight/(height**2) < 18.5:
    print(weight/(height**2), "Underweight")

elif weight/(height**2) >= 18.5 and weight/(height**2) < 25:
    print(weight/(height**2), "Normal")

elif weight/(height**2) >= 25 and weight/(height**2) < 30:
    print(weight/(height**2), "Overweight")

elif weight/(height**2) >= 30:
    print(weight/(height**2), "Obesity")

























