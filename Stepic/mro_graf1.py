"""
________________________|Clamping_____
dict{Child:[parent], }<--[]<--stdin(input_data.txt)
^| - обработать вх. данные
 | - структурa наследования <-[]<-list date
                             ^| - split generator
                              | - stacker
                              | - create structure
 | - найти путь от реб к род
 | - вывести результат проверки
"""
def treatment(s: list) -> tuple:
	"""processing in std"""
	n = int(s[0])
	nlst = [i.strip('\r\n') for i in s[1:n + 1]]
	q = int(s[n + 1].strip('\r\n'))
	qlst = [i.strip('\r\n') for i in s[n + 2:n + q + 2]]
	return nlst, qlst

def split_gen(n_lst):
	for i in n_lst:
		yield i.strip().split(" : ")

def stacker(f1, struct):

	for i in f1:
		if len(i)>1:
			if i[0] in struct:
				struct[i[0]].extend(i[1].split(' '))
			else:
				struct[i[0]] = i[1].split(' ')

def create_struct(n_lst, f1, f2):
	struct = dict()
	gen = split_gen(n_lst)
	stacker(gen, struct)
	return struct



def print_info(o, s_o):
	print(s_o, id(o))

	print(o)
	print('_____')

def find_path(graph, chi, par, path=[]):
	path = path + [chi]
	if chi == par:
		return path
	if chi not in graph:
		return None
	for node in graph[chi]:
		if node not in path:
			newpath = find_path(graph, node, par, path)
			if newpath: return newpath


import sys
s = sys.stdin.readlines()
n_lst, q_lst = treatment(s)
struc = create_struct(n_lst, split_gen, stacker)
for i in q_lst:
	parent, child = i.split(" ")
	if parent == child:
		print("Yes")
	else:
		ansver = find_path(struc, child, parent)
		if ansver == None:
			print("No")
		else:
			print("Yes")





