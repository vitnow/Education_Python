
class House:
    houses_history = []
    def  __new__ (cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.houses_history = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1<= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {len(self)}"

    def __eq__(self, other):
        return self.number_of_floors == other
    def  __lt__(self, other):
        return self.number_of_floors < other
    def  __le__(self, other):
        return self.number_of_floors <= other
    def  __gt__(self, other):
        return self.number_of_floors > other
    def  __ge__(self, other):
        return self.number_of_floors >=  other
    def  __ne__(self, other):
        return self.number_of_floors !=  other
    def __add__(self, value):
        self.number_of_floors += value
        return self
    def __iadd__(self, other):
        return self + other
    def __radd__(self, other):
        return self + other



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
del h1
print('Данные объекты хранятся только в нашей памяти:',House.houses_history)