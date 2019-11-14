"""
__________________________|Ограничения________________________
Полученный результат<----[              ]<----На входе
                         ^|-Инструмент
"""
from pprint import pprint

"""
_________________________Clamping____
матрица переходов <--[ ]<-- file = Number(parent) Number(children)
    |^- упаковка в список 
                        -> [['5'], ['0 1'], ['1 2','_', '1 2'], ['1 3', '1 3', '1 4'], ['2 3'], ['3 0'], ['4 0', '4 2']]
    |- раскидать в матрицу 
    |- посчитать вероятностную матрицу 90/10
"""
import re
import sys

small_obj = [line.strip().split("  ") for line in sys.stdin.read().split('\n')]
n = int(small_obj[0][0])
matrix_link = [[0]*n for _ in range(n)]
count_link =[0 for _ in range(n)]
for line in small_obj[1:]:
    for l in line:
        i, j = map(int, l.split())
        matrix_link[i][j] += 1
        count_link[i] += 1

sys.stdout.write(str(n)+" "+str(n)+"\n")

for i in range(n):
    for j in range(n):
        p = (.90 * matrix_link[i][j]/count_link[i]) + (.10/n)
        sys.stdout.write(str(round(p, 8))+' ')
    print()
