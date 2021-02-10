class Robot:
#     population = 1
#
#     def __init__(self, name):
#         self.name = name
#         print('(Инициализация {0})'.format(self.name))
#
#     def __del__(self):
#         print('{0} уничтожается!'.format(self.name))
#         self.population -= 1
#         if self.population == 0:
#             print('{0} был последним.'.format(self.name))
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#
#     def sayHi(self):
#         print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
#         print('У нас {0:d} роботов.'.format(Robot.population))
#
#
# robot = Robot('Robot')
# robot_2 = Robot('Robot 2')
# robot.sayHi()
# del robot
# robot_2.sayHi()
# robot.sayHi()


# class Cat:
#     name = 'Alice'
#     animal_type = 'cat'
#
# class Dog(Cat):
#     pass
#
#
# dog = Dog()

# class Animal:
#     say = 'Meow'
#
#     def say_smth(self):
#         print(f'{self.say}')
#
#
# class Cat(Animal):
#     pass
#
#
# class Dog(Animal):
#     def say_smth(self):
#         print(f'{self.say}')
#
#
# class Fish(Dog):
#     say = 'None'
#     pass
#
#
# Dog().say_smth()
# Cat().say_smth()
# Fish().say_smth()


# class People:
#     count = 0
#     work = ''
#
#     def add_man(self):
#         self.count += 1
#         print(f"You added 1 {self.work}")
#         print(f'{self.work} - {self.count}')
#
#
# class Police(People):
#     work = 'Police'
#
#
# class Farmer(People):
#     work = 'Farmer'
#
#     def add_man(self):
#         count = 5
#         self.count += count
#         print(f"You added {count} {self.work}")
#         print(f'{self.work} - {self.count}')
#
# def run():
#     police = Police()
#     farmer = Farmer()
#     police.add_man()
#     police.add_man()
#     farmer.add_man()
#
# run()


# class House:
#     def __init__(self, number, people):
#         self.house_number = number
#         self.people_cnt = people
#
#     def count_people(self, people_came):
#         self.people_cnt += people_came
#         print(f"Номер дома: {self.house_number}")
#         print("Кол-во жителей: " + str(self.people_cnt))
#         print('----------------')
#
#
# house_219 = House(219, 6)
# house_72 = House(72, 0)
#
#
# people_coming = int(input("Enter count of people: "))
#
# house_219.count_people(people_coming)
# house_72.count_people(people_coming)


# class SchoolMember:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, position):
#         super().__init__(name, age, position)
#
#     def give_mark(self):
#         mark = int(input("Give mark: "))
#         return mark
#
#
# class Student(SchoolMember):
#     def __init__(self, name, age, position, grade):
#         super().__init__(name, age, position)
#         self.grade = grade
#
#     def get_mark(self, give_mark):
#         print(f"{self.name} get {give_mark}")
#
#
# teacher = Teacher('Марья Ивановна', 56, 'Учитель')
# student = Student('Петров', 12, 'Ученик', 5)
#
# teacher_mark = teacher.give_mark()
# student.get_mark(teacher_mark)


class Character:
    def __init__(self, legion, name, hp, mp, dmg, mana_dmg):
        self.legion = legion
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.mana_dmg = mana_dmg

    def walk(self):
        print(f"{self.name} goes forward")

    def attack(self):
        dmg = self.dmg
        return dmg

    def ability(self):
        dmg = self.mana_dmg
        return dmg

    def get_dmg(self, dmg):
        self.hp -= dmg


class Human(Character):
    def __init__(self, legion, name, hp, mp, dmg, mana_dmg):
        super().__init__(legion, name, hp, mp, dmg, mana_dmg)


class Orc(Human):
    def __init__(self, legion, name, hp, mp, dmg, mana_dmg):
        super().__init__(legion, name, hp, mp, dmg, mana_dmg)


human = Human('Human', 'Artos', 100, 100, 25, 45)
orc = Orc('Orc', 'Trall', 100, 100, 35, 50)

print("Human attack!")
human_dmg = human.attack()
orc.get_dmg(human_dmg)
print(f"Orc hp: {orc.hp}")

print("Orc attack!")
orc_dmg = orc.attack()
human.get_dmg(orc_dmg)
print(f"Human hp: {human.hp}")

print("Orc ability attack!")
orc_dmg = orc.ability()
human.get_dmg(orc_dmg)
print(f"Human hp: {human.hp}")