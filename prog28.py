# a = input("Enter the Number: ")
# print(f"Multiplication table of {a} is :")
# try:
#   for i in range(1,11):
#     print(f"{int(a)}X{i} = {int(a)*i}")
# except Exception as e:
#     print(e)

# print("Some imp Lines of Code")
# print("End of Program")

try:
    num = input("Enter the Number: ")
    a = [6,4]
    print(a[num])
except ValueError:
    print("Invalid Input")
except IndexError:
    print("Index Error")