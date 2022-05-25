print("welcome!")
playing = input("do you want to play?")
if playing.lower() != "yes":
    quit()

print("Okay!let's play:)")
score = 0

answer = input("what does cpu stand for?")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stand for?")
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does psu stand for?")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got " + str(score)+ " questions correct!")