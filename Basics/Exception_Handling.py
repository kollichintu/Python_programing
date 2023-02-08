try:
    print(x)
except:
    print('x is undefined')
    

try:
    print('Hello')
except:
    print('error')
else:
    print('Everything Looks Good')
    
    

try:
    print(x)
except:
    print('error with x undefined')
else:
    print('x')
finally:
    print('this is finally block')
    
# file open,write from code
notes_Local = open('Notes.txt','w')
notes_Local.write('Hi this is the line written from python code')

# raise Exception('')
# raise TypeError('')