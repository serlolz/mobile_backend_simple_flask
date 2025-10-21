from flask import Flask
import json

app = Flask(__name__)


@app.route('/news.all.get')
def get_news_all_articles():
	data=[]
	with open('news_data.json', 'r') as file:
		data = json.load(file)
	app.logger.debug('_________________Hello '+str(data))
	return json.dumps(data)


@app.route('/news.categories.get')
def get_news_categories():
	data=[{'id':1,'name':'Sports'},{'id':2,'name':'Politics'},{'id':3,'name':'Education'}]
	return json.dumps(data)


@app.route('/')
def index():
	return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
	app.run(port=8080)


