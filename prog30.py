a = input("Enter Value between 5 and 9 -> ")
if(type(a)==int) :
    if(a<5 or a>9):
        raise ValueError("Value Should be between 5 and 9")
else :
    if(a!="quit") : 
        raise ValueError("Value Should be between 5 and 9")