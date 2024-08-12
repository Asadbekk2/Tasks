#Task 1
# for num in range(21):
#     if num % 2 ==1: #0 это нечетные числа
#         continue
#     print(num)

#Task 2



#Task 3

# def is_palindroma(s):
#     s = s.lower()
#     return s == s[:: -1]

# s = input("Введите строку: ")
# if is_palindroma(s):
#     print("Cтрока является палиндромом")
# else:
#     print("Строка не является палиндромом")    

#Task 4

# def sum_of_number(n):
#     return n * (n + 1) // 2

# n = int(input("Введите значение n: "))
# print("Сумма чисел от 1 до", n, "равна", sum_of_number(n))

#Task 6

#Task 5

#def sort_chisel(numbers):
#     numbers.sort()
# nums = [3,4,6,1,2,8,6,7]    
# sort_chisel(nums)
# print(f"Отсортировка чисел: {nums}")

#Task 7



#Task 8

def word_count(s):
    words = s.split()
    return len (words)

s = input("Введенное строка: ")
print("Количество слов в строке:", word_count(s))

#Task 9

#Task 10

#Task 11

#Task 12

#Task 13



#Task 14



#Task 15

# def remove_duplicates(numbers):
#     unique_numbers = []
#     for num in numbers:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers 

# numbers = [0, 1, 2, 3, 2, 4, 5, 3, 6]
# unique_numbers = remove_duplicates(numbers)
# print(unique_numbers)

#Task 16

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def text(self):
#             return f'Hello my name is {self.name}, and i {self.age} old'
    
# person = Person("Maba", 28)
# print(person.text())
# print("  ")        
        

#Task 17

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimetr(self):
#         return 2 * (self.width + self.height)

# rect = Rectangle(5,10)
# print("Площадь:", rect.area())
# print("Периметр:", rect.perimetr())       

#Task 18

# class Student:
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades
#         def text(self):
#             return f"Hello my name is {self.name}, and i have good grades {self.grades}"

# class GraduateStudent(Student):
#     def __init__(self,name,grades,thesis_title):
#         super().__init__(name,grades)
#         self.thesis_title = thesis_title

#     def text_graduate(self):
#         return f"Hello i am boy and my name is {self.name}, and i also have good grades {self.grades} this is title name {self.thesis_title}"

# graduate = GraduateStudent("Robert", 90, "New World")
# print(graduate.text_graduate())
# print("  ")
# print(graduate.text_graduate())