i = 10
# if i > 10:
#     a = 10
#     print(b)
#     if a > 10:
#         print(a)
#         b = 10
#
#
# print(b)
# print(a)
# print(i)
# a = 1
#
# class Name:
#     a = 10
#
#     def __init__(self, name, age):
#         self.name = 'Alex'
#         self.new_name = name
#         self.my_age = age
#
#     def print_name(self):
#         print(self.name, self.new_name)
#         print(self.my_age)
#
#
# Name('New Name', 22).print_name()


# class Human:
#     hp = 100
#     armor = 100
#
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#
#     def shoot_in_leg(self, damage_hp, damage_armor):
#         print(f"{self.name} get damage")
#         self.hp = self.hp - damage_hp
#         self.armor = self.armor - damage_armor
#
#     def shoot_in_body(self, damage_hp, damage_armor=0):
#         print(f"{self.name} get body damage")
#         self.hp = self.hp - damage_hp
#         self.armor = self.armor - damage_armor
#
#
# police_man = Human('Policeman', 'deagle')
# military = Human('Military', 'ak-47')
#
# print(police_man.weapon)
# print(military.weapon)
# print()
#
# police_man.shoot_in_leg(20, 35)
# print("Police man hp:", police_man.hp, "\nPolice man armor:", police_man.armor)
# print()
#
# military.shoot_in_leg(23, 10)
# print("Military man hp:", military.hp, "\nMilitary man armor:", military.armor)
# print()
#
# print("Police man hp:", police_man.hp)
# print("Military hp:", military.hp)
# print()
#
#
# police_man.shoot_in_body(70)
# print("Police man hp:", police_man.hp, "\nPolice man armor:", police_man.armor)
#
# military.shoot_in_body(55, 10)
# print("Military man hp:", military.hp, "\nMilitary man armor:", military.armor)


# class Character:
#     def __init__(self, name, ability, weapon):
#         self.name = name
#         self.hp = 100
#         self.ability = ability
#         self.weapon = weapon
#
#     def hit(self):
#         print(f'{self.name} hit smth with {self.weapon}')
#
#     def damage(self, damage: int):
#         self.hp -= damage
#         print(f"Get {damage} damage! HP left: {self.hp}")
#
#     def heal(self):
#         self.hp += 10
#         print(self.hp)
#
#
# Character('Alex', 100, 'Stick').hit()
# Character('Alex', 100, 'Stick').heal()
#
# character = Character('Alex', 100, 'Stick')
# character.hit()
# character.heal()
# character.heal()
# character.damage(50)
# character.damage(12)
#
# user_input = int(input("Enter damage to give: "))
# character.damage(user_input)

# from class_pet import Pet

# class Pet:
#     paws = 4
#     eyes = 2
#     color = 'Black'
#
#
# class Dog(Pet):
#     color = 'White'
#
#
# class Cat(Pet):
#     color = 'Red'
#
#
# pet = Pet()
# cat = Cat()
# dog = Dog()
#
# print(dog.paws)
# print(cat.paws)
#
# print(pet.color)
# print(dog.color)
# print(cat.color)


# class Pet:
#     def __init__(self, color):
#         self.paws = 4
#         self.eyes = 2
#         self.color = color
#
#
# class Dog(Pet):
#     def __init__(self, color):
#         super().__init__(color)
#         self.color = color
#
#
# dog = Dog('Black')
# print(dog.paws)


# Создать класс Human с атрибутами hands=2, legs=2, head=1
# Унаследовать класс и добавить имя и возраст
# Распечатать все атрибуты


# class Human:
#     hands = 2
#     legs = 2
#     head = 1
#
#
# class Man(Human):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# alex = Man('Alex', 22)
# print(alex.name)
# print(alex.age)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_noise(self):
#         print(f'{self.name} makes meow')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_noise(self):
#         print(f'{self.name} makes wof')
#
#
# cat = Cat('Cat')
# dog = Dog('Dog')
#
# cat.make_noise()
# dog.make_noise()


class Character:
    def __init__(self, legion, name, hp, mp, dmg, medicine):
        self.legion = legion
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.medicine = medicine

    def walk(self):
        print(f"{self.name} goes forward")

    def attack(self, mp):
        self.mp -= mp
        print(f'{self.name} attack enemy and lost {mp}. Left mp: {self.mp}')
        print(f'{self.name} give {self.dmg} damage')
        return self.dmg


    def defend(self, mp):
        self.mp += mp
        print(f'{self.name} defend against enemy and won one {mp}.left mp {self.mp}')
        print(f'{self.name} defend himself form {self.dmg} damage')
        return self.dmg

    def heal_itself(self, mp, medicine):
        self.medicine += medicine
        print(f'{self.name} medicine itself if it get a {self.dmg} damage' )
        return self.medicine



a = Character('aad', 34, 34, 55, 'sdf', 44)
a.walk()
a.attack(3)
a.defend(3)
a.heal_itself('dd', 6)





