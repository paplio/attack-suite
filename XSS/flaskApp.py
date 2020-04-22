from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/XSS')
def XSS():
	if request.method == 'GET':
		return render_template("myForm.html")
	else: return "Hello there!"

if __name__ == "__main__":
	app.run(debug=False)