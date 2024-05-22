# Default Arguments
def average(a=1,b=3):
    print("The Average is = ", (a+b)/2)

average()
average(4,6)
average(b=10)

def avg(*numbers):
    sum = 0
    for i in numbers :
        sum = sum + i
    # print("Average is: ",sum/len(numbers))
    return sum/len(numbers)

c = avg(1,2,3,4,5)
print(c)

def name(**name):
    print(type(name))
    print("Hello, ",name["fname"],name["sname"],name["lname"])

name(fname="Ram",sname="Gopal",lname="Aiyyer")