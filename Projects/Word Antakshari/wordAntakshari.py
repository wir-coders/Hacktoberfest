import random

print("Hello Player. Let's get started right away")
print("rules: ")
print("1. To start every round, you need to input a word (it should be a valid word within any dictionary)")
print("2 The computer will give you the next word according to the last letter of your word and so on")
print("You have 10 rounds")
reply = str(input("shall we begin? please reply with Y for yes or N for no: "))
proceed = "y" or "Y"
game_list = []
newstring = ""
cpuword=""
cpuscore,userscore=0,0
if reply == proceed:
    for i in range(10):
        print("Welcome to round: " + str(int(i)))

        fobj = open("pthondictionary.txt")
        text = fobj.read().strip().split()


        while True:
            if newstring!="":
                print("New starting letter is ",newstring)
            word = str(input("Please enter a word to start with: ")).lower()
            if (newstring != ""):
                if word[0] == newstring[-1]:
                    if word in game_list:
                        print("You cannot reuse this word again")
                        continue
                    if word == "":
                        continue
                    if word in text:
                        game_list.append(word)
                        userscore+=len(word)
                        for match in text:
                            if match[0] == word[-1]:
                                with open("match.txt", "a") as f:
                                    f.write(match + "\n")
                        break
                    else:
                        print("Your word is not valid since it's not in dictionary, Please retry")
                        continue
                else:
                    print("your word should start from the computer's end word")
                    continue
            else:
                if word in game_list:
                    print("You cannot reuse this word again")
                    continue
                if word == "":
                    continue
                if word in text:
                    game_list.append(word)
                    userscore += len(word)
                    for match in text:
                        if match[0] == word[-1]:
                            with open("match.txt", "a") as f:
                                f.write(match + "\n")
                    break
                else:
                    print("Your word is not valid since it's not in dictionary, Please retry")
                    continue
        fobj.close()

        f = open("match.txt", "r")
        cpuword = str(random.choice(f.readlines())).strip("\n")
        game_list.append(str(cpuword))
        cpuscore += len(cpuword)
        print(cpuword)
        newstring=cpuword[-1]
        f.close()
        f = open("match.txt", "w")
        f.write("")
else:
    exit(print("Thanks for trying our game "))

if(userscore>cpuscore):
    print(f'Winner is USER. USERS POINT IS {userscore} and COMPUTERS POINT IS {cpuscore}')
elif(userscore<cpuscore):
    print(f'Winner is CPU. CPU POINT IS {cpuscore} and USER POINT IS {userscore}')
else:
    print("GAME DRAW")