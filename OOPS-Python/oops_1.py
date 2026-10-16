#initate a class
class employee:
    #special method/magic method/dunder method - constructor
    #below things are just for example irl we use constructor for methods that needs to be executed by default
    # when we open facebook we get connected to database automatically user dont need to do that sp thats a real life example
    
    def __init__(self):
        print("started executing attributes/data")
        self.id =123
        self.name="bhati"
        self.salary = 500000
        self.designation = "sde"
        print("attributes executed")

    #define a method in a class
    def travel(self,destination):
        print("travel method was called manually")
        print(f"employee is going to{destination}")
    

#above we defined a class so now we need to make objects of that class
sam=employee()

print(sam.id) #print attributes

#calling a method
sam.travel("kerela")
