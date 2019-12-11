"""
________________________|Clamping_____
dict{Child:[parent], }<--[]<--stdin(input_data.txt)
^| - обработать вх. данные
 | - структурa наследования <-[]<-list date
                             ^| - split generator
                              | - stacker
                              | - create structure
 | - проверить наследование
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
		if len(i) == 1:
			struct[i[0]] = i
		elif len(i)>1:
			if i[0] in struct:
				struct[i[0]].extend(i[1].split(' '))
			else:
				struct[i[0]] = i[1].split(' ')

def create_struct(n_lst, f1, f2):
	struct = dict()
	gen = split_gen(n_lst)
	stacker(gen, struct)
	return struct

def split_q(struc, q_lst):
	#
	for i in q_lst:
		q_i = i.strip().split(" ")
		if len(q_i)==1:
			yield 0, 0
		parent, child = q_i
		if child and parent in struc:
			yield parent, child
		else:
			yield 0, 0

def rec(d, par, chi):
	if par in d[chi]:
		return "Yes"
	elif chi in d[chi]:
		return  "No"
	elif chi not in d[chi] and par not in d[chi]:
		for i in d[chi]:
			return rec(d, par, i)

def check(struc, q_lst, split_q, rec):
	#
	for _ in split_q(struc, q_lst):
		parent, child = _
		if parent != 0:
			ansver = rec(struc, parent, child)
		else:
			ansver = "No"
		print(ansver)

def print_info(o, s_o):
	print(s_o, id(o))

	print(o)
	print('_____')

import sys
s = sys.stdin.readlines()
n_lst, q_lst = treatment(s)
struc = create_struct(n_lst, split_gen, stacker)

print_info(n_lst, 'n_lst')
print_info(q_lst, 'q_lst')
print_info(struc, 'struct')

check(struc, q_lst, split_q, rec)
