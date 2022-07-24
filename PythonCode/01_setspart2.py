# important : this syntax will create an empty dict. not epmty set

a = {
}
print(type(a))

# how to create empty set ?
# sets is the collection of non repeated elements 
b = set()
print(type(b))
b.add(4)
b.add(6)
b.add(5)
b.add(4)
b.add(5)
# b.add([4, 5, 6])  list can't be add in sets as well dict.
b.add((4, 5, 6))   # this is tuple method.(())

print(b)
print(len(b)) # it print the length of sets 
b.remove(5)
print(b)
print(b.pop())  #  this method removes artibitary elements 
print(b)

print(b.clear())
print(b)

print(b.union(8,11))  # not cleared will do it later by the help of freind 
print(b)


