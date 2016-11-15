"""
	This is a simple command line application called NUMBER_APP
	That consumes a public api NUMBERS APP FROM mashape.com.
	It lets you get a fun mathematical property about a number 
"""
import os
import urllib2


###  FUNCTIONS   ###
def display_title_bar():
	#clear the screen and display title bar
	os.system("clear")

	print("\t**********************************************")
	print("\t***   NUMBER_APP  ***")
	print("\t*** Hello old and new friends!  ***")
	print("\t*** Enter any number and learn a mathematical property about it. ***")
	print("\t**********************************************")

def get_user_input():

	num = int(input("Enter a number"))


### MAIN FUNCTION ###

	display_title_bar()
	
	while num != 0:
		num = get_user_input()

		response = urllib2.urlopen(https://numbersapi.p.mashape.com/{number}/math)
		html = response.read()
		
		curl --get --include 'https://numbersapi.p.mashape.com/1729/math?fragment=true&json=true' \
	  	-H 'X-Mashape-Key: XkQxbgnUcimshlmLWonFBaCY20MZp1yp9d6jsndCKBE0QisoYG' \
	  	-H 'Accept: text/plain'

	
