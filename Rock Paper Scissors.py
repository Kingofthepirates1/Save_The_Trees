import random

randomint = random.randint(0, 2)
tempinput = input("Rock, Paper, Scissors!").lower()

if tempinput == "rock":
    tempint = 0
elif tempinput == "paper":
    tempint = 1
elif tempinput == "scissors":
    tempint = 2

if randomint == 0:
    cpuinput = "Rock"
elif randomint == 1:
    cpuinput = "Paper"
elif randomint == 2:
    cpuinput = "Scissors"

if randomint - tempint == 1:
    print("I picked " + cpuinput + ". You lose!")
elif tempint - randomint == 2:
    print("I picked " + cpuinput + ". You lose!")
elif randomint == tempint:
    print("Draw! You both chose" + cpuinput)
else:
    print("I picked " + cpuinput + ". You win!")