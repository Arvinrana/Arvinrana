import os
oldname = "peoms.txt"
newname = "poems.txt"

with open("peoms.txt") as f:
    data = f.read()

with open("poems.txt", "w") as f:
    f.write(data)

os.remove(oldname)


# this exercise is used to rename the existing file 
