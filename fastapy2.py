#!/usr/bin/python

  import sys
if sys.version_info[0] < 2 and sys.version_info[1] < 7:
    raise Exception("""Must be using Python 2.7 for the full
                    functionality of this script.\n
                    Python 3.7 is required for the full script.""")
if sys.version_info[0] >= 2 and sys.version_info[1] >= 7:
    print('Your using at least Version 2.7, You are good to go...')

PRINT_ERROR = '''Does not exist\n
                 Get module installed before import attempt\n
                 If running server side then contact your admin'''

try:
  import sys
  print('SYS import successful')
except ImportError:
  print(PRINT_ERROR)
  sys.exit(0)

try:
  import argparse
  print('ARGPARSE import successful')
except ImportError:
  print(PRINT_ERROR)
  sys.exit(0)
#import glob2


DOCSTRING = """
-------------------------------------------------------------
            File Parsing
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
           - JOINER DOES NOT WORK IN PYTHON 2 - 
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


def parse_command_args(args=None):
    """
    Sets up and parses command line arguments

    Returns:
        the arguments namespace
    """
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=DOCSTRING)
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
    op = parser.parse_args(args)
    return op


print('You have entered: \n{0}'.format(sys.argv[1:]))


def main():
    """
    A for loop for argument checking and
    function calling
    """
    op = parse_command_args()
    
    if op.EN:
        entryfunction(op.FI, op.FO, op.EN)
        print('entryfunction selected \n{0}'.format(sys.argv[1:]))
        if len(sys.argv[1:]) != 6:
            print('Check the number of args, somethings not right')
            sys.exit(0)

    if op.CS:
        chunkfunction(op.FI, op.FO, op.CS, op.ORG)
        print('chunkfunction selected \n{0}'.format(sys.argv[1:]))
        if len(sys.argv[1:]) != 8:
            print('Check your number of args, somethings not right')
            sys.exit(0)

    if op.SC and op.EC:
        surgicalfunction(op.FI, op.FO, op.SC, op.EC)
        print('surgicalfunction selected \n{0}'.format(sys.argv[1:]))
        if len(sys.argv[1:]) != 8:
            print('Check your number of args, somethings not right')
            sys.exit(0)

    if op.J:
        joinerfunction(op.FI, op.FO, op.J)
        print('joinerfunction selected \n{0}'.format(sys.argv[1:]))
        if len(sys.argv[1:]) != 6:
            print('Check your number of args, somethings not right')
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

    with open(FI) as filetoparse:
        for name, seq in read_fasta(filetoparse):
            nameseq = name, seq
            entry.append(nameseq)
            count += 1

            if count == EN:
                filecounter += 1

                with open('{0}{1}.fa'.format(FO, filecounter), 'w') as done:
                    print('Find your file at: \n {0}entry{1}.fa'.format(FO, filecounter))
                    for idss, sequence in entry:
                        done.write('{0}{1} \n'.format(idss, sequence))

                    count = 0
                    entry = []

        filecounter += 1
        with open('{0}entry{1}.fa'.format(FO, filecounter), 'w') as done:
            for idss, sequence in entry:
                done.write('{0}{1} \n'.format(idss, sequence))

            entry = []
            print('Give me a second to load files')


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
            with open('{0}{1}|{2}.fa'.format(FO, ORG, counter), 'w') as opened:
                print('Find your file at: \n {O}{1}.fa'.format(FO, ORG))
                opened.write(''.join(towrite))
                counter += 1
                towrite = []
                length = 0

        read = file.readline()
    with open('{0}{1}|{2}.fa'.format(FO, ORG, counter), 'w') as opened:
        opened.write(''.join(towrite))
        print('Find your file at: \n {O}{1}.fa'.format(FO, ORG))
        towrite = []
        length = 0


def surgicalfunction(FI, FO, SC, EC):
    """A function to find a specified index of """
    with open(FI, 'r') as opened:
        openread = opened.read()
        openread2 = openread.strip()
        find = openread2[SC:EC]
        with open('{O}snipped|{1}:{2}.fa'.format(FO, SC, EC), 'w') as snipped:
            print('Find your file at: \n {O}snipped|{1}:{2}.fa'.format(FO, SC, EC))
            snipped.write(find)


# def joinerfunction(FI, FO, J):
#     """A function to join all singular enteries into one multi-line fasta"""
#     filenames = glob2.glob(FI + '*.fa')

#     with open('{O}{1}.fa'.format(FO, J), 'w') as outfile:
#         for file in filenames:
#             with open(file) as infile:
#                 outfile.write(infile.read(5000)+'\n')
#                 print('Find your file at: \n {0}{1}.fa'.format(FO, J))
# Beleive it will fail for large files read(5000) should stop that


if __name__ == '__main__':
    main()
