# with open('prog43.txt','r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read(5) 
#     print(data)

with open('prog43.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())