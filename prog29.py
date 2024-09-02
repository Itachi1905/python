def func():
    try:
        l = [1,2,3,4]
        a = input("Enter the Index: ")
        print(l[a])
        return 1
    except:
        print("Some error Occured")
        return 0
    finally:
        print("I am always Executed")
    
    # print("I am always Executed")

x = func()
print(x)