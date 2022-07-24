# contructor and its methods

class employee():
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def show_employee_details(self):
        print("the name of employee is  ", self.name)
        print("the age of employees is ", self.age)
        print("the salary of employee is  ", self.salary)
        print("the gender of employees is  ", self.gender)

e1 = employee("nona",25,10000,"male")

e1.show_employee_details()

