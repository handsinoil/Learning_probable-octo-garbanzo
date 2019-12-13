#!/usr/bin/env python3
# coding=utf-8
"""___Clamping___
1. Обработать входные данные
1.1 написать функцию для считывания кол-ва ввода строк

1.2 преобразовать сырые данные в рабочий вид
    1.2.1  считать информацию наследования в промежуточный удобный вид типо словаря
    1.2.2 обработать входные данные запроса пути от предка до потомка
        писать функцию считывания запросов в виде списка

2. найти путь от предка до потомка если он есть
	написать функцию котора находит путь

3. вывести результат проверки
циклом пробежать по запросам и выдать ответ да или нет
"""


def print_info(o, s_o):
	print(s_o, id(o))

	print(o)
	print('_____')


# 1.1
import sys


def read_n():
	return int(sys.stdin.readline())


# 1.2.1

def read_inheritance(n):
	reader = (tuple(map(str.strip, line.split(":"))) for line in sys.stdin)
	print_info(reader, 'reader')
	inheritance = {}
	for i in range(n):
		key, *val = next(reader)
		if len(val) != 0:
			val = val.pop().split()
		inheritance[key] = val
	print_info(inheritance, 'inheritance')
	return inheritance


# 1.2.2

def read_queries(q):
	reader = [line.split() for line in sys.stdin]
	print_info(reader, 'reader')
	queries = list(reader)
	print_info(queries, 'queries')
	return queries

# 2.

def is_parent(tree, chi, par, path=[]):
	path = path + [chi]
	print_info(path, 'path')

	if chi not in tree:
		return None
	if chi == par:
		return path

	for c in tree[chi]:
		if c not in path:
			newpath = is_parent(tree, c, par, path)

			if newpath:
				return newpath

	return None

# 3

n = read_n()
classes = read_inheritance(n)
q = read_n()
queries = read_queries(q)

for q in queries:
	parent, child = q
	if is_parent(classes, child, parent):
		print("Yes")
	else:
		print("No")
