import sqlite3
from flask import Flask, render_template, redirect, url_for, request

cursor = sqlite3.connect('database.db') #connect to the database that we'll be using for our website

#just gonna go ahead and add some dummy thingys for now, since we're really just looking to exploit this data and read/edit/delete it

cursor.execute('CREATE table usernames')


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST': #this meeans the user is trying to enter a username+password into our form! yay! or dun dun dunn is it a hacker
		name = request.form['name']
		password = request.form['password']
		if(cursor.execute('SELECT exists(SELECT * from names where name = ?', (name,)):
			return render_template('success.html')
	else return render_template('nope.html')






