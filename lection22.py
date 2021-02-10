# class Animal:
#     def __init__(self, eyes, limbs):
#         self.eyes_count = eyes
#         self.limbs = limbs
#
#     def eyes_count(self, eyes):
#         self.eyes_count += eyes
#         print("кол-во: " + str(self.eyes_count()))
#
#     def count_limbs(self, limbs):
#         self.count_limbs += limbs
#         print("кол-во: " + str(self.count_limbs()))
#
#
# class Cat(Animal):
#     def __init__(self, eyes, limbs, paws):
#         super(Cat, self).__init__(eyes, limbs)
#         self.paws = paws
#
#
# class Fish(Animal):
#     def __init__(self, eyes, limbs, fins):
#         super(Cat, self).__init__(eyes, limbs)
#         self.fins = fins
#
#
# class Pigeon(Animal):
#     def __init__(self, eyes, limbs, wings):
#         super(Cat, self).__init__(eyes, limbs)
#         self.wings = wings
#
#
# cat = Cat(2, 4, 2)
# fish = Fish(2, 3, 4)
# pigeon = Pigeon(3, 4, 10)
# Cat.count_limbs(limbs=3)

