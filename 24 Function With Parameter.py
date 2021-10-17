def user_name(name):# Name is Parameter
    print(f"Hey {name}, How are you?")

user_name("Pradumna") #Here Pradumna is Argument
user_name("Mary")

def add_two_num(Num1,Num2):
    print(Num1+Num2)

add_two_num(3,6)

# Keyword Arguments:

def two_num(num1, num2):
    print(f"{num1} {num2}")

two_num(num2=4,num1=3) #Here position doesn't matters

# First you positional agrument then keyword agrument
two_num(4, num1=3)

