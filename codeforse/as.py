
with open('lepus.in') as lep:
	n, lst = lep.read().split('\n')

l = '.....'
c = l+lst
n = int(n)
a = [-1 for i in range(n+5)]
a[5] = 0
for i in range(5, n+5):

	if c[i] =="w":
		continue
	elif c[i] == '"':
		a[i]=1
	elif c[i]==".":
		a[i]=0
for i in range(5, n+5):
	m = (max(a[i-1], a[i-3], a[i-5]))
	if a[i]==-1:
		continue
	if a[i] == 1:
		a[i] = a[i]+m
b = a[:]
for i in range(5, n+5):
	b[i] = max(max(a[i-1], a[i-3]), a[i-5])
with open('lepus.out', mode='wt') as o:
	print(b[-1], file=o)
print(b[-1])
