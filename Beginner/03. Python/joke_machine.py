jokes=["What did the pirate say when he turned 80? - Aye Matey", "Why cant you trust an Atom? -Because they make up everything!","What do computers eat for a snack? - Microchips!", "Why did the scarecrow get a promotion?- He was outstanding in his field!","What do you call a chicken who counts her eggs?- A Mathmachicken!","A jump lead walks into a bar. The barman says dont start anything!.","Whats the difference between a Hippo and a Zippo? -One is really heavy and the others a little lighter!","The guy who invented predictive text died last night- His funfair is next Monkey.","Parallel lines have so much in common its a shame they will never meet","Someone stole my Microsoft Office andy they're gonna pay- You have my Word!",]

def joke_machine(): 
    while True:
        try:
            num=int(input("Enter your favorite number between 1 and 10 and i will tell you a joke: ")) 
        except:
            print("Please enter a number between 1 and 10")
        else:
            break

    if num==1:
     print (jokes[0])
    elif num==2:
     print (jokes[1])
    elif num==3:
     print (jokes[2])
    elif num==4:
     print (jokes[3])
    elif num==5:
     print (jokes[4])
    elif num==6:
     print (jokes[5])
    elif num==7:
     print (jokes[6])
    elif num==8:
     print (jokes[7])
    elif num==9:
     print (jokes[8])
    elif num==10:
     print (jokes[9])
    else:
     print("Stop joking around and enter the right number!")

    play_again()

def play_again():
    replay=input("Would you like to play again? Hit Y for Yes and N for No: ")
    if replay.upper() =='Y':
        joke_machine()
    elif replay.upper() == 'N':
        print("Oh thats too bad , see you soon")
    else:
        play_again()


def welcome():
    print("""***********************************************************
              WELCOME TO DENICE'S JOKE MACHINE!!
***********************************************************""")


welcome()
joke_machine()
