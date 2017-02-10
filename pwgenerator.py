'''
pwgenerator.py - Michael Bateman
Refer to https://github.com/michael-bateman/password-generator/blob/master/README.md for documentation.
'''

# imports
import random

# main code

# the following is user input
amountoftimes = input("How many passwords would you like generated? ") # number of passwords to be generated
pw_length = input("What's the length of characters in your password? ") # the numbers of charecters for your password
lowercasetimes = input("Lowercase letters? ")
numbertimes = input("Numbers? ")
upcasetimes = input("Upper case? ")

# does calculations based on how many of what types of password you wany
lowercase = "abcdefghijklmnopqrstuvwxyz" * lowercasetimes
number = "0123456789" * numbertimes
upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * upcasetimes

# if/else statement to make strings
if (lowercasetimes == 0):
	alphabet = number + upcase
elif (numbertimes == 0):
	alphabet = upcase + lowercase
elif (upcasetimes == 0):
	alphabet = number + lowercase
else:
	alphabet = lowercase + number + upcase

# opens the file 'passwords.txt' for writing
file = open("passwords.txt","w")

# generates the passwords
for i in range(amountoftimes):
	mypw = ""
	for i in range(pw_length):
	    next_index = random.randrange(len(alphabet))
	    mypw = mypw + alphabet[next_index]

	file.write(mypw + '\n') # writes the password in the file

file.close() # closes the file when complete
