"""A Self-Led Adventure."""

__author__ = 730383189

points: int = 0
if __name__ == "__main__": 
    def main() -> None:
        """Begins Game."""
        print("You awake in a dark room. You don't know where you are, or how you got there.")
        decision_1: str = input("What would you like to do? \n1. Go back to sleep \n2. Check phone \n3. Get up \n")
        if decision_1 == "1":
            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        if decision_1 == "2": 
            points == points + 1
            print("It's dead... that's odd. You're certain you plugged it in before going to sleep.")
            decision_2: str = input("What would you like to do? \n1. Get up \n2. Go back to sleep\n")
            if decision_2 == "1": 
                print("#Insert Result of intial elif 3 here")
            if decision_2 == "2": 
                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        if decision_1 == "3": 
            points == points + 2
            print("You sit up and hear a light jangling noise. Upon looking down, you realize you're chained to the bed.")
            decision_2: str = input("What would you like to do? \n1. Panic \n2. Call out for help \n3. Investigate surroundings further\n")
            if decision_2 == "1": 
                print("You start to furiously claw and scream, trying as hard as you can to take the shackle off.")
                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                decision_3: str = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                if decision_3 == "1":
                    points == points + 1
                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    points == points + 2
                    print("You curse like you've never cursed before, but the words have no effect.")
                    print("The figure rushses at you and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
            if decision_2 == "2": 
                points == points + 1
                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                decision_3: str = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                if decision_3 == "1":
                    points == points + 1
                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    points == points + 2
                    print("You curse like you've never cursed before, but the words have no effect.")
                    print("The figure rushses at you and lunges with the object held high above its head.")
                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
            if decision_2 == "3": 
                points == points + 2
                print("As you look around, a few things come into focus:")
                print("The chain around your leg has a padlock on it, and has about four feet of slack")
                print("There is a window with a crack in the glass. It has bars over it, but one bar is missing. \nIf one more was gone, perhaps you could escape through there.")
                print("Next to you is a nightstand with a lamp.")
                print("on the far side of the room, there is a door with no lock. Beyond it you can hear faint mumbling")
                print("There is a desk and chair with papers on it")
                decision_3: str = input("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Check the desk for clues\n")
                if decision_3 == "1":
                    points == points + 1
                    print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                    print("The light gets the attention of something beyond the door. A figure burts into the room.")
                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                    print("In his right hand, you notice he's holding a massive axe.")
                    decision_4: str = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                    if decision_4 == "1":
                        points == points + 1
                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "2": 
                        print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "3": 
                        points == points + 2
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The man rushses at you and lunges with the axe held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "2": 
                    print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                    print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                    decision_4: str = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                    if decision_4 == "1":
                        points == points + 1
                        print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "2": 
                        print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                    if decision_4 == "3": 
                        points == points + 2
                        print("You curse like you've never cursed before, but the words have no effect.")
                        print("The figure rushses at you and lunges with the object held high above its head.")
                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                if decision_3 == "3": 
                    points == points + 2
                    print("You get off the bed, and can barely manage to get the desk with the four feet granted by your chain")
                    print("On the desk, the papers written are unreadable in the dark")
                    print("You notice a small penlight on the desk")
                    decision_4: str = input("What would you like to do? \n1. Turn on the penlight and read the papers \n2. Check the drawers of the desk \n3. Leave the desk")
                    if decision_4 == "1": 
                        print("You begin to read the messages on the desk, and are instantly filled with a sense of dread.")
                        print("The writings vary from prayers to god, written wills, or just drawings of terrifying monsters.")
                        print("One thing is clear. Other people have been in the same situation as you, and they were scared.")
                        decision_5: str = input("What would you like to do? \n1. Check the drawers of the desk \n2. Leave the desk")
                        if decision_5 == "1":
                            print("As you shuffle through the drawers, you find a letteropener  and a file.")
                            print("You put these in your pocket")
                            print("The bottom drawer is locked shut")
                        if decision_5 == "2": 
                            print("You turn from the desk.") 
                            decision_6: str = ("What would you like to do? \n1. Turn on the lamp \n2. Call out for help \n3. Scan the room with the penlight")
                            if decision_6 == "1": 
                                points == points + 1
                                print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("The light gets the attention of something beyond the door. A figure burts into the room.")
                                print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                print("In his right hand, you notice he's holding a massive axe.")
                                decision_7: str = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                if decision_7 == "1":
                                    points == points + 1
                                    print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    points == points + 2
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The man rushses at you and lunges with the axe held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2":
                                print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                                print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                                decision_7: str = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                                if decision_7 == "1":
                                    points == points + 1
                                    print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "2": 
                                    print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3": 
                                    points == points + 2
                                    print("You curse like you've never cursed before, but the words have no effect.")
                                    print("The figure rushses at you and lunges with the object held high above its head.")
                                    print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                print("Once the penlight turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                                print("You also start to get an accurate sense of how far you are from everything else in the room.")
                                print("The door and window are too far to reach with the chain on your leg")
                                print("There is a key on the floor about 10 feet away, in the opposite corner of the room")
                                decision_7: str = input("What do you want to do? \n1. Start dragging the bed behind you to get to the key/door \n2. Start dragging the bed behind you to get to the window \n3. Grab sheets and fashion a rope to grab the key\n")
                                if decision_7 == "1" or decision_7 == "2":
                                    print("As you drag the bed, it makes a tremendous scratching noise!")
                                    print("You get the attention of something beyond the door")
                                    print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                                    print("In his right hand, you notice he's holding a massive axe.")
                                    decision_8: str = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                                    if decision_8 == "1":
                                        points == points + 1
                                        print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "2": 
                                        print("You look for something to use, and decide upon the lamp. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                    if decision_8 == "3": 
                                        points == points + 2
                                        print("You curse like you've never cursed before, but the words have no effect.")
                                        print("The man rushses at you and lunges with the axe held high above its head.")
                                        print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                                if decision_7 == "3":
                                    print("You fashion a rope and throw it into the corner. After three attempts, it works!") 
                                    decision_8: str = input("What would you like to do? \n1. Try keys on cuffs \n2. Try keys on drawer")

                    if decision_4 == "2": 
                        print("As you shuffle through the drawers, you find a letteropener  and a file.")
                        print("You put these in your pocket")
                        print("The bottom drawer is locked shut")
                    if decision_4 == "3":
                        print("You turn from the desk.") 
                        decision_5: str = ("What would you like to do? \n1. Turn on the lamp \n2. Call out for help")
                        if decision_5 == "1": 
                            points == points + 1
                            print("Once the light turns on, your stomach turns. All around the room are what appear to be blood stains, some in horrifying positions.")
                            print("The light gets the attention of something beyond the door. A figure burts into the room.")
                            print("With the light on, you are able to see the figure is a hideously disfigured man, no shorter than 6', but with a spine so bent you he struggles to even look forward.")
                            print("In his right hand, you notice he's holding a massive axe.")
                            decision_6: str = input("What would you like to do? \n1. Ask the man for help \n2. Try fighting him \n3. Curse at him\n")
                            if decision_6 == "1":
                                points == points + 1
                                print("You call out \"Sir! Please free me with your axe!\" to which the man pays no regard. \nHe rushes at you, and lunges with his axe held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "2": 
                                print("You look around and grab the nearest thing you see, the lamp on the bedside table. \nBy the time you turn to face the man again, you barely catch a glimpse of the end of his swing.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision_6 == "3": 
                                points == points + 2
                                print("You curse like you've never cursed before, but the words have no effect.")
                                print("The man rushses at you and lunges with the axe held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                        if decision_5 == "2":
                            print("You scream at the top of your lungs \"Help! Somebody please help me!!\"")
                            print("A looming figure bursts through an unseen door along the far wall of the room, holding something in its hand.")
                            decision: str = input("What would you like to do? \n1. Ask the figure for help \n2. Try fighting the figure \n3. Curse at the figure\n")
                            if decision == "1":
                                points == points + 1
                                print("You call out \"Please help me!\" to which the figure pays no regard. \nIt rushes at you, and lunges with the object held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision == "2": 
                                print("You look around and grab the nearest thing you see, a lamp on the bedside table. \nBy the time you turn to face the figure again, you barely catch a glimpse of the end of its swing.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
                            if decision == "3": 
                                points == points + 2
                                print("You curse like you've never cursed before, but the words have no effect.")
                                print("The figure rushses at you and lunges with the object held high above its head.")
                                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")

main()