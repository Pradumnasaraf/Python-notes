try:
    age = int(input("Age: "))
    income = 200
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Age Can't be zero")

except ValueError:
    print("Invalid Value")
    
