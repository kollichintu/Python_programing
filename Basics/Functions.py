def my_Function():
    print('This is print statement under function')


my_Function()

# *args ==>* used when unsure about argument values --->returns tuple with values
#**args ===>** used when unsure about multiple argument ---->returns dict with key pair value

#Recusrsive function --->function calling its function

def num_Factorial(x):
    if x == 1:
        return 1
    else:
        return x *num_Factorial(x-1)


print(num_Factorial(4))

#Annonymous or Lambda func

lambda x: x*x


class abcd:
    def __init__(self):
        print('this is __init__ function')

ab_cd = abcd()

        
