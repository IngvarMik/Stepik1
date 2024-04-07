"""Программа получает на вход строку. Ваша задача вывести все символы этой строки, которые имеют нечетные индексы
Sample Input:
Donald Trump
Sample Output:
oadTup"""
s = str(input())
print(s[1::2])

"""Программа получает на вход строку. Ваша задача развернуть строку и вывести ее на экран.
Sample Input:
leetcode.com
Sample Output:
moc.edocteel"""

s = str(input())
print(s[::-1])

"""Программа получает на вход строку.
Выведите каждый третий символ строки в обратном порядке, начиная с последнего.
Sample Input:
The Big Bang Theory
Sample Output:
ye ag T"""
print(input()[::-3])

"""Программа получает на вход одно слово. Ваша задача перенести последнюю букву в начало,
 тем самым сдвинуть все остальные буквы вправо на один разряд.
   В качестве ответа нужно вывести полученное слово
Sample Input 1:
become
Sample Output 1:
ebecom"""
s = str(input())
res = s[-1]+s[0:-1]
print(res)