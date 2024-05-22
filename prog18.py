countries = ("india","china","russia","japan")
temp = list(countries)
temp.append("USA")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
print(temp)

tuple1 = (1,2,3,4,5,1,2)
tup = tuple1 + countries
print(tup)
# res = tuple1.index(3)
# res = tuple1.count(1)
# res = tuple1.index(3,4,8)
res = len(tuple1)
print('Count of 3 in Tuple is : ',res)