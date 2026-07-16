import random
rn = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if rn == 0:
    print("YOURS CHOICE IS: ")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
    
elif rn == 1:
    print("YOURS CHOICE IS : ")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif rn == 2:
    print("YOURS CHOICE IS : ")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

random_choice = random.randint(0,2)
print("COMPUTERS CHOICE IS :")
if random_choice == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

elif random_choice == 1:
    print("""  
          ____________
    ---'        ______)
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif random_choice == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    
if rn == 0 and random_choice == 2:
    print("YOU WON THIS GAME")
elif rn == 1 and random_choice == 0:
    print("YOU WON THIS GAME")
elif rn == 2 and random_choice == 1:
    print("YOU WON THIS GAME")
elif rn == random_choice:
    print("GAME TIE REMATCH ")
else:
    print("YOU LOST THIS GAME")
