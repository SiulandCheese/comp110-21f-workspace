"""A Self-Led Adventure."""

__author__ = 730383189

points: int = 0
if __name__ == "__main__": 
    def main() -> None:
        """Begins Game."""
        print("You awake in a dark room. You don't know where you are, or how you got there.")
        decision: str = input("What would you like to do? \n1. Go back to sleep \n2. Check phone \n3. Get up \n")
        if decision == "1":
            print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        elif decision == "2": 
            points == points + 1
            print("It's dead... that's odd. You're certain you plugged it in before going to sleep.")
            decision: str = input("What would you like to do? \n1. Get up \n2. Go back to sleep")
            if decision == 1: 
                print("#Insert Result of intial elif 3 here")
            if decision == 2: 
                print(f"Game over! You managed to score a total of {points} points. \nPlay again to try and beat that score!")
        elif decision == "3": 
            points == points + 2
            print("You sit up and hear a light jangling noise. Upon looking down, you realize you're chained to the bed.")
            decision: str = input("What would you like to do? \n1. Panic \n2. Call out for help \n3. Investigate surroundings further\n")
            if decision == "1": 
                print("You start to furiously claw and scream, trying as hard as you can to take the shackle off.")
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
            if decision == "2": 
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
        else: 
            print("Oops! Looks like you didn't enter a choice of 1, 2, or 3. Try again!")
main()