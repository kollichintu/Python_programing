#Mean
list1 = [3,7,10,13,18,20,25,29,30]

mean_list1 = round(sum(list1)/len(list1))

print('mean is ',mean_list1)

#Median
# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}thterm

list1 = [12, 16, 20, 12,  23, 24]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print('medain is ',median)


#Mode
list_1 =[4, 7, 3, 17, 11, 3, 9, 3, 10, 20]
frquency = {}
for i in list_1:
    frquency.setdefault(i,0)
    frquency[i]+=1

    
frequent = max(frquency.values())


for i,j in frquency.items():
    if j == frequent:
        mode = i
print('mode is ',mode)

