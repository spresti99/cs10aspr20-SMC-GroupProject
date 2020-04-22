"""
   Miranda Lassar and Sonia Presti and Charisma Chauhan storybook_app.py is an app for stories in the terminal
   it is also used as a module in the storybook_webapp flask app

"""
def split(word):
    return list(word)

def welcome(name):
    newName = split(name)
    for y in range(0, len(newName)):
        if newName[y] == 'a' or newName[y] == 'A':
            print('  _______ \n |   _   | \n |  |_|  | \n |       | \n |       | \n |   _   | \n |__| |__|')
        if newName[y] == 'b' or newName[y] == 'B':
            print(' _______ \n| |_|   |\n|       |\n|  _   |\n| |_|   |\n|_______|')
        if newName[y] == 'c' or newName[y] == 'C':
            print(' _______\n|       |\n|       |\n|       |\n|      _|\n|     |_ \n|_______|')
        if newName[y] == 'd' or newName[y] == 'D':
            print(' ______  \n|      | \n|  _    |\n| | |   |\n| |_|   |\n|       |\n|______|')
        if newName[y] == 'e' or newName[y] == 'E':
            print(' _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |___ \n|_______|')
        if newName[y] == 'f' or newName[y] == 'F':
            print(' _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |    \n|___|    ')
        if newName[y] == 'g' or newName[y] == 'G':
            print(' _______ \n|       |\n|    ___|\n|   | __ \n|   ||  |\n|   |_| |\n|_______|')
        if newName[y] == 'h' or newName[y] == 'H':
            print(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n|   _   |\n|__| |__|')
        if newName[y] == 'i' or newName[y] == 'I':
            print(' ___  \n|   | \n|   | \n|   | \n|   | \n|   | \n|___| ')
        if newName[y] == 'j' or newName[y] == 'J':
            print('     ___ \n    |   |\n    |   |\n    |   |\n ___|   |\n|       |\n|_______|')
        if newName[y] == 'k' or newName[y] == 'K':
            print(' ___   _ \n|   | | |\n|   |_| |\n|      _|\n|     |_ \n|    _  |\n|___| |_|')
        if newName[y] == 'l' or newName[y] == 'L':
            print(' ___     \n|   |    \n|   |    \n|   |    \n|   |___ \n|       |\n|_______|')
        if newName[y] == 'm' or newName[y] == 'M':
            print(' __   __ \n|  |_|  |\n|       |\n|       |\n|       |\n| ||_|| |\n|_|   |_|')
        if newName[y] == 'n' or newName[y] == 'n':
            print(' __    _ \n|  |  | |\n|   |_| |\n|       |\n|  _    |\n| | |   |\n|_|  |__|')
        if newName[y] == 'o' or newName[y] == 'O':
            print(' _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|       |\n|_______|')
        if newName[y] == 'p' or newName[y] == 'P':
            print(' _______ \n|       |\n|    _  |\n|   |_| |\n|    ___|\n|   |    \n|___|    ')
        if newName[y] == 'q' or newName[y] == 'Q':
            print(' _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|      | \n|____||_|')
        if newName[y] == 'r' or newName[y] == 'R':
            print(' ______   \n|    _ |  \n|   | ||  \n|   |_||_ \n|    __  |\n|   |  | |\n|___|  |_|')
        if newName[y] == 's' or newName[y] == 'S':
            print(' _______ \n|       |\n|  _____|\n| |_____ \n|_____  |\n _____| |\n|_______|')
        if newName[y] == 't' or newName[y] == 'T':
            print(' _______ \n|       |\n|_     _|\n  |   |  \n  |   |  \n  |   |  \n  |___|  ')
        if newName[y] == 'u' or newName[y] == 'U':
            print(' __   __ \n|  | |  |\n|  | |  |\n|  |_|  |\n|       |\n|       |\n|_______|')
        if newName[y] == 'v' or newName[y] == 'V':
            print(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n |     | \n  |___|  ')
        if newName[y] == 'w' or newName[y] == 'W':
            print(' _     _ \n| | _ | |\n| || || |\n|       |\n|       |\n|   _   |\n|__| |__|')
        if newName[y] == 'x' or newName[y] == 'X':
            print(' __   __ \n|  |_|  |\n|       |\n|       |\n |     | \n|   _   |\n|__| |__|')
        if newName[y] == 'y' or newName[y] == 'Y':
            print(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|_     _|\n  |   |  \n  |___|  ')
        if newName[y] == 'z' or newName[y] == 'Z':
            print(' _______ \n|       |\n|____   |\n ____|  |\n| ______|\n| |_____ \n|_______|')

def intro_story():
    print("Hello! Welcome to your first interactive story!")
    print("Before we begin, we would love to get to know a little bit about you!")
    name = input("What is your name?")
    welcome(name)
    print('Pretty cool, right? This is called ASCII art, and this is how we are going to tell stories!')

def owl_story():
    print("Ollie the Owl's Big Adventure")
    ready = input('Shall we begin?')
    if ready == 'yes' or ready == 'Yes' or ready == 'Y':
        print("Meet Ollie the Owl!")
        print('  /\ /\ \n ((ovo)) \n ():::() \n   VVV')

intro_story()
owl_story()
