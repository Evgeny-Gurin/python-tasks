'''
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля
выводит сумму полученных на вход чисел.
'''

num = int(input())
sum = num
while num != 0:
  num = int(input())
  sum += num

print(sum)