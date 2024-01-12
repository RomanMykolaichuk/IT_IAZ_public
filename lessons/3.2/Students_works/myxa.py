# звіт про виконане завдання

# Вивести на екран привітання "Hello, world!"
print("Hello, world!")

# Завдання 2. Обчислити суму двох чисел і вивести результат.
# Запитуємо користувача про два числа
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
# Обчислюємо суму
sum_result = num1 + num2
# Виводим результат
print("Сума двох чисел:", sum_result)

# Завдання 3. Обчислити площу прямокутника за заданими сторонами.
# Введимо значення двох сторін прямокутника 
length = float(input("Введіть розмір довжини прямокутника: "))
width = float(input("Введіть розмір ширини прямокутника: "))
# Обчислюємо суму
area = length * width
area1 = round(area, 3)
# Виводим результат
print("Площа прямокутника:", area1)

# Завдання 4. Вивести на екран таблицю множення на 7.
# Записуєм алгоритм розрухунку
for i in range(1, 10):
    result = 7 * i
# Виводим результат
    print("7 *", i, "=", result)

# Завдання 5. Знайти найбільший спільний дільник двох чисел.
# Записуєм алгоритм розрухунку
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# Вводим два числа
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
# Пошук найбільшого спільного дільника
result = gcd(num1, num2)
# Виводим результат
print("Найбільший спільний дільник:", result)

# Завдання 6. Перевести температуру з Цельсія в Фаренгейти.
# Вводим температуру в градусах Цельсій
celsius = float(input("Введіть температуру в градусах Цельсія: "))
# Конвертуємо значення температури в градусах Фаренгейта
fahrenheit = (celsius * 9/5) + 32
# Виводим результат
print("Температура в градусах Фаренгейта:", fahrenheit)

# Завдання 7. Порахувати факторіал заданого числа.
# Опис функції для розрахунку факторіала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Введення числа 
num = int(input("Введіть число: "))
# Розрахунок факторіала
result = factorial(num)
# Виводим результат
print("Факторіал числа", num, "дорівнює", result)

# Завдання 8. Порахувати факторіал заданого числа.
# Створюємо список чисел від 1 до 20
numbers = list(range(1, 21))
# Виводим список
print("Початковий список чисел:", numbers)
# Фільтр парних чисел зі списку
even_numbers = [num for num in numbers if num % 2 == 0]
# Виводим список парних чисел
print("Парні числа:", even_numbers)

# Завдання 9. Обчислити суму чисел Фібоначчі до заданого числа.
def fibonacci_sum(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return sum(fib_sequence)

# Задане число, до якого обчислюємо суму
num = int(input("Введіть число: "))
result = fibonacci_sum(num)
print(f"Сума чисел Фібоначчі до {num} дорівнює {result}")

# Завдання 10. Порахувати кількість голосних літер у заданому рядку.
def count_vowels(string):
    vowels = "aeiouAEIOU"  # список голосних літер
    vowel_count = 0  # лічильник голосних літер
    
    for char in string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Заданий рядок, в якому ми будемо рахувати голосні літери
input_string = input("Введіть рядок: ")
vowel_count = count_vowels(input_string)
print(f"Кількість голосних літер у рядку: {vowel_count}")

# Завдання 11. Визначити, чи є задане слово паліндромом.
def is_palindrome(word):
    word = word.lower()  # Перетворюємо слово в нижній регістр для порівняння
    reversed_word = word[::-1]  # Реверсуємо слово

    return word == reversed_word

# Задане слово, яке ми будемо перевіряти
input_word = input("Введіть слово: ")
if is_palindrome(input_word):
    print(f"{input_word} є паліндромом.")
else:
    print(f"{input_word} не є паліндромом.")



# Завдання 12. Знайти всі прості числа у заданому діапазоні.
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Заданий діапазон, в якому ми будемо шукати прості числа
start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

prime_numbers = find_primes_in_range(start_range, end_range)
print(f"Прості числа в діапазоні від {start_range} до {end_range}: {prime_numbers}")

# Завдання 13. Розрахувати квадратне рівняння.
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Розв'язків немає
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]

# Введення коефіцієнтів квадратного рівняння
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

solutions = solve_quadratic(a, b, c)
if solutions is None:
    print("Рівняння не має розв'язків.")
elif len(solutions) == 1:
    print(f"Рівняння має один розв'язок: x = {solutions[0]}")
else:
    print(f"Рівняння має два розв'язки: x1 = {solutions[0]}, x2 = {solutions[1]}")


# Завдання 14. Порахувати суму цифр заданого числа.
def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    return total_sum

# Задане число, суму цифр якого ми будемо рахувати
input_number = int(input("Введіть число: "))
result = sum_of_digits(input_number)
print(f"Сума цифр числа {input_number} дорівнює {result}")


# Завдання 15. Вивести всі парні та непарні числа від 1 до 50 окремо.
def separate_even_odd_numbers(start, end):
    even_numbers = []
    odd_numbers = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

start_range = 1
end_range = 50

even_nums, odd_nums = separate_even_odd_numbers(start_range, end_range)

print("Парні числа:")
print(even_nums)

print("Непарні числа:")
print(odd_nums)


# Завдання 16. Знайти максимальний елемент у списку.
def find_max_element(lst):
    max_element = lst[0]  # Припускаємо, що перший елемент найбільший

    for element in lst:
        if element > max_element:
            max_element = element

    return max_element

# Заданий список, в якому ми будемо шукати максимальний елемент
input_list = [int(x) for x in input("Введіть список чисел через пробіл: ").split()]
max_num = find_max_element(input_list)
print(f"Максимальний елемент у списку: {max_num}")


# Завдання 17. Видалити дублікати зі списку.
def remove_duplicates(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Заданий список, з якого ми будемо видаляти дублікати
input_list = [int(x) for x in input("Введіть список чисел через пробіл: ").split()]
unique_numbers = remove_duplicates(input_list)
print(f"Список без дублікатів: {unique_numbers}")

# Завдання 18. Знайти довжину строки.
def find_string_length(string):
    length = len(string)
    return length

# Заданий рядок, для якого ми будемо знаходити довжину
input_string = input("Введіть рядок: ")
length = find_string_length(input_string)
print(f"Довжина рядка: {length}")


# Завдання 19. Вивести заданий рядок у зворотньому порядку.
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

# Заданий рядок, який ми будемо виводити у зворотньому порядку
input_string = input("Введіть рядок: ")
reversed_result = reverse_string(input_string)
print(f"Рядок у зворотньому порядку: {reversed_result}")

# Завдання 20. Згенерувати список квадратів чисел від 1 до 10.
def generate_square_list(start, end):
    square_list = [num ** 2 for num in range(start, end + 1)]
    return square_list

start_range = 1
end_range = 10

squares = generate_square_list(start_range, end_range)
print(f"Список квадратів чисел від {start_range} до {end_range}: {squares}")

# Завдання 21. Обчислити суму чисел, які діляться на 3 або 5 у діапазоні від 1 до 100.
total_sum = sum(num for num in range(1, 101) if num % 3 == 0 or num % 5 == 0)
print(f"Сума чисел, які діляться на 3 або 5 у діапазоні від 1 до 100: {total_sum}")

# Завдання 22. Визначити, чи є задане число простим.
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Задане число, яке ми будемо перевіряти
input_number = int(input("Введіть число: "))
if is_prime(input_number):
    print(f"{input_number} є простим числом.")
else:
    print(f"{input_number} не є простим числом.")

    
# Завдання 23. Перевести десяткове число у двійкову та шістнадцяткову системи числення.
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)[2:]  # Видаляємо префікс "0b"
    return binary_num

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = hex(decimal_num)[2:]  # Видаляємо префікс "0x"
    return hexadecimal_num

# Задане десяткове число, яке ми будемо переводити
input_decimal = int(input("Введіть десяткове число: "))

binary_result = decimal_to_binary(input_decimal)
hexadecimal_result = decimal_to_hexadecimal(input_decimal)

print(f"Двійкове представлення числа {input_decimal}: {binary_result}")
print(f"Шістнадцяткове представлення числа {input_decimal}: {hexadecimal_result}")

# Завдання 24. Вивести всі букви алфавіту разом із їхніми порядковими номерами.
for i in range(26):
    letter = chr(ord('a') + i)  # Перетворюємо числовий індекс на букву
    print(f"{i+1}: {letter}")


# Завдання 25. Порахувати суму цифр у заданому числі без використання рядкового представлення.
def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        total_sum += digit
        number //= 10
    return total_sum

# Задане число, суму цифр якого ми будемо рахувати
input_number = int(input("Введіть число: "))
result = sum_of_digits(input_number)
print(f"Сума цифр числа {input_number} дорівнює {result}")


# Завдання 26. Знайти середнє арифметичне елементів списку.
def calculate_average(lst):
    if not lst:
        return 0  # Якщо список порожній, повертаємо 0

    total_sum = sum(lst)
    average = total_sum / len(lst)
    return average

# Заданий список чисел, для якого ми будемо знаходити середнє арифметичне
input_list = [float(x) for x in input("Введіть список чисел через пробіл: ").split()]
average_result = calculate_average(input_list)
print(f"Середнє арифметичне елементів списку: {average_result}")

# Завдання 27. Перевірити, чи є задане число паліндромом.
def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number

# Задане число, яке ми будемо перевіряти
input_number = int(input("Введіть число: "))
if is_palindrome(input_number):
    print(f"{input_number} є паліндромом.")
else:
    print(f"{input_number} не є паліндромом.")
    

# Завдання 28. Замінити всі входження заданої літери у рядку іншою літерою.
def replace_letter(input_string, old_letter, new_letter):
    replaced_string = input_string.replace(old_letter, new_letter)
    return replaced_string

# Заданий рядок, у якому будемо замінювати літери
input_string = input("Введіть рядок: ")
old_char = input("Введіть літеру, яку потрібно замінити: ")
new_char = input("Введіть літеру, на яку потрібно замінити: ")

result = replace_letter(input_string, old_char, new_char)
print(f"Результат заміни: {result}")


# Завдання 29. Визначити, чи є заданий рядок анаграмою іншого рядка.
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

# Задані рядки, які ми будемо порівнювати
input_str1 = input("Введіть перший рядок: ")
input_str2 = input("Введіть другий рядок: ")

if is_anagram(input_str1, input_str2):
    print("Ці рядки є анаграмами.")
else:
    print("Ці рядки не є анаграмами.")
    
# Завдання 30. Знайти найбільший спільний дільник списку чисел.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_list(numbers):
    if not numbers:
        return None
    
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
    
    return current_gcd

# Заданий список чисел, для якого ми будемо знаходити НСД
input_list = [int(x) for x in input("Введіть список чисел через пробіл: ").split()]
result = find_gcd_of_list(input_list)

if result is None:
    print("Список чисел порожній, немає НСД.")
else:
    print(f"Найбільший спільний дільник чисел: {result}")