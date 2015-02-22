#!/usr/bin/python3

import sys

class Country():
	def __init__(self,string):
		self.string = string
		
	def __str__(self):
		return "Hello from {}".format(self.string)
	
	
	
def main(argv):
	string = (argv[1])
	string2 = (argv[2])
	co2 = Country(string2)
	co = Country(string)
	print(co)
	print(co2)
	

	
if __name__ == "__main__":
	main(sys.argv)
