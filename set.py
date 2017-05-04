def union(a,b):
	u = [j for j in b if j not in a]
	return a + u

def intersection(a,b):
	ine = [i for i in b if i in a]
 	return ine

def setdifference(a,b):
	d = [i for i in a if i not in b]
	return d

def symdifference(a,b):
	return setdifference(union(a,b),intersection(a,b))
	#return setdifference(a,b) + setdifference(b,a) works too

def cproduct(a,b):
	p = [(i,j) for i in a for j in b]
	return p

a = [1,10,100]
b = [2,20,200]
print union(a,b)
print intersection(a,b)

print setdifference(a,b)
print setdifference(b,a)

print symdifference(a,b)
print cproduct(a,b)
