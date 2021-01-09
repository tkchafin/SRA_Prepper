#!/usr/bin/python

import sys
import os
import getopt
import pandas as pd

def main():
	params = parseArgs()
	
	

#Object to parse command-line arguments
class parseArgs():
	def __init__(self):
		#Define options
		try:
			options, remainder = getopt.getopt(sys.argv[1:], 'hp:', \
			["help", "params="])
		except getopt.GetoptError as err:
			print(err)
			self.display_help("\nExiting because getopt returned non-zero exit status.")
		#Default values for params
		#Input params
		self.paramfile=None


		#First pass to see if help menu was called
		for o, a in options:
			if o in ("-h", "-help", "--help"):
				self.display_help("Exiting because help menu was called.")

		#Second pass to set all args.
		for opt, arg_raw in options:
			arg = arg_raw.replace(" ","")
			arg = arg.strip()
			opt = opt.replace("-","")
			#print(opt,arg)
			if opt == "h" or opt == "help":
				continue
			elif opt=="p" or opt=="params":
				self.paramfile=arg
			else:
				assert False, "Unhandled option %r"%opt

		#Check manditory options are set
		if not self.paramfile:
			self.display_help("No param file provided.")



	def display_help(self, message=None):
		if message is not None:
			print()
			print (message)
		print ("\nfastaFormatter.py\n")
		print("Author: Tyler K Chafin, University of Arkansas")
		print ("Contact: tylerkchafin@gmail.com")
		print ("Description: Preps files from projects with large numbers of samples for SRA upload")
		print("""
		-p, --params:	Path to params file (see example)
""")
		print()
		sys.exit()

#Call main function
if __name__ == '__main__':
    main()
