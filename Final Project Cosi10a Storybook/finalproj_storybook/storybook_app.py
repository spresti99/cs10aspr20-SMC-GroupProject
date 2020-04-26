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

if __name__ == "__main__":
	intro_story()
	owl_story()


#the function story2_conditions returns a dictionary of the variables that will be passed to story2.html
def story2_conditions(choices):
	conditions = {}
	if len(choices)==1:
		if choices[0] == "get dressed":
			storytext = "Okay, time to get dressed. Let's pick out a color hat to wear"
			question = "Enter: black or blue or red"
			opt1 = "black"
			opt2 = "blue"
			opt3 = "red"
			pictureUrl = "https://i.imgur.com/acuLNws.jpg"
			options3Display = "display:inline"
			options2Display = "display:none"
			options1Display = "display:none"

		elif choices[0] == "go fishing":
			storytext = "I just grabbed my fishing pole, now I am ready to catch some fish. Tell me when you are ready to cast the line!"
			question = "Enter: ready"
			opt1 = "ready"
			pictureUrl = "https://i.imgur.com/JqzW4Ff.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0] == "go swimming":
			storytext = "I put on my snorkel, now I am ready to jump into the ocean. On the count of 3, let's jump together! 1... 2... 3... JUMP!"
			question = "Enter: jump"
			opt1 = "jump"
			pictureUrl = "https://i.imgur.com/qIEmd9Q.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

	if len(choices)==2:
		if choices[0]=="get dressed" and choices[1] == "blue":
			storytext = "I love this blue hat, thanks for helping me choose to wear it today. I am now ready to go outside and fish!"
			question = "Enter: start fishing"
			opt1 = "start fishing"
			pictureUrl="https://i.imgur.com/TcaBpZU.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0]=="get dressed" and choices[1] == "black":
			storytext = "I love this black hat, thanks for helping me choose to wear it today. I am now ready to go outside and fish!"
			question = "Enter: start fishing"
			opt1 = "start fishing"
			pictureUrl="https://i.imgur.com/IDiSGp2.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0]=="get dressed" and choices[1] == "red":
			storytext = "I love this red hat, thanks for helping me choose to wear it today. I am now ready to go outside and fish!"
			question = "Enter: start fishing"
			opt1 = "start fishing"
			pictureUrl="https://i.imgur.com/sFc1S8p.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0] == "go fishing" and choices[1] == "ready":
			storytext = "I hope to catch a big fish today. Tell me when you are ready to cast the line"
			question = "Enter: ready"
			opt1 = "ready"
			pictureUrl = "https://i.imgur.com/aFscZZG.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0] == "go swimming" and choices[1]=="jump":
			storytext = "SPLASH! Now we can explore underwater. Which friend do you want to visit? Willy the Whale, Fiona the Fish, or Colby the Crab"
			question = "Enter: Willy or Fiona or Colby"
			opt1 = "Willy"
			opt2 = "Fiona"
			opt3 = "Colby"
			pictureUrl = "https://i.imgur.com/8cjaMgB.jpg"
			options3Display = "display:inline"
			options2Display = "display:none"
			options1Display = "display:none"

	if len(choices)==3:
		if choices[0]=="get dressed" and choices[1] == "blue" and choices[2]=="start fishing":
			storytext = "I just grabbed my fishing pole, now I am ready to catch some fish. Tell me when you are ready to cast the line!"
			question = "Enter: ready"
			opt1 = "ready"
			pictureUrl="https://i.imgur.com/iljLO8r.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0]=="get dressed" and choices[1] == "black" and choices[2]=="start fishing":
			storytext = "I just grabbed my fishing pole, now I am ready to catch some fish. Tell me when you are ready to cast the line!"
			question = "Enter: ready"
			opt1 = "ready"
			pictureUrl="https://i.imgur.com/IGWrjOy.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

		elif choices[0]=="get dressed" and choices[1] == "red" and choices[2]=="start fishing":
			storytext = "I just grabbed my fishing pole, now I am ready to catch some fish. Tell me when you are ready to cast the line!"
			question = "Enter: ready"
			opt1 = "ready"
			pictureUrl="https://i.imgur.com/SMe1MD1.jpg"
			options3Display = "display:none"
			options2Display = "display:none"
			options1Display = "display:inline"

#	else:
#		storytext = "What a fun day! Now it is time to go to sleep, goodnight!"

	conditions.update( {'storytext': storytext} )
	conditions.update( {'question': question} )
	conditions.update( {'pictureUrl': pictureUrl} )
	if options3Display=="display:inline":
		conditions.update( {"opt1": opt1} )
		conditions.update( {"opt2": opt2})
		conditions.update( {"opt3": opt3})
	if options2Display=="display:inline":
		conditions.update( {"opt1": opt1} )
		conditions.update( {"opt2": opt2})
	if options1Display=="display:inline":
		conditions.update( {"opt1": opt1} )

	conditions.update( {"options3Display": options3Display})
	conditions.update( {"options2Display": options2Display})
	conditions.update( {"options1Display": options1Display})
	return conditions



#conditions = story2_conditions(choice)


#the get functions below return the string for each of the variables that will be passed to story2.html
def get_storytext(conditions):
	return conditions['storytext']
def get_question(conditions):
	return conditions['question']
def get_pictureUrl(conditions):
	return conditions['pictureUrl']
def get_opt1(conditions):
	return conditions['opt1']
def get_opt2(conditions):
	return conditions['opt2']
def get_opt3(conditions):
	return conditions['opt3']
def get_options3Display(conditions):
	return conditions['options3Display']
def get_options2Display(conditions):
	return conditions['options2Display']
def get_options1Display(conditions):
	return conditions['options1Display']
