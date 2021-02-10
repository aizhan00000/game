#
# class Animal:
#     name = 'Ai'
#     animal_type = 'cat'
#
# class Dog(Animal):
#     pass
#
# dog = Dog()
# print(dog.name)
# print(f'{Animal.name} is a {dog.animal_type}')

# class People:
#     count = 0
#     work = ''
#
#     def add_man(self):
#         self.count += 1
#
# class Police(People):
#     work = 'Police'
#
# class Farmer(People):
#     work = 'Farmer'
#
#
# police = Police()
# print(police.add_man())


# class House:
#     def __init__(self, people):
#         self.people_count = people
#
#     def count_people(self, people_came):
#         self.people_count += people_came
#         print("кол-во: " + str(self.people_count))
#
#
# class HouseNo219(House):
#     pass
#
#
# class HouseNo72(House):
#     pass
#
#
# house_219 = HouseNo219(6)
# house_72 = HouseNo72(4)
#
#
# people_coming = int(input("enter a count of people:  "))
#
# house_72.count_people(people_coming)
# house_219.count_people(people_coming)

#
# class SchoolMember:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, position):
#         super(Teacher, self).__init__(name, age, position)
#
#
#     def give_mark(self):
#         mark = int(input("give mark:  "))
#         return mark
#
#
# class Student(SchoolMember):
#     def __init__(self, name, age, position, grade):
#         super(Student, self).__init__(name, age, position)
#         self.grade = grade
#
#
#     def get_mark(self, mark):
#         print(f"{self.name} get {mark}")
#
# teacher = Teacher('Aijan', 18, 'teacher')
# student = Student('Aidana', 18, 'student', 7)
#
# teacher_mark = teacher.give_mark()
# student.get_mark(teacher_mark)









