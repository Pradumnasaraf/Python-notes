i =0
while i<5:
    print(" * "*i)
    i = i+1
print("Done")


win_guess = 9
i=1
while i <= 3:
    user_guess = input(f"Guess {i} : ")
    i= i+1
    if int(user_guess) == win_guess:
        print("You Win")
        break  
else: 
    print("You Loose")
    
