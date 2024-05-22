s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities1 = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
print(cities1.intersection(cities2))
print(cities1.symmetric_difference(cities2))
print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2))
print(cities1.issubset(cities2))
print(cities1.remove("Tokyo"))
# Remove generates Error when element is not present
print(cities1.discard("Tokyo"))
print(cities1)
print(cities2.pop())
# Symmetric Difference means Disjoint of a Set