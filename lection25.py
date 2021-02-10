# #
# #
# #
# #
# #
# # class Sanjar:
# #       count = 0
# #     def __init__(self, age, surname, name, job):
# #         self.age = age
# #         self.name = name
# #         self.surname = surname
# #         self.job = job
# #
# #     def print_persanality(self, age, job, name, surname):
# #         a = input("hello , you was welcome to moldogazieva's family!!!"
# #                   "what do you want to know about Sanjar:    ")
# #         if a == 'age':
# #            print(f"sanjar is {age} years old")
# #         elif a == "name":
# #             print(f"{name}")
# #         elif a == 'job':
# #             print(f"sanjar is a {job}")
# #         elif a == "surname":
# #             print(f"{surname}")
# #
# #
# #     def walk:
# #         a = input("do you want to continue?   ")
# #         if a == 'yes':
# #             print("okay")
# #         else:
# #             print("bye")
# #
# #
# # s = Sanjar(50,'policie', 'sanjar', 'moldogaziev')
# # s.print_persanality(50,'policie', 'sanjar', 'moldogaziev')
#
# class Animal:
#     def __init__(self, animal):
#         self.animal = animal
#         self.limbs = 'limbs'
#         self.eyes = 2
#
#     def print_animal(self):
#         print(f"animal {self.animal}")
#         print(f"number of the eyes {self.eyes}")
#         print(f"limbs are {self.limbs}")
#
#     def walk(self):
#         print("animal walk")
#
# class Cat(Animal):
#     def __init__(self, animal):
#         super().__init__(animal)
#         self.limbs = 'paws'
#
#
#     def walk(self):
#         print("cat walks")
#
#
#
# class Fish(Animal):
#     def __init__(self, animal):
#         super().__init__(animal)
#         self.limbs = 'fins'
#
#     def walk(self):
#         print("fish swims")
#
#
#
#
# class Pigeon(Animal):
#     def __init__(self, animal):
#         super().__init__(animal)
#         self.limbs = 'fins'
#
#     def walk(self):
#         print("pigeon fly")
#
#
#
# cat = Cat('cat')
# pigeon = Pigeon('pigeon')
# fish = Fish('fish')
#
#
# cat.print_animal()
# cat.walk()
# print()
# fish.print_animal()
# fish.walk()
# print()
# pigeon.print_animal()
# pigeon.walk()
# print()


class Animal:
    def __init__(self, animal):
        self.animal = animal
        self.eyes = 2
        self.limbs = 'limbs'

    def print_animal(self):
        print(f"animal {self.animal}")
        print(f"number of eyes {self.eyes}")
        print(f"this animal with {self.animal}")

    def walk(self):
        print("animal walks")


class Cat(Animal):
    def __init__(self, animal):
        super().__init__(animal)
        self.limbs = 'paws'


    def walk(self):
        print("cat walks")


class Fish(Animal):
    def __init__(self, animal):
        super().__init__(self)
        self.limbs = 'fins'

    def walk(self):
        print("fish swims")

class Pigeon(Animal):
    def __init__(self, animal):
        super().__init__(self)
        self.limbs = 'wings'

cat = Cat(Cat)
fish = Fish(Fish)
pigeon = Pigeon(Pigeon)

cat.print_animal()
cat.walk()
print()
fish.print_animal()
fish.walk()
print()
pigeon.print_animal()
pigeon.walk()
print()




