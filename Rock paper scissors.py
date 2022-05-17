import random 

ending = "N"
while ending == "N":
    
    computer_output = ["rock","paper","scissors"]
    computer_input=random.choice(computer_output)
    user_input = input("rock, paper or scissors: \n")
    
    def losser():
        print("computer chosed,", computer_input, ",you lose Big l")
        
    def winner():
        print("computer chosed,", computer_input, ",you win")
        
    
    if computer_input==user_input:
        print("Both choosed ", user_input, ": So, it is draw")
    elif user_input=="rock":
        if computer_input=="paper":
            losser()
        if computer_input=="scissors":
            winner()
    elif user_input=="paper":
        if computer_input=="scissors":
            losser()
        if computer_input=="rock":
            winner()
    elif user_input=="scissors":
        if computer_input=="rock":
            losser()
        if computer_input=="paper":
            winner()
    elif user_input=="911":
        print("you automatically win")
    else:
        print("invalid input, check your spelling losser")

    ending = input ("Wanna go on ? (Y/N)")
    
        

