# Treasure Island
# you have to find out the treasure with some right guess


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
a=input("You're at a cross road. where you want to go? Type \"left\" or \"right\" \n").lower()
if(a == "left"):
  b=input("you come to a lake. There is an island in the middle of lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()

  if(b=="wait"):
    c=input("You arrive at the island unharmed. There is a house with 3 doors. one red, one blue and one yellow.Which color do you choose? \n").lower()

    if(c=="yellow"):
      print("You Win!")

    elif(c=="red"):
      print("You Burned by fire. Game Over!")

    elif(c=="blue"):
      print("You enter a room of beasts. Game Over!")

    else:
      print("Game Over!")
  else:
    print("You attacked by trout. Game Over!")
else:
  print("You fall into a hole. Game Over!")

