import random

#Print any random number in float between 0 and 1
print(random.random())

#Print any random number between 10 and 20 
print(random.randint(10,20))

# Randomly picks any element
members =["jhon", "Mary", "Red", "Black"]
print(random.choice(members))

class Dice:
    
    def roll():
        Numbers = [1,2,3,4,5,6]
        print(f"({random.choice(Numbers)},{random.choice(Numbers)})")
        
dice = Dice
dice.roll()


