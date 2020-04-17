import sqlite3
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

#just gonna go ahead and add some dummy thingys for now, since we're really just looking to exploit this data and read/edit/delete it

#SELECT exists(SELECT * from usernames where name = usr



@app.route('/login', methods = ['GET', 'POST'])
def login():
	cursor = sqlite3.connect('database.db') #connect to the database that we'll be using for our website
	cursor.execute("INSERT into usernames VALUES('techsupport','techpassword')")
	cursor.execute("INSERT into usernames VALUES('custsupport','custpassword')")
	cursor.execute("INSERT into usernames VALUES('Alpheus','Alpass')")
	cursor.execute("INSERT into usernames VALUES('Barthemius','Bartword')")
	cursor.execute("INSERT into usernames VALUES('Thisguy1','HisPassword2')")
	
	if request.method == 'POST': #this meeans the user is trying to enter a username+password into our form! yay! or dun dun dunn is it a hacker
		usr = request.form['name']
		password = request.form['password']
		print usr + " " + password
		commandThing = "SELECT exists( SELECT * from usernames where name like'"+usr+"')"
		if ((cursor.execute(commandThing).fetchone()[0]) != 0):
			return "yep"
		else: return render_template('login.html')
	else: return render_template('login.html')

if __name__ == '__main__':
   app.run()





