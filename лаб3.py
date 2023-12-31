# 1. Четные числа (пока). Напишите программу,
# которая будет печатать все четные числа от 1 до N, где N - положительное целое число,
# введенное пользователем. Используйте цикл while.
N = int(input("Enter a positive integer (N): "))
num = 1

while num <= N:
    if num % 2 == 0:
        print(num)
    num += 1


# 2. Факториал (While). Напишите программу для вычисления факториала числа N,
# где N - положительное целое число,
# введенное пользователем. Используйте цикл while.

N = int(input("Enter a positive integer (N): "))

if N < 0:
    print("Factorial is not defined for negative numbers.")
elif N == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    i = 1

    while i <= N:
        factorial *= i
        i += 1

    print(factorial)

# 3. Поиск по номеру (перерыв). Напишите программу,
# //            которая попросит пользователя ввести цифры с клавиатуры, отыщет число 42 и,
# //            если оно введено, завершит работу программы, используя конструкцию break.

while True:
    n= int(input("Enter a number: "))
    if n == 42:
        print("Number 42 is entered.!")
        break

# /        4. Подсчет символов (строковые операции).
# //        Попросите пользователя ввести строку.
# //        Затем подсчитайте и выведите количество букв "а" в этой строке.

str = input("Enter a string: ")
count = str.count("a")

print(count)

# 5. Сумма цифр числа (строковые операции).
# //                Попросите пользователя ввести число, затем найдите и выведите сумму его цифр.

num = input("Enter a number: ")
total = 0

for char in num:
    if char.isdigit():
        total += int(char) 
print(total)

# //        6. Числа Фибоначчи (пока). Напишите программу для печати первых N чисел Фибоначчи,
# //                где N - положительное целое число, введенное пользователем. Используйте цикл while.

N = int(input("Enter a positive integer (N): "))
a, b = 0, 1
count = 0

while count < N:
    print(a, end=" ")  
    a, b = b, a + b 
    count += 1 
print() 


# 7. Переверните строку (операции со строками). Попросите пользователя ввести str.
# //        вводим, а затем выводим его в обратном порядке.

string = input("Enter a string: ")
reversed_string = string[::-1]  
print("Reversed string:", reversed_string)

# //        8. Пропустите четные (продолжайте).
# //                Напишите программу, которая предложит пользователю ввести цифры, и если введенное число четное,
# //        оно будет пропущено с помощью конструкции continue. Программа должна вывести сумму всех нечетных чисел.

sum= 0

while True:
    num = input("Enter a number (or 'stop' to quit): ")
    
    if num == 'stop':
        break

    num = int(num)
    
    if num % 2 == 0:  
        continue  
    
    sum+= num

print("Sum of odd numbers:", sum)


# 9. Угадайте число (перерыв). Напишите игру, в которой компьютер выбирает случайное число от 1 до 100,
# //            а пользователь должен угадать это число.
# //                Программа должна отображать подсказки ("Слишком маленький" или "Слишком большой") и завершать работу,
# //                когда пользователь угадает число. Используйте конструкцию break, чтобы завершить игру.

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too small.")
    else:
        print("Too large.")


# //        10. Палиндром (строковые операции). Попросите пользователя ввести строку и определить,
# //                является ли она палиндромом (читайте то же самое справа налево, что и слева направо).

string = input("Enter a string: ")
reversed_string = string[::-1]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# //        11. Пронумеруйте до степени (пока). Напишите программу,
# //            которая предлагает пользователю ввести число X и степень Y.
# //        Затем вычислите и выведите X в степени Y, используя цикл while.

x = float(input("Enter a number (X): "))
y = int(input("Enter the power (Y): "))

result = 1
count = 0

while count < y:
    result *= x
    count += 1

print(f"{x} to the power of {y} is: {result}")


# 12. Подсчет простых чисел (While, Break).
# Напишите программу, которая найдет и напечатает все простые числа в диапазоне от 1 до N,
# //        где N - положительное целое число, введенное пользователем.
# Используйте цикл while и конструкцию break для оптимизации процесса.



# 13. Обратное число (строковые операции). Попросите пользователя ввести номер и напечатать его в обратном порядке.
number = input("Введите число: ")
reversed_number = number[::-1]
print("Число в обратном порядке:", reversed_number)



# //        14. Проверьте на первичность (продолжайте).
# //                Напишите программу, которая проверяет, является ли число,
# //        введенное пользователем, простым числом. Если число не является простым,
# //                программа должна напечатать следующее простое число и продолжить тестирование. Используйте конструкцию continue.


# //        15. Шифр Цезаря (строковые операции).
# //        Попросите пользователя ввести строку и сдвинуть все буквы в строке на N позиций вперед по алфавиту (циклически),
# //                где N - целое число, введенное пользователем. Выведите зашифрованную строку.
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
