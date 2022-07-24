# this is first method to execute percentage question
# marks = [89, 56, 23, 78]
# percentage = (sum(marks)/400)*100

# print(percentage)

# this is second method to execute percentage question
#marks = [45, 56, 78, 99]
#percentage = ((marks[0] + marks[1] + marks[2] + marks[3])/400) *100
#print(percentage)

# this is third method ....
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400) *100
    return p

marks = [45, 56, 78, 99]
percentage = percent(marks)

print(percentage)
  

