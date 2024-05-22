l = [11,12,45,1,2,3,1]
print(l)
l.sort(reverse=True)
print(l)
print(l.index(1))
print(l.count(3))

m = l.copy()
m[0] = 0
print(m)
print(l)

l.insert(1,899)
print(l)
p = [5,6,7,8]
k = l+m
l.extend(m)
print(l)