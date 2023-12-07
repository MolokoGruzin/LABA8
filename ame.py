from random import *

N = randint(4, 31)

#privet
def ai(n):
if (n < 5) and (n > 1):
x = n - 1
print("\nКомпьютер взял ", x, " камней")
print("\nКомпьютер победил!")
exit()
else:
x = randint(1, 3)
return x


a = 0

while N > 1:
print("\n\nВ куче ", N, " камней")
print("Выберите дествие:\nВзять 1 камень Взять 2 камня Взять 3 камня\n 1 2 3\n")
try:
a = int(input())
if a < 1 or a > 3:
print("\nВведено неверное значение")
exit()
except ValueError:
print("\nВведено неверное значение")
exit()
N = N - a
print("\n\nВ куче ", N, " камней")
if N < 2:
break
a = ai(N)
N = N - a
print("\nКомпьютер взял ", a, " камней")
print("\nВы победили!")