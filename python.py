#Task 1
# for num in range(21):
#     if num % 2 ==1: #0 это нечетные числа
#         continue
#     print(num)

#Task 2

# def minimal_chisla(number):
#     if not number:
#         return None
    
#     min_number = number[0]
#     for num in number:
#         if num < min_number:
#             min_number = num

#         return min_number

# numbers = [5,4,1,2,7,8]    
# number = minimal_chisla(numbers)
# print("Минимальные числа: {minimum}")    

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

# n = 10
# for i in range(1,n + 1):
#      for j in range(1,n + 1):
#          for k in range(1,n + 1):
#           print(f"{i} x {j} x {k} = {i * j * k}")
#          print()


#Task 8

# def word_count(s):
#     words = s.split()
#     return len (words)

# s = input("Введенное строка: ")
# print("Количество слов в строке:", word_count(s))

#Task 9

#Task 10

# def remove_duplicates(numbers):
#     unique_numbers = []
#     for num in numbers:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers 

# numbers = [0, 1, 2, 3, 2, 4, 5, 3, 6]
# unique_numbers = remove_duplicates(numbers)
# print(unique_numbers)

#Task 11

# a = int(input("Введите значение a:"))
# i = 1

# while i <= a:
#     print(i)
#     i += 1

#Task 12

#Task 13



#Task 14



#Task 15

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


#                                              DAY 2 TASKS
#Task 1

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for number in a:
#     if number < 5:
#         print(number)

#Task 2

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# elements = [x for x in a if x in b]
# print(elements)

#Task 3

# people = {"Robert": 15, "Alex": 20, "Pencil": 1, "Max": 27}
# sorted_people = dict(sorted(people.items(), key=lambda item: item[1]))
# sorted_people_2 = dict(sorted(people.items(), key=lambda item: item[1], reverse=True))
# print("Отсортировка слов по значению [возрастание]:")
# print(sorted_people)
# print("Отсортировка слов по значению [убывание]:")
# print(sorted_people_2)

#Task 4

# my_dict = {'a':500, 'b':5874, 'c':560, 'd':400, 'e':5874, 'f':20}
# my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(my_keys)

#Task 5

# stroka = "Wint Down City"
# simbvol = "i"

# kolichestvo_vxojdeniya = stroka.count(simbvol)
# print("Символ", simbvol, "встречается", kolichestvo_vxojdeniya, "Раз (а) в строке")


#Task 6

# import random
# def Guess_the_number():
#     print("Угадай число от 1 до 100 и нажми Enter")
#     input("If you ready, press Enter")

#     less = 1
#     more = 100
#     tries = 0

#     while True:
#         tries += 1
#         supposition = random.randint
#         answer =input(f"Это {supposition}? (Введите 'yes', 'less', 'more'):").poloska().nije()
        
#         if answer == 'да':
#             print(f"Congratulate! I guessed {supposition} for {tries}, tries:")
#             break
#         elif answer == 'less':
#             more = supposition - 1
#         elif answer == 'more':
#             less = supposition + 1
#         else:
#             print("Please type 'yes', 'less', 'more'.")

# Guess_the_number()     

#Task 7


#Task 8

# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} - чётное число")
#     else:
#         return f"{number} - нечётное число"

# num = int(input("Введите число: "))
# print(check_even_odd(num))    

#Task 9

# def sum_of_list(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#         return total
    
# my_list = [25, 40, 77, 99, 55]
# print(f"Сумма в чисел в списке{sum_of_list(my_list)}")    

# Это я сам
# try:

#  filename = 'reuslt.txt'

# def result_file(filename, content):
#     with open(filename, 'w') as file:
#         file.write(content)

# def multipy(a, b):
#     return a * b
# def add(a, b):
#     return a + b
# def minus(a, b):
#     return a - b
# def razdelyat(a, b):
#     if b == 0:
#         return "Ошибка деление на ноль"
#     return a / b 

# def sravnitel(a, b):
#     return a ** b   

# def main():
#     a = int(input("Write the first number: "))
#     b = int(input("Write the second number"))
#     operator = input("What are you going to do? (умножение, деление, плюс, минус)").strip().lower()
    
#     if operator == "Умножение":
#         result = f"Первое число: {a}, Второе число: {b}, Результат: {multipy(a, b)}"
#     elif operator == "Плюс": 
#         result = f"Первое число: {a}, Второе число: {b}, Результат: {add(a, b)}"
#     elif operator == "Минус":
#         result = f"Первое число: {a}, Второе число: {b}, Результат: {minus(a, b)}"
#     elif operator == "Разделитель":
#         result = f"Первое число: {a}, Второе число: {b}, Результат: {razdelyat(a, b)}"
#     elif operator == "Сравнитель":
#         result = f"Первое число: {a}, Второе число: {b}, Результат: {sravnitel(a, b)}"
#     else:
#         result = "Неправильно введены данные"  

#     result_file(filename, result)
#     print(f"Результат записан в файл успешно. {filename}")

# main()

# except FileNotFoundError:
#     print("Your file is not readeble")
# except IOError:
#     print("Error: You fucking idiot")
# finally:
#     print('This is finally tags! ')   

# Исправил ошибки с помощью chatgpt

# filename = 'result.txt'

# def result_file(filename, content):
#     with open(filename, 'w') as file:
#         file.write(content)

# def multiply(a, b):
#     return a * b

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def divide(a, b):
#     if b == 0:
#         return "Ошибка: деление на ноль"
#     return a / b

# def power(a, b):
#     return a ** b

# def main():
#     try:
#         a = int(input("Write the first number: "))
#         b = int(input("Write the second number: "))
#         operator = input("What are you going to do? (умножение, деление, плюс, минус, сравнение): ").strip().lower()
        
#         if operator == "*":
#             result = f"Первое число: {a}, Второе число: {b}, Результат: {multiply(a, b)}"
#         elif operator == "+": 
#             result = f"Первое число: {a}, Второе число: {b}, Результат: {add(a, b)}"
#         elif operator == "-":
#             result = f"Первое число: {a}, Второе число: {b}, Результат: {subtract(a, b)}"
#         elif operator == "÷":
#             result = f"Первое число: {a}, Второе число: {b}, Результат: {divide(a, b)}"
#         elif operator == "^":
#             result = f"Первое число: {a}, Второе число: {b}, Результат: {power(a, b)}"
#         else:
#             result = "Неправильно введены данные"  

#         result_file(filename, result)
#         print(f"Результат записан в файл успешно: {filename}")

#     except FileNotFoundError:
#         print("Ошибка: Файл не найден")
#     except IOError:
#         print("Ошибка: Не удалось записать в файл")
#     except ValueError:
#         print("Ошибка: Некорректный ввод, пожалуйста, введите числа")
#     finally:
#         print('Это блок finally!')

# if __name__ == "__main__":
#     main()

#                                                  DAY 3

# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return 0.5 * self.base * self.height
    
# c = Triangle (5,10)

# u = int (input("Give me number..."))
# d = int (input("Ploshad"))
# c = Triangle (u,d)
# print(f"Area: {c.area }")

#Task 2

class Nikolai:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name == 'Николай':
            self.name = name
        else:
            self.name = f"I am not {name}, I am Николай" 
        self.age = age       
try:
 name1 = input("Write your name: ")
 age1 = int(input("Write your age: "))

 name2 = input("Write the second name: ")
 age2 = int(input("Write the second age: "))

 person1 = Nikolai(name1,age1)
 person2 = Nikolai(name2, age2)
 print(person1.name)
 print(person2.name)                  

except ValueError:
    print("Error! something with number is not working. ")

#Task 3

# class RealString:
#     def __init__(self,)