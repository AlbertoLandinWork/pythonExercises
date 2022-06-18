# clases
class Employee:
    def __init__(self, first, last, title, department):
        self.first = first
        self.last = last
        self.title = title
        self.department = department
        self.email = first.lower() + "." + last.lower() + "@calzadorutila.com"

    def display_divider(self, arg_char = "-", line_lenght = 100):
        print(arg_char * line_lenght)
    
    def display_information(self):
        self.display_divider("-", 45)
        print(f"Employee information | {self.first} {self.last}".center(45, " "))
        self.display_divider("-", 45)
        print(f"Title: {self.title} | Department: {self.department}")
        print(f"Email address: {self.email}")

    #Getters
    @property
    def fullname(self):
        print(f"{self.first} {self.last}")
    
    #Setters
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    #Deleters
    @fullname.deleter
    def fullname(self):
        print("Name & last name has been succssesfully deleted")
        self.first = None
        self.last = None

# Instances

employee_01 = Employee("Alvison", "Hunter", "Web Development", "Development team")
employee_01.fullname = "Raúl Sánchez"
employee_01.display_information()