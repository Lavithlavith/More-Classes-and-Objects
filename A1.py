class IOString():
    def __init__(self):
        self.str1 = ""
    
    def get_string(self):
        self.str1 = input("Enter String:")
    
    def print_string_upper(self):
        print("Result is upper is: ",self.str1.upper())
    def print_string_lower(self):
        print("Result in lower is: ",self.str1.lower())

str1 = IOString()

str1.get_string()
str1.print_string_upper()
str1.print_string_lower()
