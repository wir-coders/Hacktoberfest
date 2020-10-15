def showAries():
    print("ARIES (March 21 – April 19)")
    print("")
    print("Aries is independent in nature, fun loving, impulsive and a tough cookie. You desire big goals and possess the determination to accomplish them without getting weakened by any hurdle. " +
          "The courage and ambition you hold are worthy enough to drive you ahead. Sometimes your bossy behavior tends to be hurtful.")
    print("")
    print("Try to strengthen your ego and not suppress others.")

def showTaurus():
    print("TAURUS (April 20 – May 20)")
    print("")
    print("Taurus, the born leaders, are morally and ethically upright and loyal. You possess a firm spirit which keeps you moving on the right path. " +
          "Your ethicality knows no limits. You keep your emotions and feelings to yourself. The unmoving emotions and behavior turn you into a reserved and obstinate person. " +
          "Your work act as the barricade between your emotions and you as it consumes all your time and restricts you in sharing what you feel.")
    print("")
    print("You must open and communicate as it would provide you relief rather than hurting you.")

def showGemini():
    print("GEMINI (May 21 – June 20)")
    print("")
    print("The Combination of charismatic persona and open personality. Your versatility, intelligence, and witty behavior draw the attention of people. " +
          "Being happy is your life's Mantra, no matter what ups and downs you face. Your excellent communication skills keep your social circle growing. " +
          "As you easily get bored, you tend to be insensitive towards others’ feelings.")
    print("")
    print("Try to have a better understanding of others' perspective and feelings too.")

def showCancer():
    print("CANCER (June 21 – July 22)")
    print("")
    print("Cancer is the most understanding, generous and emotional among all. And, the biggest introvert with the deepest feelings and emotions, on the other side. " +
          "Rather than living in a practical world, you live in a world of fantasy with hundreds of voices revolving in your head and guiding your way.")
    print("")
    print("Try to have more social connections and live in a practical world.")

def showLeo():
    print("LEO (July 23 – Aug. 22)")
    print("")
    print("Leo, the born leaders, are noble, honest and confident. You always remain in the spotlight and holds a persona which attracts others. " +
          "But sometimes you are self-centered and highly rely upon others' viewpoints and opinion.")
    print("")
    print("You must ensure that your decisions are not dependent on others, rather, they must be based on your own views.")

def showVirgo():
    print("VIRGO (Aug. 23 – Sept. 22)")
    print("")
    print("Virgo is practical, meticulous and cool-headed. You are the one with the solution to every problem. In the race of heart and head, you always listen to your head. " +
          "Sometimes you set unrealistic goals which are hard to accomplish that also creates a difficult situation for you and others.")
    print("")
    print("You must go with the flow rather than controlling everything.")

def showLibra():
    print("LIBRA (Sept. 23 – Oct. 22)")
    print("")
    print("Libra is diplomatic but is balanced in nature, possess the carefree attitude and are pleasant in behavior. " +
    "You are balanced in making decisions but because of your careless behavior, you face difficult situations. " +
          "You try to make others comfortable. You think too much which results in delayed decisions.")
    print("")
    print("Try to take prompt decisions by believing in yourself.")

def showScorpio():
    print("SCORPIO (Oct. 23 – Nov. 21)")
    print("")
    print("Scorpio is people with a sensual, creative and confident persona. Your sensual nature makes you the best lovers of all the zodiacs. " +
          "You hold a magnetic pull which draws the attention of people. You have a sharp memory and a revengeful streak which can be dangerous for your enemies.")
    print("")
    print("It is good for you to move on and forgive rather than keeping knots of grudges.")

def showSagittarius():
    print("SAGITTARIUS (Nov. 22 – Dec. 21)")
    print("")
    print("Sagittarius holds explosive, fiery and generous personality. You attract people with your funny behavior and generosity. " +
          "Many times you also hurt others with your frank and fearless attitude as you unintentionally hurt others with your outspoken attitude.")
    print("")
    print("Try to listen to other people too and remain emotionally-available.")

def showCapricorn():
    print("CAPRICORN (Dec. 22 – Jan. 19)")
    print("")
    print("Capricorns are hardworking, calm, determined and motivated. You are helpful and practical in nature. " +
          "Whatever the challenges are, you always remain ready and keep attaining your desired goals. Your workaholic nature and competitive spirit can sometimes be annoying to others.")
    print("")
    print("Sometimes slowing down your speed might help you cherish every moment.")

def showAquarius():
    print("AQUARIUS (Jan. 20 – Feb. 18)")
    print("")
    print("Being Aquarius, you are alluring, adventurous and captivating in nature. You possess worldly knowledge because of your passion for travel. " +
          "Your personality is full of intelligence and you keep the conversation going for hours owing to your excellent communication skills. " +
          "However, your independent and unpredictable nature sometimes makes difficult for people to understand you.")
    print("")
    print("It’s good to communicate with an open heart, to make your trips more happening.")

def showPisces():
    print("PISCES (Feb. 19 – March 20)")
    print("")
    print("Being a Pisces, you tend to be compassionate, sympathetic and artistic. You are the one with a pure heart and always remain kind to others. " +
          "You hold a personality that craves solitude. You live in a world of dreams and imagination and possess the huge interest in music and art.")
    print("")
    print("Try to live in a practical world rather than losing yourself in thoughts and imaginations.")

def main():
    sign = input("Enter your zodiac sign to know your sign's characteristics and personality traits: ")
    if sign.lower() == "aries":
        showAries()
        print("")
        print("")
        main()
    elif sign.lower() == "taurus":
        showTaurus()
        print("")
        print("")
        main()
    elif sign.lower() == "gemini":
        showGemini()
        print("")
        print("")
        main()
    elif sign.lower() == "cancer":
        showCancer()
        print("")
        print("")
        main()
    elif sign.lower() == "leo":
        showLeo()
        print("")
        print("")
        main()
    elif sign.lower() == "virgo":
        showVirgo()
        print("")
        print("")
        main()
    elif sign.lower() == "libra":
        showLibra()
        print("")
        print("")
        main()
    elif sign.lower() == "scorpio":
        showScorpio()
        print("")
        print("")
        main()
    elif sign.lower() == "sagittarius":
        showSagittarius()
        print("")
        print("")
        main()
    elif sign.lower() == "capricorn":
        showCapricorn()
        print("")
        print("")
        main()
    elif sign.lower() == "aquarius":
        showAquarius()
        print("")
        print("")
        main()
    elif sign.lower() == "pisces":
        showPisces()
        print("")
        print("")
        main()
    else:
        print("Sorry, you have entered an invalid zodiac sign. Please try again.")
        print("")
        print("")
        main()

main()

