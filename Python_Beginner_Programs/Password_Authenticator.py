import getpass

#getpass which used to take password as password(blank) without appearing to user on screen
username_Password = {"kollichintu":"868836","laxmankolli":"dell@","laxman":"1234"}
user_Name = input('Enter userName here :')
password = getpass.getpass('Enter password here :')

for i in username_Password.keys():
    if user_Name == i:
        while password != username_Password.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
       


