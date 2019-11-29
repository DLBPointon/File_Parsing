#Import Functions
import argparse
import sys
import os
import textwrap

parser = argparse.ArgumentParser(prog = 'PlayWithFasta', 
								formatter_class = argparse.RawDescriptionHelpFormatter,
								description = textwrap.dedent("""\

						   Welcome to Play with Fasta
						  ----------------------------
					   A script to process and parse FASTA files

				   This script contains the function Chunk (c), Entry (e), 
				   Surgical (s) and Joiner (j) which will parse a given file 
				   in the specified way: 
				   c = creates multiple files, each containing User defined bp. 
				   e = creates multiple files, each with a User specified 
				     number of entries. 
				   s = this file will return a substring found between the User 
				     defined indexs. 
				   j = this function will join all files in a directory. 
				     For example a large multi-line FASTA.

					   	     By Damon-Lee Pointon

									"""))
parser.add_argument('-a', choices = ['e', 'c', 's', 'j'],
					required = True,
					action = 'store',
					help = 'e = Entry Number Per File Function, c = Number of Base Pairs per file Function, s = Return the substring between two user defined indexs and j = Joins singular entry file into one file.')
#Parser for the subparsers
subparsers = parser.add_subparsers()

def Entry(FileInput, FileOutPut, EntryNo = 1):
    
    Count = 0
    FileCounter = 0
    NandS = []
    
    def read_fasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []           
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

    with open(FileInput) as fp:
        for name, seq in read_fasta(fp):
            NameSeq = name, seq
            print(name, seq)
            NandS.append(str(NameSeq).strip())
            count += 1 
            if Count == EntryNo:
                FileCounter += 1
                with open(FileOutPut + str(FileCounter) + '.fasta', 'w') as Done:
                    Done.write(str(NandS).strip('[](),""'''))
                    Count = 0
                    NandS = []
        
        else:
            with open(FileOutPut + str(FileCounter) + '.fasta', 'w') as Done:
                Done.write(str(NandS).strip('[](),""''').replace(',', '\n'))
                NandS = []

def Chunks(FileInput, FileOutPut, OrganismOI, ChunkSize):
    File = open(FileInput, 'r')
    Read = File.readline()
    ToWrite = []
    Length = 0
    Counter = 0

    while Read:
        ToWrite.append(Read)
        Length += len(Read)-1
        if Length > ChunkSize:
            with open(FileOutPut + OrganismOI + '|{}'.format(Counter) + '.fasta', 'w') as o:
                o.write(''.join(ToWrite))
                Counter += 1
                ToWrite = []
                Length = 0
        Read = File.readline()
    with open(FileOutPut + OrganismOI + '|{}'.format(Counter) + '.fasta', 'w') as o:
        o.write(''.join(ToWrite))

def Surgical(FileInput, StartCoord, EndCoord):
    with open(FileInput, 'r') as Open:
        OR = Open.read()
        OR2 = OR.strip()
        Find = OR2[StartCoord:EndCoord]
        print(Find)

def Joiner(Dir, FileOutPut):
    Total = []
    Counter = 0

    for file in os.listdir(FileOutPut):
        if file.endswith('.fasta'):
            fullpath = os.path.join(FileOutPut, file)
            Total.append(fullpath)
            with open(FileOutPut + Counter, 'w') as outfile:
                for filename in Total:
                    with open(filename ,'r') as infile:
                        for line in infile:
                            outfile.write(line)

def main():
#Entry: Number per file function
	entry_parser = subparsers.add_parser('Entry')
	entry_parser.set_defaults(func = Entry)
	entry_parser.add_argument('-fi', '-FileInput', 
					action = 'store',
					type = str, 
					help = 'File to be Input into the function')
	entry_parser.add_argument('-fo', '-FileOutPut', 
					action = 'store',
					type = str,
					help = 'Directory of output files')
	entry_parser.add_argument('-en', '-EntryNo', 
					action = 'store',
					type = int,
					help = 'Number of entries per file')

#Chunks: Base Pair per file function
	chunks_parser = subparsers.add_parser('Chunks')
	chunks_parser.set_defaults(func = Chunks)
	chunks_parser.add_argument('-fi', '-FileInput', 
					action = 'store',
					type = str, 
					help = 'File to be Input into the function')
	chunks_parser.add_argument('-fo', '-FileOutPut', 
					action = 'store',
					type = str,
					help = 'Directory of output files')
	chunks_parser.add_argument('-org', '-OrganismOI', 
					action = 'store',
					type = str,
					help = 'The Organism of Interest')
	chunks_parser.add_argument('-ch', '-ChunkSize', 
					action = 'store',
					type = str,
					help = 'The size, in base pairs, that each file is required to be')

#Surgical: Returns a sub-string between the user defined indexs
	surgical_parser = subparsers.add_parser('Surgical')
	surgical_parser.set_defaults(func = Surgical)
	surgical_parser.add_argument('-fi', '-FileInput', 
					action = 'store',
					type = str, 
					help = 'File to be Input into the function')
	surgical_parser.add_argument('-sc', '-StartCoord', 
					action = 'store',
					type = int,
					help = 'The User defined Starting Index for a substring')
	surgical_parser.add_argument('-ec', '-EndCoord', 
					action = 'store',
					type = int,
					help = 'The User defined End index for a substring')

#Joiner, joins the diretory contents into one file
	joiner_parser = subparsers.add_parser('Joiner')
	joiner_parser.set_defaults(func = Joiner)
	joiner_parser.add_argument('-dir', '-Directory',
					action = 'store',
					type = str,
					help = 'The working directory containing all files to be used by this function')
	joiner_parser.add_argument('-fo', '-FileOutPut', 
					action = 'store',
					type = str,
					help = 'The directory the finished file will be output to')

#Making sure args are plugged proppperly
	args = parser.parse_args()
	try:
		func = args.func(args)
		FileInput = args.FileInput
		FileOutPut = args.FileOutPut
		ChunkSize = args.ChunkSize
		EntryNo = args.EntryNo
		StartCoord = args.StartCoord
		EndCoord = args.EndCoord
		OrganismOI = args.OrganismOI
		Dir = args.Directory
	except AttributeError:
		parser.error("too few arguments")
		
	func(args)
	

#Version Control
parser.add_argument('--version', action = 'version', 
					version = '%(prog)s 2.0')
args, sub_args = parser.parse_known_args()

main()
