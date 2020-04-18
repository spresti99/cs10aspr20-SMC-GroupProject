"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import storybook_app
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
	return render_template('storybook.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/story2')
def story2():
    return render_template('story2.html')

@app.route('/story3')
def story3():
    return render_template('story3.html')

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
