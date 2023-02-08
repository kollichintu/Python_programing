import os


file_read = open('Notes.txt','a')
file_read.write('\n second line from code with append mode')

file_read.close()


# '''doc string like multline comment '''


another_file = open('C:\\Users\\LaxmanKolli\\Desktop\\WorkupFiles\\Workup\\DE.txt','r')
# for line in another_file:
#     print(line)

print(another_file.readline())

#a --->append the given content to the file
#w --->overwrite the content if file exists.
#x  -->create a new file


#remove --->remove file using os module
#rmdir ---> remove dir/folder

if os.path.exists('sample.txt'):
    os.remove('sample.txt')
else:
    print('file do not exists')
    

first_list = [1,2,3,4,5]

def square_fun(num):
    return num * num

new_list = list(map(square_fun,first_list))
print(new_list) 