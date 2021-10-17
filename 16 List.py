names =["Jhon", "Sif","Saraf","Mary"]
print(names[3])
print(names[-1])
print(names[2:])

names[0] = 'Hello'
print(names)

## Find the largest number in the list

list = [1, 2, 3, 6, 11, 3]
Big =list[0]
for items in list:
    if Big <items:
        Big = items
print(Big)