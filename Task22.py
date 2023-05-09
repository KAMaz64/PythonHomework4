# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

N = int(input('введите кол-во элементов 1-го массива: '))
array_A_input = input(f'Введите через пробел {N} элементов массива A[1..N]: ').split()
array_A = list(map(int, array_A_input))

M = int(input('введите кол-во элементов 2-го массива: '))
array_B_input = input(f'Введите через пробел {M} элементов массива B[1..M]: ').split()
array_B = list(map(int, array_B_input))


array_C = set(array_A).intersection(set(array_B))

array_D = list(array_C)

temp = 0
for i in range(0, len(array_D)):
    for j in range(i+1, len(array_D)):
        if array_D[i] > array_D[j]:
            temp = array_D[i]
            array_D[i] = array_D[j]
            array_D[j] = temp

print(array_D)