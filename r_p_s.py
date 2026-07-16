import random
urs_choise = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if urs_choise == 0:
    print("YOURS CHOICE IS: ")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
    
elif urs_choise == 1:
    print("YOURS CHOICE IS : ")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif urs_choise == 2:
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
    
if  urs_choise == 0 and random_choice == 2:
    print("YOU WON THIS GAME")
elif urs_choise == 1 and random_choice == 0:
    print("YOU WON THIS GAME")
elif urs_choise == 2 and random_choice == 1:
    print("YOU WON THIS GAME")
elif urs_choise == random_choice:
    print("GAME TIE REMATCH ")
else:
    print("YOU LOST THIS GAME")
