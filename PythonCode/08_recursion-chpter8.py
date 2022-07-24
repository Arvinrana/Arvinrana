# n = 500
# product = 1
# for i in range(n):
   # # product = product *(i+1)

# print(product)    

# factorial recursion
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
        return product
f = factorial_iter(8)
print(f)        

# recursion method not clear 