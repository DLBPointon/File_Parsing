#!/usr/bin/env python

"""
-------------------------------------------------------------
                      ßFile Parsing
-------------------------------------------------------------
This is my program to take an input file and produce outputs
based on the function requested by the User.
-------------------------------------------------------------
FI - FileInput & FO - FileOutPut are mandatory arguments.
--------------'.fa' file will be returned!!!-----------------
-------------------------------------------------------------
entryfunction Function is called when -FI, -FO and -en are entered.
  -  This will split a file into a -en defined number of
     enteries per proceduraly generated files.
     Entries are header and sequence pairs.
  -  Example Input:

     'python trial.py -FI '~Skynet/Desktop/FileOfInterest'
     -FO '~Skynet/Desktop/SaveDir' -en 100'
-------------------------------------------------------------
chunkfunction Function is called when -FI, -FO and -ch are entered.
  -  This will split a file into -ch defined number of base
     pairs per proceduraly generated file.
  -  Example Input:

     'python trial.py -FI '~Replicator/Desktop/FileOfInterest'
     -FO '~Replicator/Desktop/SaveDir' -org Asuran -ch 100000'

     Please Note, small file cause an entryfunction effect.
-------------------------------------------------------------
surgicalfunction Function is called when -FI, -FO, -sc and -ec are
     entered.
  -  This will return the bp between the two user defined
     co-ordinates, -sc and -ec (start and end respectively).
     A file will be produced.
  -  Example Input:

     'python trial.py -FI '~R2D2/Desktop/FileOfInterest'
     -FO '~R2D2/Desktop/SaveDir' -sc 100000 -ec 150000'
-------------------------------------------------------------
joinerfunction Function is called when only -FI and -FO are entered.
  -  This will concatenate a directories worth of files into
     a singular file.
     For this function -FI should end at the directory of
     intended use rather at a file of use.
  -  Example Input:

     'python trial.py -FI '~Hal9000/Desktop/DirOfInterest'
     -FO '~Hal9000/Desktop/SaveDir' -j Name'
     Name is your chosen naming scheme.
-------------------------------------------------------------
ALL FUNCTIONS
  -  When you need everything done and now. This will require
     all args in a specific order:
     Joiner will not be needed in this case.
  -  Order:
     -FI -FO -en -org -ch -sc -ec
  -  Example Input:

     'python trial.py -FI '~Ultron/Desktop/DirOfInterest'
     -FO '~Ultron/Desktop/SaveDir' -en 100 -org Tony -ch 100000
     -sc 125000 -ec 150000'
-------------------------------------------------------------
FILE Nomenclature - Uses the examples above
  -  entryfunction - Files returned as:
       1.fa, 2.fa, 3.fa, 4.fa, 5.fa... etc

  -  chunkfunction - Files returned as:
       Asuran|1.fa, Asuran|2.fa, Asuran|3.fa

  -  surgicalfunction - Files returned as:
       snipped|100000/150000.fa

  -  joinerfunction - Files returned as:
       jointfiles.fa

-------------------------------------------------------------
           By Damon-Lee Pointon
"""
import sys
import argparse
import textwrap
import glob2


def parse_command_args(args=sys.argv[1:]):
    """
    Sets up and parses command line arguments

    Returns:
        the arguments namespace
    """
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s Beta 4.0')
    parser.add_argument('-FI', '--Input',
                        type=str,
                        action='store',
                        help='Input FASTA file',
                        dest="FI",
                        required=True)
    parser.add_argument('-FO', '--OutPut',
                        type=str,
                        action='store',
                        help='Output Directory',
                        dest="FO",
                        required=True)
    parser.add_argument('-cs', '--Chunk',
                        action='store',
                        type=str,
                        help='Base-pair length of chunk per file',
                        dest='CS')
    parser.add_argument('-org', '--Name',
                        type=str,
                        action='store',
                        help='A User defined pre-fix for the save files',
                        dest='ORG')
    parser.add_argument('-sc', '--SCoord',
                        action='store',
                        type=int,
                        help='The User defined Starting Index for a substring',
                        dest='SC')
    parser.add_argument('-ec', '--ECoord',
                        action='store',
                        type=int,
                        help='The User defined End index for a substring',
                        dest='EC')
    parser.add_argument('-en', '--EntryNo',
                        action='store',
                        type=int,
                        help='The number of entries required per file',
                        dest='EN')
    parser.add_argument('-j', '--joiner',
                        action='store',
                        type=str,
                        help='A non functional that specifies joinerfunction',
                        dest='J')
    options = parser.parse_args(args)
    return options


def main():
    """
    A for loop for argument checking and
    function calling
    """
    options = parse_command_args()
    aFI = sys.argv[2]
    aFO = sys.argv[4]
    for arg in sys.argv:

        if arg == '-en':
            entryfunction(aFI, aFO, int(sys.argv[6]))
            print(f'entryfunction selected \n{sys.argv[1:]}')
            if len(sys.argv[1:]) != 6:
                print('Check the number of args, somethings not right')
                sys.exit(0)

        elif arg == '-cs':
            chunkfunction(aFI, aFO, int(sys.argv[6]), sys.argv[8])
            print(f'chunkfunction selected \n{sys.argv[1:]}')
            if len(sys.argv[1:]) != 8:
                print('Check your number of args, somethings not right')
                sys.exit(0)

        elif arg == '-sc':
            surgicalfunction(aFI, aFO, int(sys.argv[6]), int(sys.argv[8]))
            print(f'surgicalfunction selected \n{sys.argv[1:]}')
            if len(sys.argv[1:]) != 8:
                print('Check your number of args, somethings not right')
                sys.exit(0)

        elif arg == '-j':
            joinerfunction(aFI, aFO, sys.argv[6])
            print(f'joinerfunction selected \n{sys.argv[1:]}')
            if len(sys.argv[1:]) != 6:
                print('Check your number of args, somethings not right')
                sys.exit(0)

        elif len(arg) == 14:
            entryfunction(aFI, aFO, int(sys.argv[6]))
            chunkfunction(aFI, aFO, sys.argv[8], int(sys.argv[10]))
            surgicalfunction(aFI, aFO, int(sys.argv[12]), int(sys.argv[14]))
            print(f'entry, chunk and surgical all selected \n{sys.argv[1:]}')
            if len(sys.argv[1:]) != 14:
                print('Check your number of args, somethings not right.')
                print('Calling all funs requires a specific order')
                sys.exit(0)


def read_fasta(filetoparse):
    """A function which opens and splits a fasta into name and seq"""
    name, seq = None, []
    for line in filetoparse:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))


def entryfunction(FI, FO, EN=1):
    """The entryfunction function splits a FASTA file into a user defined
    number of entries per file"""
    count = 0
    filecounter = 0
    entry = []
    print('Give me a second to load files')
    with open(FI) as filetoparse:
        for name, seq in read_fasta(filetoparse):
            nameseq = name, seq
            entry.append(nameseq)
            count += 1

            if count == EN:
                filecounter += 1

                with open(f'{FO}{filecounter}.fa', 'w') as done:
                    print(f'Find your file at: \n {FO}{filecounter}.fa')
                    for idss, sequence in entry:
                        done.write(f'{idss} {sequence} \n\n')

                    count = 0
                    entry = []

        filecounter += 1
        with open(f'{FO}{filecounter}.fa', 'w') as done:
            print(f'Find your file at: \n {FO}{filecounter}.fa')
            for idss, sequence in entry:
                done.write(f'{idss} {sequence} \n\n')

            entry = []


def chunkfunction(FI, FO, CS, ORG='chunk'):
    """A function to split a file based on user defined bp per file"""
    towrite = []
    length = 0
    counter = 0

    file = open(FI, 'r')
    read = file.readline()

    while read:
        towrite.append(read)
        length += len(read)
        if length >= CS:
            with open(f'{FO}{ORG}|{counter}.fa', 'w') as opened:
                opened.write(''.join(towrite))
                counter += 1
                towrite = []
                length = 0
                print(f'Find your file at: \n {FO}{ORG}{counter}.fa')

        read = file.readline()
    with open(f'{FO}{ORG}|{counter}.fa', 'w') as opened:
        opened.write(''.join(towrite))
        towrite = []
        length = 0
        print(f'Find your file at: \n {FO}{ORG}{counter}.fa')
    file.close()


def surgicalfunction(FI, FO, SC, EC):
    """A function to find a specified index of """
    with open(FI, 'r') as opened:
        openread = opened.read()
        openread2 = openread.strip()
        find = openread2[SC:EC]
        with open(f'{FO}snipped|{SC}:{EC}.fa', 'w') as snipped:
            snipped.write(find)
            print(f'Find your file at: \n {FO}snipped|{SC}:{EC}.fa')


def joinerfunction(FI, FO, J):
    """A function to join all singular enteries into one multi-line fasta"""
    filenames = glob2.glob(FI + '*.fa')

    with open(f'{FO}{J}.fa', 'w') as outfile:
        for file in filenames:
            with open(file) as infile:
                for line in infile:
                    outfile.write(line)
    print(f'Find your file at: \n {FO}{J}.fa')
# Beleive it will fail for large files read(5000) should stop that


if __name__ == '__main__':
    main()
