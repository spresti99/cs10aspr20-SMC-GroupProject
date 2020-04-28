"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import storybook_app
app = Flask(__name__)

global state

state = {'message':'',
		 'choice':'',
		 'story2_choices':[]}

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
	return render_template('story1.html', state=state)

def split(word):
	return list(word)

def welcome(name):
	global state
	newName = split(name)
	for y in range(0, len(newName)):
		if newName[y] == 'a' or newName[y] == 'A':
			state['message']+=('\n\n  _______ \n |   _   | \n |  |_|  | \n |       | \n |       | \n |   _   | \n |__| |__|')
		if newName[y] == 'b' or newName[y] == 'B':
			state['message']+=('\n\n _______ \n| |_|   |\n|       |\n|  _   |\n| |_|   |\n|_______|')
		if newName[y] == 'c' or newName[y] == 'C':
			state['message']+=('\n\n _______\n|       |\n|       |\n|       |\n|      _|\n|     |_ \n|_______|')
		if newName[y] == 'd' or newName[y] == 'D':
			state['message']+=('\n\n ______  \n|      | \n|  _    |\n| | |   |\n| |_|   |\n|       |\n|______|')
		if newName[y] == 'e' or newName[y] == 'E':
			state['message']+=('\n\n _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |___ \n|_______|')
		if newName[y] == 'f' or newName[y] == 'F':
			state['message']+=('\n\n _______ \n|       |\n|    ___|\n|   |___ \n|    ___|\n|   |    \n|___|    ')
		if newName[y] == 'g' or newName[y] == 'G':
			state['message']+=('\n\n _______ \n|       |\n|    ___|\n|   | __ \n|   ||  |\n|   |_| |\n|_______|')
		if newName[y] == 'h' or newName[y] == 'H':
			state['message']+=('\n\n __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n|   _   |\n|__| |__|')
		if newName[y] == 'i' or newName[y] == 'I':
			state['message']+=('\n\n ___  \n|   | \n|   | \n|   | \n|   | \n|   | \n|___| ')
		if newName[y] == 'j' or newName[y] == 'J':
			state['message']+=('\n\n     ___ \n    |   |\n    |   |\n    |   |\n ___|   |\n|       |\n|_______|')
		if newName[y] == 'k' or newName[y] == 'K':
			state['message']+=('\n\n ___   _ \n|   | | |\n|   |_| |\n|      _|\n|     |_ \n|    _  |\n|___| |_|')
		if newName[y] == 'l' or newName[y] == 'L':
			state['message']+=('\n\n ___     \n|   |    \n|   |    \n|   |    \n|   |___ \n|       |\n|_______|')
		if newName[y] == 'm' or newName[y] == 'M':
			state['message']+=('\n\n __   __ \n|  |_|  |\n|       |\n|       |\n|       |\n| ||_|| |\n|_|   |_|')
		if newName[y] == 'n' or newName[y] == 'n':
			state['message']+=('\n\n __    _ \n|  |  | |\n|   |_| |\n|       |\n|  _    |\n| | |   |\n|_|  |__|')
		if newName[y] == 'o' or newName[y] == 'O':
			state['message']+=('\n\n _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|       |\n|_______|')
		if newName[y] == 'p' or newName[y] == 'P':
			state['message']+=('\n\n _______ \n|       |\n|    _  |\n|   |_| |\n|    ___|\n|   |    \n|___|    ')
		if newName[y] == 'q' or newName[y] == 'Q':
			state['message']+=('\n\n _______ \n|       |\n|   _   |\n|  | |  |\n|  |_|  |\n|      | \n|____||_|')
		if newName[y] == 'r' or newName[y] == 'R':
			state['message']+=('\n\n ______   \n|    _ |  \n|   | ||  \n|   |_||_ \n|    __  |\n|   |  | |\n|___|  |_|')
		if newName[y] == 's' or newName[y] == 'S':
			state['message']+=('\n\n _______ \n|       |\n|  _____|\n| |_____ \n|_____  |\n _____| |\n|_______|')
		if newName[y] == 't' or newName[y] == 'T':
			state['message']+=('\n\n _______ \n|       |\n|_     _|\n  |   |  \n  |   |  \n  |   |  \n  |___|  ')
		if newName[y] == 'u' or newName[y] == 'U':
			state['message']+=('\n\n __   __ \n|  | |  |\n|  | |  |\n|  |_|  |\n|       |\n|       |\n|_______|')
		if newName[y] == 'v' or newName[y] == 'V':
			state['message']+=('\n\n __   __ \n|  | |  |\n|  |_|  |\n|       |\n|       |\n |     | \n  |___|  ')
		if newName[y] == 'w' or newName[y] == 'W':
			state['message']+=('\n\n _     _ \n| | _ | |\n| || || |\n|       |\n|       |\n|   _   |\n|__| |__|')
		if newName[y] == 'x' or newName[y] == 'X':
			state['message']+=('\n\n __   __ \n|  |_|  |\n|       |\n|       |\n |     | \n|   _   |\n|__| |__|')
		if newName[y] == 'y' or newName[y] == 'Y':
			state['message']+=('\n\n __   __ \n|  | |  |\n|  |_|  |\n|       |\n|_     _|\n  |   |  \n  |___|  ')
		if newName[y] == 'z' or newName[y] == 'Z':
			state['message']+=('\n\n _______ \n|       |\n|____   |\n ____|  |\n| ______|\n| |_____ \n|_______|')

@app.route('/story2start')
def story2start():
	storytext = "Hello, my name is Flipper! Today is going to be a great day. What should I do first?"
	question = "Enter: go swimming or go fishing or get dressed"
	pictureUrl = "https://s7d5.turboimg.net/t1/52388300_penguin_iceberg.jpg"
	state['story2_choices'] = []
	audio = "/static/Story2StartML.mp3"

	return render_template("story2.html", storytext=storytext, picUrl=pictureUrl, question=question, opt1="go swimming", opt2="go fishing", opt3="get dressed",
	options3Display="display:inline",
	options2Display="display:none",
	options1Display="display:none",
	audio=audio)

@app.route('/story2', methods=['GET','POST'])
def story2():

	if request.method == 'GET':
		state['story2_choices'] = []
		return story2start()

	elif request.method == 'POST':
		userChoice = request.form['story2Option']
		state['story2_choices'].append(userChoice)
		c = storybook_app.story2_conditions(state['story2_choices'])
		storytext = storybook_app.get_storytext(c)
		question = storybook_app.get_question(c)
		pictureUrl = storybook_app.get_pictureUrl(c)
		audio = storybook_app.get_audio(c)

		options3Display = storybook_app.get_options3Display(c)
		options2Display = storybook_app.get_options2Display(c)
		options1Display = storybook_app.get_options1Display(c)

		opt1 = "default opt1"
		opt2 = "default opt2"
		opt3 = "default opt3"

		if options3Display == "display:inline":
			opt1 = storybook_app.get_opt1(c)
			opt2 = storybook_app.get_opt2(c)
			opt3 = storybook_app.get_opt3(c)
		if options2Display == "display:inline":
			opt1 = storybook_app.get_opt1(c)
			opt2 = storybook_app.get_opt2(c)
		if options1Display == "display:inline":
			opt1 = storybook_app.get_opt1(c)

#		audio = "/static/happyBirthday.mp3"

		return render_template("story2.html", storytext=storytext, picUrl=pictureUrl, question=question, opt1=opt1, opt2=opt2, opt3=opt3,
		options3Display=options3Display,
		options2Display=options2Display,
		options1Display=options1Display,
		audio=audio)




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
