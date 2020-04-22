from bs4 import BeautifulSoup
import requests
import flaskApp
import mechanize

def checkXSS(url):
	#using requests to work with a localhost server with BS4
	request = requests.get(url)

	#using BS4 to get info from the html source
	soup = BeautifulSoup(request.text, 'html.parser')
	print(soup.prettify())
	hotNSour = soup.form
	#finding all input elements in the html code
	inputs = hotNSour.find_all('input')
	fields = []

	#adding to an empty list for each attribute in the form
	for thing in inputs:
		if thing.has_attr('name'):
			fields.append(thing['name'])

	#filling out and submitting the form using mechanize
	submitter = mechanize.Browser()
	submitter.open(url)
	submitter.select_form(name='formy')

	#the script we want to inject! :D
	payLoad = '<script>alert("vulnerable!");</script>'

	#usually, we add the script to the first field of the form - since we don't really want to wait when exploiting dumb forms :P
	submitter.form[fields[0]] = payLoad

	#you can basically fill the rest of the forms with just random text, since we don't really care what's happening with it
	for i in range(1, len(fields)):
		submitter.form[fields[i]] = "Some text thingy idk"

	#submitting the form and getting the form result to see if we managed to exploit by injecting JS into it
	submitter.submit()
	result = submitter.response().read()
	print("form submitted! here's what happened: ")
	print("\n"+ result + "\n")

	if('<script>' in str(result)):
		print("form is vulnerable and not protected from XSS!")
	else:
		print("form is protected")

#server wise, we're working with a localhost held by Flask, hosting the server - which in turn hosts the HTML and PHP, which in turn, is read by BS4
if __name__ == "__main__":
	checkXSS("http://127.0.0.1/myForm.html")