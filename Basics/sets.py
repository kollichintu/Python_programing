this_Set = {'Apple','Banana','Cat','Cat'}
print(type(this_Set))
print(this_Set)

for i in this_Set:
    print(i)

print(len(this_Set))

this_Set.remove('Cat')
print(this_Set)

#discard to use than remove when unsure about the key object in set doesn't throw an error.
this_Set.discard('Cat')
#this_Set.remove('Cat')

that_Set = {1,2,3,4}

combine_Set = this_Set.union(that_Set)
print(combine_Set)

combine_Set.symmetric_difference_update(that_Set)

#intersection ---returns matching items
#difference ---returns non matching items
# combine_Set.intersection_update(that_Set)

print(combine_Set)


