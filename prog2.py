# Everything in Python is Object as Default

a = complex(8,2)
print(a)
b = "Harry"
print(b)
c = True
print(c+a)
d = None
print(d)
print("Type of a is ",type(a))
print("Type of b is ",type(b))
print("Type of c is ",type(c))
print("Type of d is ",type(d))

list_a = [8,2.5,complex(1,2),"good",True]
print(list_a) # Mutable
tuple_a = [8,2.5,complex(1,2),"good",True]
print(tuple_a) # Immutable
map_a = {"good":"boy","bad":"boy","age":20,"canVote":True}
print(map_a)