def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError ("this is not good ")    

a = increment(45679123)

print(a)