this_Tuple = ("A","B","C","D")
print(type(this_Tuple))
print(this_Tuple[1:])

that_Tuple = ('BMW','AUDI','Benz','MG')
print(type(that_Tuple))

#tuple to list
new_list = list(that_Tuple)
new_list[1] = 'Audi'

# list to Tuple
that_Tuple = tuple(new_list)
print(that_Tuple)
print(type(that_Tuple))

#unpacking a tuple
(a,b,c,d) = this_Tuple
print(a,b,c,d)

# Join tuple
first_tuple = this_Tuple * 2
print(first_tuple)

last_tuple = this_Tuple + that_Tuple
print(last_tuple)

#count,index