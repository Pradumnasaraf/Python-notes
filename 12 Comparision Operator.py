temp =30

if temp == 30:
    print("it's a hot day")
if temp > 30:
    print("it's a Very hot day")
else:
    print("It's not a hot day")

# Question 1

name = input("Enter some Char. ")
no_of_char = len(name)

if no_of_char <3:
    print("name must be at least 3 Char") 
elif no_of_char > 50:
    print("name can't be greater tha 50 char")
else :
    print("Name Looks Good!")

# Question 2

user_weight = int(input("Weight: "))
Weight_unit = input("(L)bs or (K)g: ").upper

if Weight_unit == "L":
    print(user_weight*0.45)

else:
     print(user_weight/0.45)
    
    
