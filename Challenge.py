class Employee:
    def __init__(self, name, Id, post):
        self.name=name
        self.Id = Id
        self.post = post
    
    def print_details(self):
        print("The name of the employee is: ",self.name)
        print("The Id of the employee is: ",self.Id)
        print("the post of the employee is: ",self.post)

    def __del__(self):
        print("Employee is destroyed")

employee1= Employee("Vivaan", "99130324", "6 , abc , street")

employee1.print_details()