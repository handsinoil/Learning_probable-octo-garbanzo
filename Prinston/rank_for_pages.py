"""
__________________________|Clamping_____
        Ранги pages<----[           ]<---- Матрица с вероятностью посещения страницы, n = общее кол-во переходов
                         ^|- Считать матрицу
                          |- Создать интервал вероятностей, выдать номер страницы и посчитать кол-во переходов на стр
                          |- Вычислить и вывести ранг страницы
"""
import random
import sys
# кол-во переходов
moves = int(sys.argv[1])
matrix = [_.strip() for _ in sys.stdin.read().split('\n')]
n = int(matrix[0][0])
matrix = matrix[1:len(matrix)-1]
# ['0.02 0.92 0.02 0.02 0.02 ', '0.02 0.02 0.38 0.38 0.2 ', '0.02 0.02 0.02 0.92 0.02 ', '0.92 0.02 0.02 0.02 0.02 ',
# '0.47 0.02 0.47 0.02 0.02 '] 5

p = [_.split() for _ in matrix]
hits = [0]*n
page = 0 # beginity page
for i in range(moves):
    r = random.random()
    total = 0.0
    for j in range(0, n):
        total += float(p[page][j])
        if r < total:
            page = j
            break
    hits[page] += 1
rank = [k/moves for k in hits]
for m in rank: print('{:<8.5f}'.format(m), end='')
