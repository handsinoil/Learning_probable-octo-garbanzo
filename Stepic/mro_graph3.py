# input() = .readline() для стандарного входа
# n = int(input())
# struct_parents= {}

def print_info(o, s_o):
	print(s_o, id(o))
	print(o)
	print('_____')
#
# for _ in range(n):
# 	a = input().split()
# 	struct_parents[a[0]] = [] if len(a) == 1 else a[2:]
# print_info(struct_parents, 'struct_parents')
#
# def child_parent(chi, par):
#
# 	return chi == par or any(map(lambda p: child_parent(p, par), struct_parents[chi]))
#
# q = int(input())
# for _ in range(q):
# 	a, b = input().split()
# 	print("Yes" if child_parent(b, a) else "No")
#####################
# def foo(a, b):
# 	tmp = a == b
# 	for i in d[b]:
# 		tmp |= foo(a, i)
# 	return tmp
#
# d = {}
#
# for i in range(int(input())):
# 	s = input().split()
# 	d[s[0]] = ([] if len(s) == 1 else s[2:])
#
# for i in range(int(input())):
# 	a, b = map(str, input().split())
# 	print("Yes" if foo(a, b) else "No")
####################
# inheritance = dict()
#
# for i in [input().split() for _ in range(int(input()))]:
# 	inheritance[i[0]] = i[2:]
# print_info(inheritance, 'inheritance')
#
# for k, v in inheritance.items():
# 	for i in v:
# 		if i in inheritance:
# 			inheritance[k].extend(inheritance[i])
# print_info(inheritance, 'inheritance')
# m = [input().split() for _ in range(int(input()))]
# print_info(m, 'm')
#
# for parent, inheritor in m:
# 	print(['No', 'Yes'][parent == inheritor or parent in inheritance[inheritor]])
####################

# a, b =([input().split() for i in range(int(input()))] for i in range(2))
# print_info(a, "a")
# print_info(b, "b")
#
# d = {i[0]: i[2:] for i in a}
#
# print_info(d, 'd')
#
# def f(par, chld):
# 	if chld not in d.keys(): return 0
# 	elif par == chld: return 1
# 	for i in d[chld]:
# 		r = f(par, i)
# 		if r: return r
# x= f("a", "g")
# print(x)
# #[print('Yes') if f(i[0], i[1]) is 1 else print('No') for i in b]

###################
a, b =([input().split() for i in range(int(input()))] for i in range(2))
d = {i[0]: i[2:] for i in a}

def child_parent(chi, par):
	return chi == par or any(map(lambda p: child_parent(p, par), d[chi]))

[print('Yes') if child_parent(i[1], i[0]) == 1 else print('No') for i in b]

##################