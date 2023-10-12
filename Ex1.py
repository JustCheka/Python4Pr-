""" 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо


mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

"""



var1 = '3 4'
var2 = '1 2 3'
var3 = '1 2 3 4'


var2 = var2.split()
var3 = var3.split()

var2 = set(var2)
var3 = set(var3)

answer = var2.intersection(var3)
answer = list(answer)
answer.sort()

for item in answer:
    print (item, end = " ")