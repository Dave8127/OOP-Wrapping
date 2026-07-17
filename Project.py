class employee():
    def __init__(self):
        self.name = str(input("\nEnter Your Name : "))
        self.age = int(input("Enter Your Age : "))
        self.__e_id = int(input("Enter ID : "))
        self.__salary = float(input("Enter Your Salary : "))
        
    def msg(self):
        print("\nEmployee Created Succesfully.......")
        
    def get_id(self):
        return self.__e_id
    def get_salary(self):
        return self.__salary

    def display(self):
        print(f"Employee Created With Name : {self.name} , Age : {self.age} , ID : {self.get_id()} and Salary : {self.get_salary()}")

class manager(employee):
    def __init__(self):
        super().__init__()
        self.department = str(input("Enter Your Department : "))
        print("\nManager Created Succesfully....")

    def display(self):
        print(f"Manager Created With Name : {self.name} , Age : {self.age} , ID : {self.get_id()} Salary , : {self.get_salary()} and Department : {self.department}")

class developer(employee):
    def __init__(self):
        super().__init__()
        self.language= str(input("Enter Your Progrraming Language : "))
        print("\nDeveloper Created Successfully.....")

    def display(self):
        print(f"Developer Created With Name : {self.name} , Age : {self.age} , ID : {self.get_id()} , Salary : {self.get_salary()} and Progrramming Language : {self.language}")

e = None
m = None
d = None

print("------------- # OOP Wrapping : Employee Management System # --------------")

while True :
   print("\nMenu :")
   print("      1. Create Employee")
   print("      2. Create Manager")
   print("      3. Create Developer")
   print("      4. Show Details")
   print("      5. Exiting.....")

   ch = int(input("\nEnter Your Choice : "))

   match ch :
        case 1:
           e = employee()
           e.msg()
        
        case 2: 
           m = manager()

        case 3:
           d = developer()

        case 4:
           print("\nChoose what U wanna Show : ")
           print("1. Employee")
           print("2. Manager")
           print("3. Developer")

           choice= int(input("\nEnter Your Choice : "))

           match choice :
                case 1 :
                    if e is not None:
                        e.display()
                    else :
                        print("\nCreate a Employee First")
                case 2 :
                    if m is not None:
                        m.display()
                    else :
                        print("\nCreate a Manager First")
                case 3 :
                    if d is not None:
                        d.display()
                    else :
                        print("\nCreate a Developer First")
                case _:
                   print("\nInvalid Choice...")

        case 5 :
           print("\nExiting...........")
           break

        case _:
           print("\nInvalid Choice.........")

        



           



