import random

name = "Calvin"
question = "Will I be sucessful?"
answer = ""

random_number = random.randint(1, 13)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Absolutely"
elif random_number == 11:
  answer = "Nein"
elif random_number == 12:
  answer = "Possibly"
elif random_number == 13:
  answer = "Frankly my Dear ... NO"
else:
  print("ERROR")

if name == "":
  print("Question: " + question)
elif question == "":
  print("Error ask a question!")
else:
  print(name + " asks: " + question)


print("Magic 8-Ball's Answer:", answer)
