"""Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
Ваша задача заменить все пробелы запятыми и вывести полученную строку.
Sample Input 1:
Smells Like Teen Spirit
Sample Output 1:
Smells,Like,Teen,Spirit"""
print(input().replace(' ',','))

"""На вход программе поступает строка, ваша задача удалить из нее все символы w и z.
Учитываем только маленькие буквы
Sample Input:
what's up?
Sample Output:
hat's up?"""
print(input().replace('w','').replace('z',''))

