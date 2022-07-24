f = open('sample.txt', 'r')
data = f.readline()  # this method helps to read the text line.
print(data)
data = f.readline()
print(data)
f.close()