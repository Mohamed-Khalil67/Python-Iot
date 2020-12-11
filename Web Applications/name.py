# app.py
from flask import Flask, render_template  
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for

app = Flask(__name__)             
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
@app.route('/')           
def index():
    return "This is the home page."

@app.route('/hello')           
def hello():
    return "Hello H3"

@app.route('/profile/<username>')           
def profile(username):
    return "<h2> Hey there %s<h2>" %username

@app.route('/post/<int:post_id>')           
def post(post_id):
    return "<h2> Post ID is %s<h2>" % post_id

@app.route('/api/books',methods = ["GET"])           
def get_book():
    return jsonify({"book":book})

if __name__ == "__main__":        
    app.run(debug=True)                 
