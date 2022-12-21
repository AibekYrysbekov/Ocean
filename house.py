class Furniture:
    def __init__(self, name, squre):
        self.name = name
        self.squre = squre

    def __str__(self):
                 return f'Мебель: {self.name} Занятая площадь:{self.squre} квадратных метра.'

class House:
    def __init__(self, house_type, squre):
        self.house_type = house_type
        self.squre = squre
        self.free_squre = squre
        self.furniture_list = []

    def __str__(self):
                 return f'Тип дома {self.house_type} площадь {self.squre} остаточная площадь {self.free_squre} список мебели {self.furniture_list}'

    def add_furniture(self,furniture):
        self.furniture_list.append(furniture.name)
        self.free_squre-=furniture.squre



bedroom = Furniture('bedroom',4)
wardrobe = Furniture('wardrobe',2)
table = Furniture('table',1.5)

print (bedroom)
print (wardrobe)
print (table)


my_house = House ('Townhouse', 116)

my_house.add_furniture(bedroom)
my_house.add_furniture(wardrobe)
my_house.add_furniture(table)

print (my_house)