"""
________________________|Clamping_____
dict{Parent:{children, }<--[]<--stdin(input_data.txt)
^| - обработать вх. данные
 | - создать структуру наследования
 | - добавить туда связи
 | - проверить наследование
"""

import sys
s = sys.stdin.readlines()

def treatment(s: list) -> tuple:
	"""processing in std"""
	n = int(s[0])
	nlst = [i.strip('\r\n') for i in s[1:n + 1]]
	q = int(s[n + 1].strip('\r\n'))
	qlst = [i.strip('\r\n') for i in s[n + 2:n + q + 2]]
	return nlst, qlst
n_lst, q_lst = treatment(s)

struct_graf = dict()
pre_struct = dict()

def create_struct(nlst):
	global struct_graf
	global pre_struct
	for i in nlst:
		d = i.split(' : ')
		if len(d) > 1:
			d_0 = d[0].strip()
			d_1 = d[1].strip().split(" ")
			pre_struct[d_0] = d_1
			struct_graf[d_0] = d_1

create_struct(n_lst)

def add_struct():
	global pre_struct
	global struct_graf
	for k, v in pre_struct.items():
		for i in v:
			if i in struct_graf.keys():
				struct_graf[k]= pre_struct[k] + pre_struct[i]

add_struct()

def check_inheritance(q_lst):
	global struct_graf
	for i in q_lst:
		d = i.strip().split(" ")
		if d[0] == d[1]:
			print("Yes")
		if d[1] in struct_graf.keys():
			if d[0] in struct_graf[d[1]]:
				print("Yes")
			else: print("No")
		else: print("No")

def print_info(o, s_o):
	print(s_o, id(o))
	print('_____')
	print(o)
	print('_____')
print_info(n_lst, 'n_lst')
print_info(pre_struct, 'pre_struct')
print_info(struct_graf, 'struct_graf')
print_info(q_lst, 'q_lst')
check_inheritance(q_lst)