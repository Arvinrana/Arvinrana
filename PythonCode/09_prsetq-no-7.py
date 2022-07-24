content = True
i = 1
with open("sample.txt2") as f:
    while content:
        content = f.readline()
        if 'python' in content:
            print(content)
            print(f" yes python is present on line number{i}")
        i+=1

# this exercise is used to find out the particular word in context and where            
        
    