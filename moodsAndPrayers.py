import datetime

def askName():
    name = input("Name: ")
    print()
    return name

def prayer(talkToGod):

    talk =  talkToGod.lower()

    yesResponse = ("yes", "yeah", "yea", "yas", "ye", "oo", "oh", "o", "sige", "cge", "sige", "yah", "yeh", "ye")

    if any(word in talk for word in yesResponse):
        print("\nYay let's pray!! :)")
        print("=======================================")

        questions = [
            "what are you thankful for today? what blessing did God give you?",
            "what are the burdens you wanna surrender to God?", 
            "what sin or weakness do you want God to heal?",
            "what did God reveal to you recently?",
            "where did you see His goodness today?",
            "\nYou may compose your own prayer here, that you might wanna tell God.\nBe sure to be have a genuine heart."
        ]

        answers = []

        for q in questions:
            print(q)
            a = input("write here: ")
            answers.append(a)

        return answers
    else:
        print("It's okay. And God will always welcome you! See you maybe next time. :D")
        return None

def welcome():
    print("=======================================")
    print("WELCOME TO MOODS AND PRAYERS ! :D")
    print("=======================================")
    print()

def askMood():
    print("How are you feeling today?")
    mood = input("Enter your mood: ")
    print()
    return mood
    
def askReason():
    print("Would you like to share why you feel this way?")
    reason = input("Your reason: ")
    print()
    return reason

def askMessageToGod():
    print("Would you like to write a short message to God? :D")
    messageToGod = input("Your message to God: ")
    print()
    return messageToGod

def message(mood):
    print("=======================================")
    print("Here's a message for you! :D")
    print("=======================================")
    print()

    lowerMood = mood.lower()

    if "happy" in lowerMood:
        print("I'm glad you're feeling happy today! WOOHOOO")
        print("You are doing well. Keep it up. :)")
    elif "sad" in lowerMood:
        print("It'll be okay. Better days are ahead! :)")
        print("Many people care and love you. And It's okay to feel sad.")
    elif "tired" in lowerMood:
        print("Take some rest.")
        print("You deserve it!!")
    elif "excited" in lowerMood:
        print("WHOAAA if you're excited, I'm excited! Let's gooo!")
    elif "stressed" in lowerMood:
        print("Take some rest champ.")
        print("Let's pray? :D")
    else:
        print("Whatever your mood is, I'm sure God and everyone else is still proud of you.")

def saveToFile(name, mood, reason, messageToGod, prayerAnswers):
    now = datetime.datetime.now()

    file = open("moodsAndPrayers.txt", "a")

    file.write("---------------------------------------------------------------------------------------------------------------------")
    file.write("\nDate: " + str(now) + "\n")
    file.write("Name: " + name + "\n")
    file.write("Mood: " + mood + "\n")
    file.write("Reason: " + reason + "\n")
    file.write("Message to God: " + messageToGod + "\n")
    
    if prayerAnswers is not None:
        file.write("Let us pray then!\n")
        for item in prayerAnswers:
            file.write(item + "\n")
        
        file.write("---------------------------------------------------------------------------------------------------------------------")
        file.close()

        print("\nYou're doing great! God always loves you!")
        print()

def main():
    welcome()
    name = askName()
    mood = askMood()
    reason = askReason()
    messageToGod = askMessageToGod()
    message(mood)

    talkToGod = input("Do you wanna pray? ")

    prayerAnswers = prayer(talkToGod)
    saveToFile(name, mood, reason, messageToGod, prayerAnswers)
    print("Thank you for your time! You are a good person!")
    print("God loves you! :)")

main()