print("Welcome to the best quiz in the world!")

name = input("What is your name? ")


playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Note: Questions that prompt for a player's name will only require their last name to be entered. If a player is commonly known by a single name, please use that name for the input.")

print("--------------------")
print("Beware of Danger Questions, get one wrong and lose a point!")



print("Okay! Let's Play!")
score = 0

print("--------------------")
print("Question Number 1")
answer = input("Which English club was the first to win the European Cup in 1968? ")
if answer.lower() == "manchester united":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Manchester United")
  score -= 1

print("--------------------")
print("Question Number 2")
answer = input("Who is the all-time top scorer for the German national team? ")
if answer.lower() == "klose":
  print("Correct!")
  score += 1
else:
  ("Incorrect! The correct answer is " + " Borussia Miroslav Klose")
  score -= 1

print("--------------------")
print("Question Number 3")
answer = input("Who is the youngest player to ever score in a World Cup tournament? ")
if answer.lower() == "pele":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Pelé")
  score -= 1

print("--------------------")
print("Question Number 4")
answer = input("WWhich club did Jürgen Klopp manage before joining Liverpool? ")
if answer.lower() == "dortmund":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + "Dortmund")


print("--------------------")
print("Question Number 5")
answer = input("Which player holds the record for the most goals scored in a single Premier League season? ")
if answer.lower() == "haaland":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Haaland")
  

print("--------------------")
print("Question Number 6: " + "Danger Question!")
answer = input("Which country hosted the 1982 FIFA World Cup? ")
if answer.lower() == "spain":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Spain")
  score -= 1

print("--------------------")
print("Question Number 7: " + "Danger Question!")
answer = input("Which player has won the most FIFA Women's World Player of the Year awards? ")
if answer.lower() == "marta":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Marta")
  score -= 1

print("--------------------")
print("Question Number 8: " + "Danger Question!")
answer = input("In what year did the UEFA Cup change its name to the UEFA Europa League? ")
if answer.lower() == "2009":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " 2009")
  score -= 1

print("--------------------")
print("Question Number 9: " + "Danger Question")
answer = input("Which player was known as Il Divin Codino(The Divine Ponytail)? ")
if answer.lower() == "baggio":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Baggio")
  score -= 1

print("--------------------")
print("Question Number 10")
answer = input("Which manager won the UEFA Champions League three times in a row with Real Madrid from 2016 to 2018? ")
if answer.lower() == "zidane":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + " Zidane")


print("Bonus Question!")

answer = input("Who is the best person in the world? " )
if answer.lower() == "alan sugar":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The correct answer is " + "Alan Sugar")
  

print("--------------------")
print("Congratulations " + str(name) + " you got " + str(score) + " questions correct!")

print("Yot got " + str((score / 11) * 100) + "%.")

if score <= 4:
  print("You're dumb")
elif score <= 5:
  print("You're mid")
else:
  print("You're a Genius")
