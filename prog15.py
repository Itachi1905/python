marks = [1,2,3,"good",True]
print(marks)
print(marks[:])
print(marks[-3])
print(marks[len(marks)-3])
print(marks[1:8:2])
# Negative Index will get converter to Posistive Indexing

if 7 in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry" :
    print("Yes")
else: print("No")

lst = [i for i in range(4)]
print(lst)
pi = [i*i for i in range(20) if i%2==0 ]
print(pi)