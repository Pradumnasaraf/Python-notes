numbers =[5,2,3,5,4,5,6]

numbers.append(20) #Add item to the end of list
numbers.insert(0,25) # insert the list iteam at particular index
numbers.remove(5) # Remove Item from the list
# numbers.clear()
numbers.pop() # Remove the list item from the list
print(50 in numbers) # Check if 50 is the list or not
print(numbers.count(5)) # Tell us how many time that number occurs in that list
print(numbers)
numbers.sort() # Sorting the list
print(numbers)
numbers2 = numbers.copy() # Make a copy of list
print(numbers2)
#print(numbers.index(50))

numbers3 =[5,2,3,5,4,5,6]

for items in numbers3:
    if items == items+1:
        numbers3.remove(items)
print(numbers3)

num =[5,2,3,5,4,5,6]
numb1 =[]
for item in num:
    if item not in numb1:
        numb1.append(item)
print(numb1)
