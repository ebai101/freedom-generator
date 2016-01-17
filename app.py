from flask import Flask, render_template, request, jsonify
import markovify

DEBUG = False
SECRET_KEY = 'wuddafuggins'
TEXT_MODEL = markovify.Text(unicode(open('text/debates.txt').read(), "utf-8"))

app = Flask(__name__)
app.config.from_object(__name__)

def gen_sentence():
	sentences = []
	for i in range(5):
		sentences.append(TEXT_MODEL.make_sentence())
	return ' '.join(sentences)

@app.route('/get_text')
def get_text():
	return jsonify(text=gen_sentence())

@app.route('/')
def index():
	return render_template('index.html', text=gen_sentence())
	
if __name__ == '__main__':
	app.run()
