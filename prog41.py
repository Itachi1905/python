# READING A FILE

# f = open('prog41.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open('prog41.txt', 'a')
f.write('Hello, world!')
f.close()

with open('prog41.txt', 'a') as f:
  f.write("Hey I am inside with")