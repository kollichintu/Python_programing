class person:
    
    first_Name = ''
    last_Name = ''
    
    def __init__(self,fname,lname):
        self.first_Name = fname
        self.last_Name = lname
    
    def printFullName(self):
        print(self.first_Name + ' ' + self.last_Name)
        
    
    
abcdObj = person('Wafa','Studies')
abcdObj.printFullName()


class animal(person):
    
    
    def __init__(self, fname, lname,year):
        self.passedOutYear = year
        

    def passed_Out_Year(self):
        print('started learning python from ' ,self.passedOutYear)
        

def_Obj = animal('Python','Learning',2023)
def_Obj.printFullName()
def_Obj.passed_Out_Year()
    