name = input("Type your name?: ")
print("Welcome", name, "to this adventure! ")

answer = input("You are on a dirt road, it has come to the end and you can go left or right, which way would you like to go (left/right)? ").lower()

if answer == "left":
  answer = input("You have come to a river, you can walk around it or swim across (swim/walk)? ")
  if answer == "swim":
    print("You swam across and were eaten by an alligator.")
  elif answer == "walk":
    print("You walked for many miles, ran out of water and lost the game.")
  else: 
    print("Not a valid option you lose.")

elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head backc (cross/back)? ")

  if answer == "back":
    print("You go back and lose. ")
  elif answer == "cross":
    answer = input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)? ")

    if answer == "yes":
      print("You spoke to the stranger and they give you gold. You win!")
    elif answer == "no":
      print("You ignore the stranger and they are offended. You lose.")
    else: 
      print("Not a valid option you lose.")

  else: 
    print("Not a valid option you lose.")

else: 
  print("Not a valid option you lose.")

print("Thank you for trying " + name)
