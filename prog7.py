# Strings are Immutable in Python

a = "!!Harry!!! !! Harry !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))
print(a.count("Harry"))
print(a.endswith("!!!"))

blogHead = "introduction to JS"
print(blogHead.capitalize())

str = "Welcome to the Console ... "
print(str.center(50))
print(len(str))
print(len(str.center(50)))

x = "He's Name is Dan. He is a Honest Man"
print(x.find("is"))
print(x.find("iseei"))
print(x.index("is"))
# print(x.index("iseei"))
print(x.isalpha())
print(x.isalnum())
print(x.isspace())
y = " "
print(y.isspace())

z = "Pikachu"
print(z.istitle())
print(z.swapcase())