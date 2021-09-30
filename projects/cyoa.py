"""A Self-Led Adventure."""

__author__ = 730383189
from random import randint


player: str
points: int = 0
MOON_EMOJI = "\U0001F319"
retry: str
difficulty: str 


def greet() -> None: 
    """Saying hello to player."""
    global player
    player = input("Hey there! What's your name? ")
    print(f"Welcome to the game, {player}, what you'll find here is a horror experience I came up with! It's over 1000 lines of code, so I hope you have fun!")


def main() -> None:
    """Actual Game!"""
    global points
    global player
    global retry   
    global difficulty 

    decision_1: str 
    decision_2: str 
    decision_3: str 
    decision_4: str 
    decision_5: str 
    decision_6: str 
    decision_7: str 
    decision_8: str 
    decision_9: str 
    decision_10: str 
    decision_11: str 
    decision_12: str 
    try_again: str = "Yes"
    greet()
    difficulty = input("Hey! What difficulty would you like to play on! \n1. Hard \n2. Medium \n3. Easy \n") 
    
    """Begins Game."""
    while try_again == "Yes":
        chances(points)
        print(f"You awake in a dark room. {MOON_EMOJI} You don't know where you are, or how you got there.")
        decision_1 = input("What would you like to do? \n1. Go back to sleep \n2. Check phone \n3. Get up \n")
        if decision_1 == "1":
            addpoint()
            if randint(0, 9) == 0:
                print("This is awkward... you found the secret ending.")
            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        if decision_1 == "2": 
            addpoint()
            print("It's dead... that's odd. You're certain you plugged it in before going to sleep.")
            decision: str = input("What would you like to do? \n1. Get up \n2. Go back to sleep\n")
            if decision == "1": 
                addpoint()
                print("You sit up and hear a light jangling noise. Upon looking down, you realize you're chained to the bed.")
                decision_2 = input("What would you like to do? \n1. Panic \n2. Call out for help \n3. Investigate surroundings further\n")
                if decision_2 == "1": 
                    print("You start to furiously claw and scream, trying as hard as you can to take the shackle off.")
                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                    decision_3 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                    if decision_3 == "1":
                        addpoint()
                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "2": 
                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "3": 
                        addpoint()
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The figure rushses at you and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_2 == "2": 
                    addpoint()
                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                    decision_3 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                    if decision_3 == "1":
                        addpoint()
                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "2": 
                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "3": 
                        addpoint()
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The figure rushses at you and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_2 == "3": 
                    addpoint()
                    print("As you look around, a few things come into focus:")
                    print("The chain around your leg has a padlock on it, and has about four feet of slack")
                    print("There is a window with a crack in the glass. It has bars over it, but one bar is missing. \nIf one more was gone, perhaps you could escape through there.")
                    print("Next to you is a nightstand with a lamp.")
                    print("on the far side of the room, there is a door with no lock. Beyond it you can hear faint mumbling")
                    print("There is a desk and chair with papers on it")
                    decision_3 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Check the desk for clues\n")
                    if decision_3 == "1":
                        addpoint()
                        print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                        print("The light gets the attention of something beyond the door. A figure burts into the room.")
                        print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                        print("In his right hand, you notice he's holding a massive axe.")
                        decision_4 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                        if decision_4 == "1":
                            addpoint()
                            print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "2": 
                            print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "3": 
                            addpoint()
                            print("You curse like you've never cursed before, but the words have no effect.")
                            print("The man rushses at you and lunges with the axe held high above its head.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "2": 
                        print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                        print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                        decision_4 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                        if decision_4 == "1":
                            addpoint()
                            print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "2": 
                            print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "3": 
                            addpoint()
                            print("You curse like you've never cursed before, but the words have no effect.")
                            print("The figure rushses at you and lunges with the object held high above its head.")
                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_3 == "3": 
                        addpoint()
                        print("You get off the bed, and can barely manage to get the desk with the four feet granted by your chain")
                        print("On the desk, the papers written are unreadable in the dark")
                        print("You notice a small penlight on the desk")
                        decision_4 = input("What would you like to do? \n1. Turn on the penlight and read the papers \n2. Check the drawers of the desk \n3. Leave the desk")
                        if decision_4 == "1": 
                            addpoint()
                            print("You begin to read the messages on the desk, and are instantly filled with a sense of dread.")
                            print("The writings vary from prayers to god, written wills, or just drawings of terrifying monsters.")
                            print("One thing is clear. Other people have been in the same situation as you, and they were scared.")
                            decision_5 = input("What would you like to do? \n1. Check the drawers of the desk \n2. Leave the desk\n")
                            if decision_5 == "1":
                                addpoint()
                                print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                print("You put these in your pocket")
                                print("The bottom drawer is locked shut")
                                print("You then turn from the desk")
                                decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                                if decision_6 == "1": 
                                    addpoint()
                                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        addpoint()
                                        print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2":
                                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                    decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        addpoint()
                                        print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The figure rushses at you and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "3": 
                                    addpoint()
                                    print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                    print("The door and window are too far to reach with the chain on your leg")
                                    print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                    decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                    if decision_7 == "1" or decision_7 == "2":
                                        print("As you drag the bed, it makes a tremendous scratching noise!")
                                        print("You get the attention of something beyond the door")
                                        print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                        print("In his right hand, you notice he's holding a massive axe.")
                                        decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                        if decision_8 == "1":
                                            addpoint()
                                            print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "2": 
                                            addpoint()
                                            print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "3": 
                                            addpoint()
                                            print("You curse like you've never cursed before, but the words have no effect.")
                                            print("The man rushses at you and lunges with the axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3":
                                        addpoint()
                                        print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                        decision_8 = input("What would you like to do? \n1. Try keys on cuffs and locked drawer")
                                        if decision_8 == "1":
                                            addpoint()
                                            print("The cuffs open!")
                                            print("You find a bloody letter. You put it in your pocket.")
                                            decision_9 = input("What would you like to do? \n1. Remove bar from window with file \n2. Wedge the chair in front of the door \n")
                                            if decision_9 == "1":
                                                print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                print("After about 45 seconds, you feel a presence watching you.")
                                                print("The last thing you see after turning around is an axe falling towards your skull.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                            if decision_9 == "2": 
                                                addpoint()
                                                print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                decision_10 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                                if decision_10 == "1": 
                                                    addpoint()
                                                    print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                    print("Whatever is on the other side of the door has noticed")
                                                    print("As it tries to break down the door, you file like your life depends on it")
                                                    print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                    print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                    print(f"Game over. You managed to finish with {points} points.")
                            if decision_5 == "2": 
                                print("You turn from the desk.") 
                                decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                                if decision_6 == "1": 
                                    addpoint()
                                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2":
                                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                    decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The figure rushses at you and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "3": 
                                    addpoint()
                                    print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                    print("The door and window are too far to reach with the chain on your leg")
                                    print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                    decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                    if decision_7 == "1" or decision_7 == "2":
                                        print("As you drag the bed, it makes a tremendous scratching noise!")
                                        print("You get the attention of something beyond the door")
                                        print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                        print("In his right hand, you notice he's holding a massive axe.")
                                        decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                        if decision_8 == "1":
                                            addpoint()
                                            print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "2": 
                                            print("You look for something to use, and decide upon the lamp. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "3": 
                                            addpoint()
                                            print("You curse like you've never cursed before, but the words have no effect.")
                                            print("The man rushses at you and lunges with the axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3":
                                        addpoint()
                                        print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                        decision_8 = input("What would you like to do? \n1. Try keys on cuffs \n2. Search drawers in desk\n")
                                        if decision_8 == "1":
                                            addpoint()
                                            print("The cuffs open!")
                                            decision_9 = input("What would you like to do? \n1. Search drawers in desk \n2. Wedge the chair in front of the door \n")
                                            if decision_9 == "1":
                                                addpoint()
                                                print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                                print("You put these in your pocket")
                                                print("The bottom drawer is locked shut")
                                                decision_10 = input("What would you like to do? \n1. Try key on locked drawer \n2. Wedge the chair in front of the door \n3. Remove bar from window with file\n")
                                                if decision_10 == "1": 
                                                    print("It works!")
                                                    print("You find a bloody letter. You put it in your pocket.")
                                                    decision_11 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file\n")
                                                    if decision_11 == "1":
                                                        addpoint()
                                                        print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                        decision_12 = input("What would you like to do? \n 1. Remove bar from window with file\n")
                                                        if decision_12 == "1": 
                                                            addpoint()
                                                            print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                            print("Whatever is on the other side of the door has noticed")
                                                            print("As it tries to break down the door, you file like your life depends on it")
                                                            print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                            print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                            print(f"Game over. You managed to finish with {points} points.")
                                                    if decision_11 == "2":
                                                        print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                        print("After about 45 seconds, you feel a presence watching you.")
                                                        print("The last thing you see after turning around is an axe falling towards your skull.")
                                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                                if decision_10 == "2": 
                                                    addpoint()
                                                    print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                    decision_11 = input("What would you like to do? \n1. Remove bar from window with file\n2. Try key on locked drawer")
                                                    if decision_11 == "1": 
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                                    if decision_11 == "2": 
                                                        addpoint()
                                                        print("It works!")
                                                        print("You find a bloody letter. You put it in your pocket.")
                                                        decision_12 = input("What would you like to do? \n1. Remove bar from window with file \n")
                                                        if decision_12 == "1": 
                                                            print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                            print("Whatever is on the other side of the door has noticed")
                                                            print("As it tries to break down the door, you file like your life depends on it")
                                                            print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                            print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                            print(f"Game over. You managed to finish with {points} points.")
                                                if decision_10 == "3": 
                                                    print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                    print("After about 45 seconds, you feel a presence watching you.")
                                                    print("The last thing you see after turning around is an axe falling towards your skull.")
                                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                            if decision_9 == "2": 
                                                addpoint()
                                                print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                decision_10 = input("What would you like to do?\n1. Search drawers in the desk")
                                                if decision_10 == "1": 
                                                    print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                                    print("You put these in your pocket")
                                                    print("The bottom drawer is locked shut")
                                                    decision_11 = input("What would you like to do? \n1. Try key on locked drawer \n2. Remove bar from window with file\n")
                                                    if decision_11 == "1": 
                                                        addpoint()
                                                        print("It works!")
                                                        print("You find a bloody letter. You put it in your pocket.")
                                                        decision_12 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                                        if decision_12 == "1":
                                                            addpoint()
                                                            print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                            print("Whatever is on the other side of the door has noticed")
                                                            print("As it tries to break down the door, you file like your life depends on it")
                                                            print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                            print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                            print(f"Game over. You managed to finish with {points} points.")
                                                    if decision_11 == "2": 
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                        if decision_8 == "2": 
                                            addpoint()
                                            print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                            print("You put these in your pocket")
                                            print("The bottom drawer is locked shut")
                                            decision_9 = input("What would you like to do? \n1. Try keys on cuffs and drawer")
                                            if decision_9 == "1": 
                                                addpoint()
                                                print("The cuffs open!")
                                                print("You then use your keys on the bottom drawer, which opens. It holds a bloodly letter.")
                                                decision_10 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file\n")
                                                if decision_10 == "1": 
                                                    addpoint()
                                                    print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                    decision_11 = input("What would you like to do? \n 1. Remove bar from window with file\n")
                                                    if decision_11 == "1": 
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                                if decision_10 == "2": 
                                                    print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                    print("After about 45 seconds, you feel a presence watching you.")
                                                    print("The last thing you see after turning around is an axe falling towards your skull.")
                                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "2": 
                            addpoint()
                            print("As you shuffle through the drawers, you find a letteropener  and a file.")
                            print("You put these in your pocket")
                            print("The bottom drawer is locked shut")
                            decision_5 = input("What would you like do? \n1. Turn on the penlight and read the papers \n2. Leave the desk \n")
                            if decision_5 == "1": 
                                addpoint()
                                print("You begin to read the messages on the desk, and are instantly filled with a sense of dread.")
                                print("The writings vary from prayers to god, written wills, or just drawings of terrifying monsters.")
                                print("One thing is clear. Other people have been in the same situation as you, and they were scared.")
                                decision_5 = input("What would you like to do? \n1. Leave the desk\n")
                                if decision_5 == "1": 
                                    print("You turn from the desk.") 
                                    decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                                    if decision_6 == "1": 
                                        addpoint()
                                        print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                        print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                        print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                        print("In his right hand, you notice he's holding a massive axe.")
                                        decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                        if decision_7 == "1":
                                            addpoint()
                                            print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_7 == "2": 
                                            print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_7 == "3": 
                                            addpoint()
                                            print("You curse like you've never cursed before, but the words have no effect.")
                                            print("The man rushses at you and lunges with the axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_6 == "2":
                                        print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                        print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                        decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                        if decision_7 == "1":
                                            addpoint()
                                            print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_7 == "2": 
                                            print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_7 == "3": 
                                            addpoint()
                                            print("You curse like you've never cursed before, but the words have no effect.")
                                            print("The figure rushses at you and lunges with the object held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_6 == "3": 
                                        print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                        print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                        print("The door and window are too far to reach with the chain on your leg")
                                        print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                        decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                        if decision_7 == "1" or decision_7 == "2":
                                            print("As you drag the bed, it makes a tremendous scratching noise!")
                                            print("You get the attention of something beyond the door")
                                            print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                            print("In his right hand, you notice he's holding a massive axe.")
                                            decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                            if decision_8 == "1":
                                                addpoint()
                                                print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                            if decision_8 == "2": 
                                                print("You look for something to use, and decide upon the lamp. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                            if decision_8 == "3": 
                                                addpoint()
                                                print("You curse like you've never cursed before, but the words have no effect.")
                                                print("The man rushses at you and lunges with the axe held high above its head.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_7 == "3":
                                            addpoint()
                                            print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                            decision_8 = input("What would you like to do? \n1. Try keys on cuffs and locked drawer \n")
                                            if decision_8 == "1":
                                                addpoint()
                                                print("The cuffs open!")
                                                print("You find a bloody letter. You put it in your pocket.")
                                                decision_9 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file")
                                                if decision_9 == "1": 
                                                    print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                    decision_10 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                                    if decision_10 == "1":
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                                if decision_9 == "2": 
                                                    print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                    print("After about 45 seconds, you feel a presence watching you.")
                                                    print("The last thing you see after turning around is an axe falling towards your skull.")
                                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_5 == "2": 
                                print("You turn from the desk.") 
                                decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help\n")
                                if decision_6 == "1": 
                                    addpoint()
                                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2":
                                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                    decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The figure rushses at you and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_4 == "3":
                            print("You turn from the desk.") 
                            decision_5 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help")
                            if decision_5 == "1": 
                                addpoint()
                                print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                print("In his right hand, you notice he's holding a massive axe.")
                                decision_6 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                if decision_6 == "1":
                                    addpoint()
                                    print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2": 
                                    print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The man rushses at you and lunges with the axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_5 == "2":
                                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                decision_6 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                if decision_6 == "1":
                                    addpoint()
                                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2": 
                                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The figure rushses at you and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
            if decision == "2": 
                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        if decision_1 == "3": 
            addpoint()
            print("You sit up and hear a light jangling noise. Upon looking down, you realize you're chained to the bed.")
            decision_2 = input("What would you like to do? \n1. Panic \n2. Call out for help \n3. Investigate surroundings further\n")
            if decision_2 == "1": 
                print("You start to furiously claw and scream, trying as hard as you can to take the shackle off.")
                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                decision_3 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                if decision_3 == "1":
                    addpoint()
                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    addpoint()
                    print("You curse like you've never cursed before, but the words have no effect.")
                    print("The figure rushses at you and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
            if decision_2 == "2": 
                addpoint()
                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                decision_3 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                if decision_3 == "1":
                    addpoint()
                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    addpoint()
                    print("You curse like you've never cursed before, but the words have no effect.")
                    print("The figure rushses at you and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
            if decision_2 == "3": 
                addpoint()
                print("As you look around, a few things come into focus:")
                print("The chain around your leg has a padlock on it, and has about four feet of slack")
                print("There is a window with a crack in the glass. It has bars over it, but one bar is missing. \nIf one more was gone, perhaps you could escape through there.")
                print("Next to you is a nightstand with a lamp.")
                print("on the far side of the room, there is a door with no lock. Beyond it you can hear faint mumbling")
                print("There is a desk and chair with papers on it")
                decision_3 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Check the desk for clues\n")
                if decision_3 == "1":
                    addpoint()
                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                    print("In his right hand, you notice he's holding a massive axe.")
                    decision_4 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                    if decision_4 == "1":
                        addpoint()
                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "2": 
                        print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "3": 
                        addpoint()
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The man rushses at you and lunges with the axe held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                    decision_4 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                    if decision_4 == "1":
                        addpoint()
                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "2": 
                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "3": 
                        addpoint()
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The figure rushses at you and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    addpoint()
                    print("You get off the bed, and can barely manage to get the desk with the four feet granted by your chain")
                    print("On the desk, the papers written are unreadable in the dark")
                    print("You notice a small penlight on the desk")
                    decision_4 = input("What would you like to do? \n1. Turn on the penlight and read the papers \n2. Check the drawers of the desk \n3. Leave the desk")
                    if decision_4 == "1": 
                        addpoint()
                        print("You begin to read the messages on the desk, and are instantly filled with a sense of dread.")
                        print("The writings vary from prayers to god, written wills, or just drawings of terrifying monsters.")
                        print("One thing is clear. Other people have been in the same situation as you, and they were scared.")
                        decision_5 = input("What would you like to do? \n1. Check the drawers of the desk \n2. Leave the desk\n")
                        if decision_5 == "1":
                            addpoint()
                            print("As you shuffle through the drawers, you find a letteropener  and a file.")
                            print("You put these in your pocket")
                            print("The bottom drawer is locked shut")
                            print("You then turn from the desk")
                            decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                            if decision_6 == "1": 
                                addpoint()
                                print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                print("In his right hand, you notice he's holding a massive axe.")
                                decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    addpoint()
                                    print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The man rushses at you and lunges with the axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2":
                                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    addpoint()
                                    print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The figure rushses at you and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                addpoint()
                                print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                print("The door and window are too far to reach with the chain on your leg")
                                print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                if decision_7 == "1" or decision_7 == "2":
                                    print("As you drag the bed, it makes a tremendous scratching noise!")
                                    print("You get the attention of something beyond the door")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_8 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "2": 
                                        addpoint()
                                        print("You pull out the letter opener and manage to stab the man once in the side. Unfortunately, the wound he deals to you in that time proves to be much more fatal.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3":
                                    addpoint()
                                    print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                    decision_8 = input("What would you like to do? \n1. Try keys on cuffs and locked drawer")
                                    if decision_8 == "1":
                                        addpoint()
                                        print("The cuffs open!")
                                        print("You find a bloody letter. You put it in your pocket.")
                                        decision_9 = input("What would you like to do? \n1. Remove bar from window with file \n2. Wedge the chair in front of the door \n")
                                        if decision_9 == "1":
                                            print("While you try to file away at the bar, you begin to create a lot of noise.")
                                            print("After about 45 seconds, you feel a presence watching you.")
                                            print("The last thing you see after turning around is an axe falling towards your skull.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_9 == "2": 
                                            addpoint()
                                            print("You quietly wedge the chair under the door handle. Effectively locking it")
                                            decision_10 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                            if decision_10 == "1": 
                                                addpoint()
                                                print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                print("Whatever is on the other side of the door has noticed")
                                                print("As it tries to break down the door, you file like your life depends on it")
                                                print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                print(f"Game over. You managed to finish with {points} points.")
                        if decision_5 == "2": 
                            print("You turn from the desk.") 
                            decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                            if decision_6 == "1": 
                                addpoint()
                                print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                print("In his right hand, you notice he's holding a massive axe.")
                                decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The man rushses at you and lunges with the axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2":
                                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The figure rushses at you and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                addpoint()
                                print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                print("The door and window are too far to reach with the chain on your leg")
                                print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                if decision_7 == "1" or decision_7 == "2":
                                    print("As you drag the bed, it makes a tremendous scratching noise!")
                                    print("You get the attention of something beyond the door")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_8 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "2": 
                                        print("You look for something to use, and decide upon the lamp. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3":
                                    addpoint()
                                    print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                    decision_8 = input("What would you like to do? \n1. Try keys on cuffs \n2. Search drawers in desk\n")
                                    if decision_8 == "1":
                                        addpoint()
                                        print("The cuffs open!")
                                        decision_9 = input("What would you like to do? \n1. Search drawers in desk \n2. Wedge the chair in front of the door \n")
                                        if decision_9 == "1":
                                            addpoint()
                                            print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                            print("You put these in your pocket")
                                            print("The bottom drawer is locked shut")
                                            decision_10 = input("What would you like to do? \n1. Try key on locked drawer \n2. Wedge the chair in front of the door \n3. Remove bar from window with file\n")
                                            if decision_10 == "1": 
                                                addpoint()
                                                print("It works!")
                                                print("You find a bloody letter. You put it in your pocket.")
                                                decision_11 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file\n")
                                                if decision_11 == "1":
                                                    addpoint()
                                                    print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                    decision_12 = input("What would you like to do? \n 1. Remove bar from window with file\n")
                                                    if decision_12 == "1": 
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                                if decision_11 == "2":
                                                    print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                    print("After about 45 seconds, you feel a presence watching you.")
                                                    print("The last thing you see after turning around is an axe falling towards your skull.")
                                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                            if decision_10 == "2": 
                                                addpoint()
                                                print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                decision_11 = input("What would you like to do? \n1. Remove bar from window with file\n2. Try key on locked drawer")
                                                if decision_11 == "1": 
                                                    addpoint()
                                                    print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                    print("Whatever is on the other side of the door has noticed")
                                                    print("As it tries to break down the door, you file like your life depends on it")
                                                    print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                    print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                    print(f"Game over. You managed to finish with {points} points.")
                                                if decision_11 == "2": 
                                                    addpoint()
                                                    print("It works!")
                                                    print("You find a bloody letter. You put it in your pocket.")
                                                    decision_12 = input("What would you like to do? \n1. Remove bar from window with file \n")
                                                    if decision_12 == "1": 
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                            if decision_10 == "3": 
                                                print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                print("After about 45 seconds, you feel a presence watching you.")
                                                print("The last thing you see after turning around is an axe falling towards your skull.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_9 == "2": 
                                            addpoint()
                                            print("You quietly wedge the chair under the door handle. Effectively locking it")
                                            decision_10 = input("What would you like to do?\n1. Search drawers in the desk")
                                            if decision_10 == "1": 
                                                addpoint()
                                                print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                                print("You put these in your pocket")
                                                print("The bottom drawer is locked shut")
                                                decision_11 = input("What would you like to do? \n1. Try key on locked drawer \n2. Remove bar from window with file\n")
                                                if decision_11 == "1": 
                                                    addpoint()
                                                    print("It works!")
                                                    print("You find a bloody letter. You put it in your pocket.")
                                                    decision_12 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                                    if decision_12 == "1":
                                                        addpoint()
                                                        print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                        print("Whatever is on the other side of the door has noticed")
                                                        print("As it tries to break down the door, you file like your life depends on it")
                                                        print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                        print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                        print(f"Game over. You managed to finish with {points} points.")
                                                if decision_11 == "2": 
                                                    addpoint()
                                                    print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                    print("Whatever is on the other side of the door has noticed")
                                                    print("As it tries to break down the door, you file like your life depends on it")
                                                    print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                    print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                    print(f"Game over. You managed to finish with {points} points.")
                                    if decision_8 == "2": 
                                        addpoint()
                                        print("As you shuffle through the drawers, you find a letteropener  and a file.")
                                        print("You put these in your pocket")
                                        print("The bottom drawer is locked shut")
                                        decision_9 = input("What would you like to do? \n1. Try keys on cuffs and drawer")
                                        if decision_9 == "1": 
                                            addpoint()
                                            print("The cuffs open!")
                                            print("You then use your keys on the bottom drawer, which opens. It holds a bloodly letter.")
                                            decision_10 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file\n")
                                            if decision_10 == "1": 
                                                print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                decision_11 = input("What would you like to do? \n 1. Remove bar from window with file\n")
                                                if decision_11 == "1": 
                                                    addpoint()
                                                    print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                    print("Whatever is on the other side of the door has noticed")
                                                    print("As it tries to break down the door, you file like your life depends on it")
                                                    print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                    print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                    print(f"Game over. You managed to finish with {points} points.")
                                            if decision_10 == "2": 
                                                print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                print("After about 45 seconds, you feel a presence watching you.")
                                                print("The last thing you see after turning around is an axe falling towards your skull.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "2": 
                        addpoint()
                        print("As you shuffle through the drawers, you find a letteropener  and a file.")
                        print("You put these in your pocket")
                        print("The bottom drawer is locked shut")
                        decision_5 = input("What would you like do? \n1. Turn on the penlight and read the papers \n2. Leave the desk \n")
                        if decision_5 == "1": 
                            print("You begin to read the messages on the desk, and are instantly filled with a sense of dread.")
                            print("The writings vary from prayers to god, written wills, or just drawings of terrifying monsters.")
                            print("One thing is clear. Other people have been in the same situation as you, and they were scared.")
                            decision_5 = input("What would you like to do? \n1. Leave the desk\n")
                            if decision_5 == "1": 
                                print("You turn from the desk.") 
                                decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                                if decision_6 == "1": 
                                    addpoint()
                                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "2":
                                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                    decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                    if decision_7 == "1":
                                        addpoint()
                                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "2": 
                                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3": 
                                        addpoint()
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The figure rushses at you and lunges with the object held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_6 == "3": 
                                    print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                    print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                    print("The door and window are too far to reach with the chain on your leg")
                                    print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                    decision_7 = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                    if decision_7 == "1" or decision_7 == "2":
                                        print("As you drag the bed, it makes a tremendous scratching noise!")
                                        print("You get the attention of something beyond the door")
                                        print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                        print("In his right hand, you notice he's holding a massive axe.")
                                        decision_8 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                        if decision_8 == "1":
                                            addpoint()
                                            print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "2": 
                                            print("You look for something to use, and decide upon the lamp. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                        if decision_8 == "3": 
                                            addpoint()
                                            print("You curse like you've never cursed before, but the words have no effect.")
                                            print("The man rushses at you and lunges with the axe held high above its head.")
                                            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_7 == "3":
                                        print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                        decision_8 = input("What would you like to do? \n1. Try keys on cuffs and locked drawer \n")
                                        if decision_8 == "1":
                                            print("The cuffs open!")
                                            print("You find a bloody letter. You put it in your pocket.")
                                            decision_9 = input("What would you like to do? \n1. Wedge the chair in front of the door \n2. Remove bar from window with file")
                                            if decision_9 == "1": 
                                                print("You quietly wedge the chair under the door handle. Effectively locking it")
                                                decision_10 = input("What would you like to do? \n1. Remove bar from window with file\n")
                                                if decision_10 == "1":
                                                    print("As you attempt to file away at the bar, you begin making a great deal of noise")
                                                    print("Whatever is on the other side of the door has noticed")
                                                    print("As it tries to break down the door, you file like your life depends on it")
                                                    print("Just as you get close, you see the blade of an axe come through the door. You have moments left")
                                                    print("Just as the door is broken down, and you see a broken, bloody, and deformed man holding an axe run into the room, \n you escape.")
                                                    print(f"Game over. You managed to finish with {points} points.")
                                            if decision_9 == "2": 
                                                print("While you try to file away at the bar, you begin to create a lot of noise.")
                                                print("After about 45 seconds, you feel a presence watching you.")
                                                print("The last thing you see after turning around is an axe falling towards your skull.")
                                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_5 == "2": 
                            print("You turn from the desk.") 
                            decision_6 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help")
                            if decision_6 == "1": 
                                addpoint()
                                print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                print("In his right hand, you notice he's holding a massive axe.")
                                decision_7 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The man rushses at you and lunges with the axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2":
                                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                decision_7 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                if decision_7 == "1":
                                    addpoint()
                                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    addpoint()
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The figure rushses at you and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "3":
                        print("You turn from the desk.") 
                        decision_5 = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help")
                        if decision_5 == "1": 
                            addpoint()
                            print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                            print("The light gets the attention of something beyond the door. A figure burts into the room.")
                            print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                            print("In his right hand, you notice he's holding a massive axe.")
                            decision_6 = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                            if decision_6 == "1":
                                addpoint()
                                print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2": 
                                print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                addpoint()
                                print("You curse like you've never cursed before, but the words have no effect.")
                                print("The man rushses at you and lunges with the axe held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_5 == "2":
                            print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                            print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                            decision_6 = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                            if decision_6 == "1":
                                addpoint()
                                print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2": 
                                print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                addpoint()
                                print("You curse like you've never cursed before, but the words have no effect.")
                                print("The figure rushses at you and lunges with the object held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        try_again = input("Would you like to try again? \nYes or No?\n")


def addpoint() -> None:
    """Adds points!"""
    global points 
    global difficulty
    global player
    points = int(difficulty) + points + len(player)
    print(f"{player}, you currently have {points} points")


def chances(points: int) -> int:
    """Chance of Success."""
    global player
    points = 0
    print(f"Before we start, let's take a look at your chances for actually beating this with a totally accurate method, {player}.")
    food: str = input("What's your favorite food? ")
    if len(food) > 4: 
        print("Wow, looks like you have a pretty good chance!")
    else: 
        print("Yeah... you're gonna need some help. Don't worry, I'll add some points on now.")
    addpoint()
    return points


if __name__ == "__main__": 
    main()