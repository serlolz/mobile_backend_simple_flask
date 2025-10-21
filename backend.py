from flask import Flask
import json

app = Flask(__name__)

@app.route('/categories.get')
def get_categories():
   data=[{'id':1,'name':'Food'},{'id':2,'name':'Beverage'}]
   return json.dumps(data)


@app.route('/')
def index():
   return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
   app.run(port=8080)


