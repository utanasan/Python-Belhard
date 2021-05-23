class Win_Door:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'

class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.length = y
        self.height = z
        self.wd = []

    def Square_equal(self):
        self.square = 2 * self.height * (self.width + self.length)
        return self.square

    def Rolls(self, x, y):
        return round(self.Square_equal() / (x * y))


    def addWD(self, w, h, name='unk'):
        self.wd.append(Win_Door(w, h, name))

    def workSurface(self):
        new_square = float(self.Square_equal())
        for i in self.wd:
            new_square -= i.square
        return new_square


while True:
    try:
        x = float(input("Длина комнаты: "))
        y = float(input("Ширина комнаты: "))
        z = float(input("Высота стен в комнате: "))
        break
    except ValueError:
        print("Допустим ввод только чисел")
r1 = Room(x, y, z)
print("Для добавления окна/двери/другого элемента, введите высоту и ширину элемента.")
print("После введения параметров всех элементов нажмите Enter")
while True:
    try:
        x_WD = input("Высота добавляемого элемента: ")
        if x_WD == "":
            break
        y_WD = input("Ширина добавляемого элемента: ")
        r1.addWD(float(x_WD), float(y_WD))
    except ValueError:
        print("Допустим ввод только чисел")
while True:
    try:
        x_R = float(input("Введите длину рулона: "))
        y_R = float(input("Введите ширину рулона: "))
        break
    except ValueError:
        print("Допустим ввод только чисел")
print(f"Площадь поверхности для оклейки составляет: {r1.workSurface()} кв.м.")
print(f"Всего нужно {r1.Rolls(x_R, y_R)} рулонов.")
