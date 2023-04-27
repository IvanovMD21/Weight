from PIL import Image, ImageFilter
from pathlib import Path
import csv
def nom1():
    path = Path.cwd()
    filename = Path(path).glob('*')
    Path("new_path").mkdir(parents=True, exist_ok=True)
    for file in filename:
        with Image.open(file) as img:
            img.load()
            new_file = img.filter(ImageFilter.CONTOUR)
            new_file.save(Path("new_path/new" + str(file)))


def nom2():
    path = ""
    filename = Path(path).glob('*')
    Path("new_path").mkdir(parents=True, exist_ok=True)
    for file in filename:
        if file.suffix in [".jpg",".png"]:
            with Image.open(file) as img:
                img.load()
                new_file = img.filter(ImageFilter.CONTOUR)
                new_file.save(Path("new_path/new", file))


def nom3():
    file = open("lab9exel.csv","r")
    data = list(csv.reader(file, delimiter=","))
    print("Список товаров: ")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб")
    print(f"Итоговая цена: {sum([int(i[1])*int(i[2]) for i in data])} руб.")

nom3()



