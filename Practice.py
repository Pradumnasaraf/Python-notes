
started = False
while True:
    user_input = input("> ")
    if user_input == "help":
        print('''
start - to start the car.
stop - to stop the car.
quit - to exit
        ''')
    elif user_input == "start":
        if started : 
            print("Car Alraedy Started")         
        else:
            print("Car Started")
            started = True
             
    elif user_input == "stop":
        if not started:
            print("Car Already Stopped")
        else:
            started = False
            print("Car Stopped")
            
            

    elif user_input == "quit":
        break

    else:
        print("Invalid! Input try help command")




        