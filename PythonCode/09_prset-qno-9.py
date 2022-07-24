file1 = "peoms.txt"
file2 = "sample.txt2"

with open(file1) as f:
    f1 = f.read()
    

with open(file2) as f:
    f2 = f.read()
    
if f1 == f2:
    print("files are identical")  
else:
    print("files are not identical")      

# this exercise is used to identify the file that is there any same file exist or not