"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import storybook_app
app = Flask(__name__)

global state
state = {'message':[]}

@app.route('/')
@app.route('/main')
def main():
	return render_template('storybook.html')

@app.route('/story1',methods=['GET','POST'])
def story1():

	global state
	#if request.method == 'GET':
		#return welcome()

	if request.method == 'POST':
		name = request.form['name']
		welcome(name)
	return render_template('story1.html')
	#def split(word):
		#return list(word)

	def welcome(name):
		global state
		newName = split(name)
		for y in range(0, len(newName)):
			if newName[y] == 'a' or newName[y] == 'A':
				state['message']+=('  _______ \n |   _   | \n |  |_|  | \n |       | \n |       | \n |   _   | \n |__| |__|')
			if newName[y] == 'b' or newName[y] == 'B':
				state['message']+=(' _______ \n| |_|   |\n|       |\n|  _   |\n| |_|   |\n|_______|')
			if newName[y] == 'c' or newName[y] == 'C':
				state['message']+=(' _______\n|       |\n|       |\n|       |\n|      _|\n|     |_ \n|_______|')
			if newName[y] == 'd' or newName[y] == 'D':
				state['message']+=(' ______  \n|      | \n|  _    |\n| | |   |\n| |_|   |\n|       |\n|______|')
			if newName[y] == 'e' or newName[y] == 'E':
				state['message']+=(' _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |___ \n|_______|')
			if newName[y] == 'f' or newName[y] == 'F':
				state['message']+=(' _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |    \n|___|    ')
			if newName[y] == 'g' or newName[y] == 'G':
				state['message']+=(' _______ \n|       |\n|    ___|\n|   | __ \n|   ||  |\n|   |_| |\n|_______|')
			if newName[y] == 'h' or newName[y] == 'H':
				state['message']+=(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n|   _   |\n|__| |__|')
			if newName[y] == 'i' or newName[y] == 'I':
				state['message']+=(' ___  \n|   | \n|   | \n|   | \n|   | \n|   | \n|___| ')
			if newName[y] == 'j' or newName[y] == 'J':
				state['message']+=('     ___ \n    |   |\n    |   |\n    |   |\n ___|   |\n|       |\n|_______|')
			if newName[y] == 'k' or newName[y] == 'K':
				state['message']+=(' ___   _ \n|   | | |\n|   |_| |\n|      _|\n|     |_ \n|    _  |\n|___| |_|')
			if newName[y] == 'l' or newName[y] == 'L':
				state['message']+=(' ___     \n|   |    \n|   |    \n|   |    \n|   |___ \n|       |\n|_______|')
			if newName[y] == 'm' or newName[y] == 'M':
				state['message']+=(' __   __ \n|  |_|  |\n|       |\n|       |\n|       |\n| ||_|| |\n|_|   |_|')
			if newName[y] == 'n' or newName[y] == 'n':
				state['message']+=(' __    _ \n|  |  | |\n|   |_| |\n|       |\n|  _    |\n| | |   |\n|_|  |__|')
			if newName[y] == 'o' or newName[y] == 'O':
				state['message']+=(' _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|       |\n|_______|')
			if newName[y] == 'p' or newName[y] == 'P':
				state['message']+=(' _______ \n|       |\n|    _  |\n|   |_| |\n|    ___|\n|   |    \n|___|    ')
			if newName[y] == 'q' or newName[y] == 'Q':
				state['message']+=(' _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|      | \n|____||_|')
			if newName[y] == 'r' or newName[y] == 'R':
				state['message']+=(' ______   \n|    _ |  \n|   | ||  \n|   |_||_ \n|    __  |\n|   |  | |\n|___|  |_|')
			if newName[y] == 's' or newName[y] == 'S':
				state['message']+=(' _______ \n|       |\n|  _____|\n| |_____ \n|_____  |\n _____| |\n|_______|')
			if newName[y] == 't' or newName[y] == 'T':
				state['message']+=(' _______ \n|       |\n|_     _|\n  |   |  \n  |   |  \n  |   |  \n  |___|  ')
			if newName[y] == 'u' or newName[y] == 'U':
				state['message']+=(' __   __ \n|  | |  |\n|  | |  |\n|  |_|  |\n|       |\n|       |\n|_______|')
			if newName[y] == 'v' or newName[y] == 'V':
				state['message']+=(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n |     | \n  |___|  ')
			if newName[y] == 'w' or newName[y] == 'W':
				state['message']+=(' _     _ \n| | _ | |\n| || || |\n|       |\n|       |\n|   _   |\n|__| |__|')
			if newName[y] == 'x' or newName[y] == 'X':
				state['message']+=(' __   __ \n|  |_|  |\n|       |\n|       |\n |     | \n|   _   |\n|__| |__|')
			if newName[y] == 'y' or newName[y] == 'Y':
				state['message']+=(' __   __ \n|  | |  |\n|  |_|  |\n|       |\n|_     _|\n  |   |  \n  |___|  ')
			if newName[y] == 'z' or newName[y] == 'Z':
				state['message']+=(' _______ \n|       |\n|____   |\n ____|  |\n| ______|\n| |_____ \n|_______|')

@app.route('/story2')
def story2():
	return render_template('story2.html')

@app.route('/story3')
def story3():
	return render_template('story3.html')

@app.route('/about_authors')
def about_authors():
	""" generates a bio page with links and images """
	return render_template('about_authors.html')

@app.route('/miranda')
def miranda():
	""" generates a bio page with links and images """
	return render_template('miranda.html')

@app.route('/sonia')
def sonia():
	""" generates a bio page with links and images """
	return render_template('sonia.html')

@app.route('/charisma')
def charisma():
	""" generates a bio page with links and images """
	return render_template('charisma.html')

@app.route('/about')
def about():
	"""generates an about page with information about the game"""
	return render_template('about.html')

if __name__ == '__main__':
	app.run(port=3000)
