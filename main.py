from flask import Flask, render_template

web_site = Flask(__name__)

@web_site.route('/')
def home():
	return render_template('test.html')

@web_site.route('/command')
def index():
	return render_template('command.html')

@web_site.route('/about')
def about():
	return render_template('about.html')
 
@web_site.route('/command/nsfw')
def nsfw():
	return render_template('nsfw.html')


@web_site.route('/giveaway')
def giveaway():
	return render_template('giveaway.html')

web_site.run(host='0.0.0.0', port=8080)