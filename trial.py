"""
-------------------------------------------------------------
			File Parsing
-------------------------------------------------------------
This is my program to take an input file and produce outputs
based on the function requested by the User.
-------------------------------------------------------------
FI - FileInput & FO - FileOutPut are mandatory arguments.
--------------'.fa' file will be returned!!!-----------------
-------------------------------------------------------------
Entry Function is called when -FI, -FO and -en are entered.
  -  This will split a file into a -en defined number of 
     enteries per proceduraly generated files.
     Entries are header and sequence pairs.
  -  Example Input:

     'python trial.py -FI ~Skynet/Desktop/FileOfInterest 
     -FO ~Skynet/Desktop/SaveDir -en 100'
-------------------------------------------------------------
Chunks Function is called when -FI, -FO and -ch are entered.
  -  This will split a file into -ch defined number of base
     pairs per proceduraly generated file.
  -  Example Input:

     'python trial.py -FI ~Replicator/Desktop/FileOfInterest 
     -FO ~Replicator/Desktop/SaveDir -org Asuran -ch 100000'
-------------------------------------------------------------
Surgical Function is called when -FI, -FO, -sc and -ec are 
     entered.
  -  This will return the bp between the two user defined 
     co-ordinates, -sc and -ec (start and end respectively).
     A file will be produced.
  -  Example Input:

     'python trial.py -FI ~R2D2/Desktop/FileOfInterest 
     -FO ~R2D2/Desktop/SaveDir -sc 100000 -ec 150000'
-------------------------------------------------------------
Joiner Function is called when only -FI and -FO are entered.
  -  This will concatenate a directories worth of files into
     a singular file.
     For this function -FI should end at the directory of 
     intended use rather at a file of use.
  -  Example Input:

     'python trial.py -FI ~Hal9000/Desktop/DirOfInterest 
     -FO ~Hal9000/Desktop/SaveDir'
-------------------------------------------------------------
ALL FUNCTIONS
  -  When you need everything done and now. This will require
     all args in a specific order:
  -  Order:
     -FI -FO -en -org -ch -sc -ec
  -  Example Input:

     'python trial.py -FI ~Ultron/Desktop/DirOfInterest 
     -FO ~Ultron/Desktop/SaveDir -en 100 -org Tony -ch 100000
     -sc 125000 -ec 150000'
-------------------------------------------------------------
FILE Nomenclature - Uses the examples above
  -  Entry - Files returned as: 
       1.fa, 2.fa, 3.fa, 4.fa, 5.fa... etc
  -  Chunks - Files returned as: 
       Asuran|1.fa, Asuran|2.fa, Asuran|3.fa
  -  Surgical - Files returned as:
       snipped|100000/150000.fa
  -  Joiner - Files returned as:
  	   Not Finished

-------------------------------------------------------------
		   By Damon-Lee Pointon
"""
import os
import sys
import argparse
import textwrap

def parse_command_args(args=sys.argv[1:]):
	"""
	Sets up and parses command line arguments

	Returns:
		the arguments namespace
	"""
	parser = argparse.ArgumentParser(prog='FileParsing',
							formatter_class = argparse.RawDescriptionHelpFormatter,
							description = textwrap.dedent(__doc__))
	parser.add_argument('-v', '--version', 
							action = 'version', 
							version = '%(prog)s Beta 3.0')
	parser.add_argument('-FI', '--FileInput',
							type=str,
							action='store',
							help='Input FASTA file',
							dest="FI",
							required=True)
	parser.add_argument('-FO', '--FileOutPut',
							type=str,
							action='store',
							help='Output Directory',
							dest="FO",
							required=True)
	parser.add_argument('-ch', '--ChunkSize', 
							action='store',
							type=str,
							help='The size, in base pairs, that each file is required to be',
							dest='CS')
	parser.add_argument('-org', '--OrgansimOI',
							type=str,
							action='store',
							help='A User defined pre-fix for the save files',
							dest='ORG')
	parser.add_argument('-sc', '--StartCoord', 
							action = 'store',
							type = int,
							help = 'The User defined Starting Index for a substring',
							dest='SC')
	parser.add_argument('-ec', '--EndCoord', 
							action = 'store',
							type = int,
							help = 'The User defined End index for a substring',
							dest='EC')
	parser.add_argument('-en', '--EntryNo', 
							action='store',
							type=int,
							help='The number of entries required per file',
							dest='EN')
	parser.add_argument('-j', '--Joiner',
							action='store',
							help='A non functional argument that specifies the joiner junction',
							dest='J')
	options=parser.parse_args(args)
	return options

def main():
	"""
	A for loop for argument checking and
	function calling
	"""
	options=parse_command_args()
	for x in sys.argv:
		if x == '-FI' and '-FO':

			if x == '-en':
				Entry(sys.argv[2], sys.argv[4], int(sys.argv[6]))
				if not len(sys.argv[1:]) == 6:
					print('Check your number of arguments, somethings not right')
					sys.exit(0)

			if x == '-ch':
				Chunks(sys.argv[2], sys.argv[4], sys.argv[6], int(sys.argv[8]))
				if not len(sys.argv[1:]) == 8:
					print('Check your number of arguments, somethings not right')
					sys.exit(0)

			if x == '-sc':
				Surgical(sys.argv[2], sys.argv[4], int(sys.argv[6]), int(sys.argv[8]))
				if not len(sys.argv[1:]) == 8:
					print('Check your number of arguments, somethings not right')
					sys.exit(0)

			if x == '-j':
				Joiner(sys.argv[2], sys.argv[4])
				if not len(sys.argv[1:]) == 4:
					print('Check your number of arguments, somethings not right')
					sys.exit(0)


			if len(x) == 14: 
				Entry(sys.argv[2], sys.argv[4], int(sys.argv[6]))
				Chunks(sys.argv[2], sys.argv[4], sys.argv[8], int(sys.argv[10]))				
				Surgical(sys.argv[2], sys.argv[4], int(sys.argv[12]), int(sys.argv[14]))
				Joiner(sys.argv[2], sys.argv[4])
				if not len(sys.argv[1:]) == 14:
					print('Check your number of arguments, somethings not right. Remember, calling all arguments requires a specific order')
					sys.exit(0)

			else:
				print('Have you used the correct args?')
				print(x)
				sys.exit(0)
		else:
			print('You have not used the mandatory -FI (FileInput) and -FO (FileOutPut) flags')
			print(x)
			sys.exit(0)


print(f'You have entered:\n{sys.argv[1:]}')


def read_fasta(fp): # Temp Until Entry is optimised
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []           
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

			
def Entry(FI, FO, EN = 1): #Optimise me please
	
	Count = 0
	FileCounter = 0
	NandS = []
	
	with open(FI) as fp:
		for name, seq in read_fasta(fp):
			NameSeq = name, seq
			NandS.append(str(NameSeq).strip())
			Count += 1 
			
			if Count == EN:
				FileCounter += 1
				
				with open(FO + str(FileCounter) + '.fa', 'w') as Done:
					Done.write(str(NandS).strip('[](),""'''))
					Count = 0
					NandS = []
		
		else:
			
			with open(FO + str(FileCounter) + '.fa', 'w') as Done:
				Done.write(str(NandS).strip('[](),""''').replace(',', '\n'))
				NandS = [] #Will be replaced with something waaay better# But Works


def Chunks(FI, FO, CS, ORG = 'Chunk'):
	with open(FI, 'r') as File:
		Read = File.readline()
		ToWrite = []
		Length = 0
		Counter = 0

		while Read:
			ToWrite.append(Read)
			Length += len(Read)-1
		if Length > CS:
			with open(FO + ORG + '|{}'.format(Counter) + '.fa', 'w') as o:
				o.write(''.join(ToWrite))
				Counter += 1
				ToWrite = []
				Length = 0
			Read = File.readline()
		with open(FO + ORG + '|{}'.format(Counter) + '.fa', 'w') as o:
			o.write(''.join(ToWrite))#Works


def Surgical(FI, FO, SC, EC):
	with open(FI, 'r') as Open:
		OR = Open.read()
		OR2 = OR.strip()
		Find = OR2[SC:EC]
		with open(f'{FO}snipped|{SC}:{EC}.fa', 'w') as Snipped:
			print(Find + f'{FO}snipped|{SC}:{EC}.fa', 'w')
			Snipped.write(Find) #Works


def Joiner(FI, FO): #Not Working
	Total = []
	Counter = 0

	for file in os.listdir(FO):
		if file.endswith('.fasta' or '.fa' or '.fna'):
			fullpath = os.path.join(FO, file)
			Total.append(fullpath)
			with open(FO + Counter, 'w') as outfile:
				for filename in Total:
					with open(filename ,'r') as infile:
						for line in infile:
							outfile.write(line)


if __name__ == '__main__':
	main()