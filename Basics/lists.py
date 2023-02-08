import random as rd



coin_toss = ["Heads","Tails"]

print('Coin Tossed value is',coin_toss[rd.randint(0,1)])


fruits = ["Apple","Mango","Kiwi"]
#append
fruits.append("Banana")

#insert
fruits.insert(1,"Orange")
#print(fruits)

#extend
seasonal_fruits = ["Watermelon","Sapota"]
fruits.extend(seasonal_fruits)
#print(fruits)

#remove
fruits.remove("Watermelon")
#print(fruits)

#pop
fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)

#looping in list
for item in fruits:
    print(item)

for item in range(len(fruits)):
    print(fruits[item])

#sort,reverse
fruits.sort()
print(fruits)
seasonal_fruits.reverse()
print(seasonal_fruits)

#join
new_list = [1,2,3]
mixed_list = seasonal_fruits + new_list
print(mixed_list)
for item in new_list:
    seasonal_fruits.append(item)

    
print(seasonal_fruits)