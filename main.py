# ЗООПАРК
import json

# Доработка классов для поддержки сериализации в JSON
class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def make_sound(self):
        print("Это метод make_sound() класса Animal")

    def eat(self):
        print(f"{self.name} ест {self.food}.")

    def to_dict(self):
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'age': self.age,
            'food': self.food
        }

class Bird(Animal):
    def __init__(self, name, age, place, food):
        super().__init__(name, age, food)
        self.place = place

    def make_sound(self):
        print(f"Птица {self.name} чирикает.")

    def eat(self):
        print(f"Птица {self.name} ест {self.food}.")

    def to_dict(self):
        data = super().to_dict()
        data.update({'place': self.place})
        return data

class Mammal(Animal):
    def __init__(self, name, age, type, color, food, sound):
        super().__init__(name, age, food)
        self.color = color
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"{self.type} {self.name} {self.sound}.")

    def eat(self):
        print(f"{self.type} {self.name} ест {self.food}.")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'type': self.type,
            'color': self.color,
            'sound': self.sound
        })
        return data

class Reptile(Animal):
    def __init__(self, name, age, type, food, sound):
        super().__init__(name, age, food)
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"{self.type} {self.name} {self.sound}.")

    def eat(self):
        print(f"{self.type} {self.name} ест {self.food}.")

    def to_dict(self):
        data = super().to_dict()
        data.update({'type': self.type, 'sound': self.sound})
        return data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} работает как {self.position}")

    def to_dict(self):
        return {
            'class': self.__class__.__name__,
            'name': self.name,
            'position': self.position
        }

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.type} {animal.name} едой {animal.food}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.type} {animal.name}.")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк")

    def show_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            animal.eat()
            animal.make_sound()

    def show_employees(self):
        print("\nСотрудники зоопарка:")
        for employee in self.employees:
            employee.work()

    def to_dict(self):
        return {
            'name': self.name,
            'animals': [animal.to_dict() for animal in self.animals],
            'employees': [employee.to_dict() for employee in self.employees]
        }

    @staticmethod
    def from_dict(data):
        zoo = Zoo(data['name'])
        animal_classes = {cls.__name__: cls for cls in [Animal, Bird, Mammal, Reptile]}
        employee_classes = {cls.__name__: cls for cls in [Employee, ZooKeeper, Veterinarian]}

        for animal_data in data['animals']:
            animal_class = animal_classes[animal_data['class']]
            if animal_data['class'] == 'Bird':
                zoo.add_animal(animal_class(animal_data['name'], animal_data['age'], animal_data['place'], animal_data['food']))
            elif animal_data['class'] == 'Mammal':
                zoo.add_animal(animal_class(animal_data['name'], animal_data['age'], animal_data['type'], animal_data['color'], animal_data['food'], animal_data['sound']))
            elif animal_data['class'] == 'Reptile':
                zoo.add_animal(animal_class(animal_data['name'], animal_data['age'], animal_data['type'], animal_data['food'], animal_data['sound']))
            else:
                zoo.add_animal(animal_class(animal_data['name'], animal_data['age'], animal_data['food']))

        for employee_data in data['employees']:
            employee_class = employee_classes[employee_data['class']]
            zoo.add_employee(employee_class(employee_data['name']))

        return zoo

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)
        print(f"\nДанные зоопарка сохранены в JSON файл {filename}")

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"\nДанные зоопарка загружены из JSON файла {filename}")
        return Zoo.from_dict(data)

# Пример использования

# Создаем объекты сотрудников
employee1 = Employee("Иван", "Охранник")
employee2 = Employee("Анна", "Ученый")
zookeeper = ZooKeeper("Олег")
veterinarian = Veterinarian("Ольга")

# Создаем животных
mammal1 = Mammal("Миша", 10, "Медведь", "бурый", "мясо", "рычит")
mammal2 = Mammal("Маша", 5, "Хомяк", "черный", "семена", "молчит")
mammal3 = Mammal("Вася", 2, "Волк", "серый", "мясо", "воет")
reptile1 = Reptile("Gena", 10, "Дракон", "мясо", "шипит")
reptile2 = Reptile("Vasya", 5, "Ящерица", "муравьи", "молчит")
bird1 = Bird("Чижик", 3, "Лес", "зерна")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo("Наш зоопарк")

zoo.add_animal(mammal1)
zoo.add_animal(mammal2)
zoo.add_animal(mammal3)
zoo.add_animal(reptile1)
zoo.add_animal(reptile2)
zoo.add_animal(bird1)

zoo.add_employee(employee1)
zoo.add_employee(employee2)
zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Показать животных и сотрудников зоопарка
zoo.show_animals()
zoo.show_employees()

# Демонстрация специфических методов сотрудников
zookeeper.feed_animal(mammal1)
veterinarian.heal_animal(reptile2)

# Сохранение состояния зоопарка в JSON файл
zoo.save_to_json('zoo_data.json')

# Загрузка состояния зоопарка из JSON файла
loaded_zoo = Zoo.load_from_json('zoo_data.json')
loaded_zoo.show_animals()
loaded_zoo.show_employees()
