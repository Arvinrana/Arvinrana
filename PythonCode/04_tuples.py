t = (1, 2, 3, 4, 6, 2, 2,) 
t1 = (1,) # this is the correct way to declare tuple
# t1 = (1) # this method get you an error 
# print(t1)

# print(t.count(2))   this method will tell you that how many int. are inside the list
# print(t.index(2))   this method will tell you that in which position int. located in the list 
print(t.index(6))
print(t.count(4))

# tuple is fix , not immutable list 