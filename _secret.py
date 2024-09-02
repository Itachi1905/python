import random

a = input("Enter the String to be Encrypted -> ")
l = ord('a')
if(len(a) < 3) :
    b = a[::-1]
    print(b)
else :
    r1 = random.randint(l, l+26)
    r2 = random.randint(l, l+26)
    r3 = random.randint(l, l+26)
    r4 = random.randint(l, l+26)
    r5 = random.randint(l, l+26)
    r6 = random.randint(l, l+26)
    c = a[0]
    b = a[:0] + a[1:] + c
    result = chr(r1) + chr(r2) + chr(r3) + b + chr(r4) + chr(r5) + chr(r6)
    print(result)

a = input("Enter the String to be Decrypted -> ")
l = ord('a')
if(len(a) < 3) :
    b = a[::-1]
    print(b)
else :
    b = a[3:len(a)-3]
    c = b[len(b)-1]
    res = c + b[:len(b)-2]
    print(res)