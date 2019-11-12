"""
This is my program to take an input file and produce outputs
based on the function requested by the User.
"""
import os
import sys
import argparse


def parse_command_args():
	"""
	Sets up and parses command line arguments

	Returns:
		the arguments namespace
	"""
	parser = argparse.ArgumentParser(prog='FileParing',
							description=__doc__)

		#Positional Arguments
	parser.add_argument('FILEINPUT', 
							action='store',
							help='Input FASTA file')
	parser.add_argument('FILEOUT',
							action='store',
							help='Output Directory')

		#Optionals
	parser.add_argument('-org', '-OrganismOI', 
							action='store',
							type=str,
							help='The Organism of Interest')
	parser.add_argument('-ch', '-ChunkSize', 
							action='store',
							type=str,
							help='The size, in base pairs, that each file is required to be')
	parser.add_argument('-sc', '-StartCoord', 
							action = 'store',
							type = int,
							help = 'The User defined Starting Index for a substring')
	parser.add_argument('-ec', '-EndCoord', 
							action = 'store',
							type = int,
							help = 'The User defined End index for a substring')
	parser.add_argument('-En', '-EntryNo', 
							action='store',
							type=int,
							help='The number of entries required per file')
	args = parser.parse_args()
	options = parser.parse_args(args)
	return args

args = parse_command_args()

print(args.FILEINPUT)

def main():
	options = getOptions(sys.argv[1:])

	try:
		FI = Options.FILEINPUT
		FO = Options.FILEOUT
		CS = Options.ChunkSize
		EntryNo = Options.EntryNo
		StartCoord = Options.StartCoord
		EndCoord = Options.EndCoord
		OrganismOI = Options.OrganismOI
		Dir = Options.Directory
	except NameError:
		print('Not Found')




