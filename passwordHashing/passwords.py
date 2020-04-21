import hashlib
import sqlite3
import csv
from passlib.hash import sha256_crypt

#this script looks to understand the different levels of encryption for passwords in a database

#lets look at a plain textfile with some username, password values
passfile = open("passfile.txt", "r")

#now, the most obvious and least secure way to store values is in plaintext
#these values can be printed out directly, something that can be a huge vulnerability
for pair in passfile:
	print(pair)

#the first method of encryption, is to set a hash function with a random value - using standard encryption functions
#here, let's go ahead and create a new file with the hashed passwords


#we'll be working with two extremely common encryption algorithms - the MD5 and SHA256 hashes respectively
def hashlibEncodeMD5(password):
	h = hashlib.md5(password.encode())
	return h.hexdigest()

def hashlibEncodeSHA256(password):
	h = hashlib.sha256(password.encode())
	return h.hexdigest()

with open("passfile.txt", "r") as passfile:
	with open("hashfile.txt", "w") as hashfile:
		csv_reader = csv.reader(passfile, delimiter=',')
		for row in csv_reader:
			password = row[1]
			hashfile.write(row[0] + ", " + hashlibEncodeMD5(password) + "\n")

#however, the problem with this is that these encryptions are consistent and unchanging for keywords.
#this problem, is solved (to some extent) by salting passwords

salt = 'iru99'
with open("passfile.txt", "r") as passfile:
	with open("salty.txt", "w") as salty:
		csv_reader = csv.reader(passfile, delimiter=',')
		for row in csv_reader:
			password = row[1] + salt
			salty.write(row[0] + ", " + hashlibEncodeSHA256(password) + "\n")

#finally, let's understand what the passlib library does - allowing the same password to have different hash values from encryption functions seeded by random salts
#To do this and view it clearly, let's look at the first password in our file and encrypt it into two different strings with the passlib library

password = "hamilton1776"
encryptOne = sha256_crypt.encrypt(password)
encryptTwo = sha256_crypt.encrypt(password)

with open("cryptCompare.txt", "w") as checkFile:
	checkFile.write("First hash: " + encryptOne + "\nPassword Two: " + encryptTwo)

#and so, we have started with plaintext and reached the industry standard of password encryption!