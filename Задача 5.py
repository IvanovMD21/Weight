n = int(input("Введите кол-во слов: "))
word = ""
for n in range(n):
    word += input("Введите слово: ") + ' '
print(word)