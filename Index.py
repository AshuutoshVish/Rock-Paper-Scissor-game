"""
Rock paper scissor game 
      Workflow
1. Input from user
2. Computer choice randomly
3. Result(who will win)

cases:-
A-Rock 
Rock -Rock     =tie
Rock -Paper    =paper Win(Comp Win)
Rock -Scisssor =Scissor win

B- Paper
Paper - Paper    =tie
Paper - Rock     =Paper Win
Paper - Scissor  =Scissor Win(Comp Win)

C- Scissor
Scissor - Scissor    =tie
Scisoor - Rock       =Rock Win(Comp win)
Scissor - Paper      =Scissor win
"""

#Now Coding Part
import random
item_list=["Rock", "Paper", "Scissor"]

user_Choice=input("Enter Your choice : Rock, Paper, Scissor : ")
comp_Choice=random.choice(item_list)
print(f"User Choice={user_Choice}, Computer Choice={comp_Choice}")

#Tie
if user_Choice==comp_Choice:
    print("Tie \nBoth Chooses Same")


#Rock
elif user_Choice=="Rock":
    if comp_Choice=="Paper":
        print("Computer Win \nPaper covers the rock")
    else:
        print("User Win \nRock smashes Scissor")


#Paper
elif user_Choice=="Paper":
    if comp_Choice=="Rock":
        print("User Win \n Paper covers the Rock")
    else:
        print("Computer Win \n Scissor cut the paper")


#Scissor
elif user_Choice=="Scissor":
    if comp_Choice=="Paper":
        print("User Win \n Scissor cut the paper")
    else:
        print("Computer Win \n Rock smashes the Scissor")