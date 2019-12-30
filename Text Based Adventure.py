import random


def error_checking(tempinput, responses, story):
    while True:
        if tempinput not in responses:
            errorval = 1
        else:
            errorval = 0
        if errorval == 1:
            for i in story:
                print(i)
            for i in options:
                print(i)

            tempinput = input("").lower()
        else:
            break


story = ["Hello."]
options = [""]
responses = ["hi", "hello", "hey", "whatup", "hi.", "hello.", "hey.", "1"]
for i in story:
    print(i)
tempinput = input("").lower()
error_checking(tempinput, responses, story)

story = ["What will you do?"]
options = ["1 > Stay in your room", "2 > Go outside"]
responses = ["stay in your room", "stay in my room", "1", "go outside", "2"]
for i in story:
    print(i)
for i in options:
    print(i)
tempinput = input("").lower()
error_checking(tempinput, responses, story)


"""while True:
    if tempinput in ["go outside", "2"]:
        print("")
    elif tempinput in ["stay in your room", "stay in my room", "1"]:
        print("Are you really going to stay in your room? There's a whole game waiting for you!")
        print("1 > Nah man I wanna play minecraft.")
        print("2 > Fine...")
        tempinput = input("").lower()

        if tempinput in ["fine...", "fine", "2"]:
            print("")
        else:
            print("Dude come on. There's more to life than minecraft. Come with me and I'll show you.")
            print("1 > Shut the door on your way out.")
            print("2 > Do me a favor, get me some cheetos from the kitchen")
            print("3 > Oh, like roblox?")
            print("4 > Fine mom, I was gonna go get Mcdonalds anyways.")
            tempinput = input("").lower()

            if tempinput in ["shut the door on your way out", "shut the door on your way out.", "shut the door", "1", "one"]:
                print("That's kind of rude.")
                print(".")
                print(".")
                print(".")
                print("Well have fun, I guess.")
                print("1 > Okay bye.")
                if tempinput in ["1", "Ok bye", "Okay bye", "bye"]:
                    print("")
                    print("")
                    print("")
                    print("")
                    print("You play minecraft and slowly succumb to health issues "
                          "from your dietary choices and sedimentary lifestyle."
                          "You died.")
                else:
                    error_checking
            elif tempinput in ["Do me a favor"]:
                print("")
    else:
        error_checking(tempinput, responses, story)"""