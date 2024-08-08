# ЗООПАРК
import pickle

class Animal:
  def __init__(self, name, age, food):
      self.name = name
      self.age = age
      self.food = food

  def make_sound(self):
      print("Это метод make_sound() класса Animal")

  def eat(self):
      print(f"{self.name} ест {self.food}.")

class Bird(Animal):
  def __init__(self, name, age, place, food):
      super().__init__(name, age, food)
      self.place = place

  def make_sound(self):
      print(f"Птица {self.name} чирикает.")
  def eat(self):
    print(f"Птица {self.name} ест {self.food}.")

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

class Reptile(Animal):
  def __init__(self, name, age, type, food, sound):
      super().__init__(name, age, food)
      self.type = type
      self.sound = sound
    
  def make_sound(self):
      print(f"{self.type} {self.name} {self.sound}.")
  def eat(self):
      print(f"{self.type} {self.name} ест {self.food}.")

# Создаем объекты животных
mammal1 = Mammal("Миша", 10, "Медведь", "бурый", "мясо", "рычит")
mammal2 = Mammal("Маша", 5, "Хомяк", "черный", "семена", "молчит")
mammal3 = Mammal("Вася", 2, "Волк", "серый", "мясо", "воет")
reptile1 = Reptile("Gena", 10, "Дракон", "мясо", "шипит")
reptile2 = Reptile("Vasya", 5, "Ящерица", "муравьи", "молчит")
bird1 = Bird("Чижик", 3, "Лес", "зерна")

# Демонстрация полиморфизма
animals = [mammal1, mammal2, mammal3, reptile1, reptile2, bird1]
for animal in animals:
  animal.make_sound()

# Композиция
class Employee:
  def __init__(self, name, position):
      self.name = name
      self.position = position

  def work(self):
      print(f"{self.name} работает как {self.position}")

# 5: 
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
# Модуль работы с файлами
  def save_to_file(self, filename):
    with open(filename, 'wb') as file:
      pickle.dump(self, file)
    print(f"Данные зоопарка сохранены в файл {filename}")

  @staticmethod
  def load_from_file(filename):
    with open(filename, 'rb') as file:
      zoo = pickle.load(file)
    print(f"Данные зоопарка загружены из файла {filename}")
    return zoo

    # Создаем объекты сотрудников
employee1 = Employee("Иван", "Охранник")
employee2 = Employee("Анна", "Научный сотрудник")
zookeeper = ZooKeeper("Олег")
veterinarian = Veterinarian("Ольга")

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

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_data.pkl')

# Загрузка состояния зоопарка из файла
loaded_zoo = Zoo.load_from_file('zoo_data.pkl')

loaded_zoo.show_animals()
loaded_zoo.show_employees()

