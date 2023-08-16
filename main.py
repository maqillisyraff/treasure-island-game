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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision_direction = input("There are 2 directions in front of you, which are left and right. Which one will you choose?\n")
decision_direction_lower = decision_direction.lower()

if decision_direction_lower == "left":
  decision_river = input("You are currently by the river-side. Do you want to swim or wait for any transport?\n")
  decision_river_lower = decision_river.lower()
  
  if decision_river_lower == "wait":
    decision_door = input("You just arrived the small island and spotted a house with 3 doors, red, yellow and blue. Which one would you choosse?\n")
    decision_door_lower = decision_door.lower()
    if decision_door_lower == "red":
      print("You just trapped in a fire. Game over!")
    elif decision_door_lower == "yellow":
      print("You found the treasure and be the richest person in the world. Congratulations! You win!")
    elif decision_door_lower == "blue":
      print("You were eaten by beasts. Game over!")
    else:
      print("Game over!")
  else:
    print("You were attacked by trout. Game over!")
else:
  print("You fall into a hole. Game over!")
  