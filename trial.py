#!/usr/bin/env/python3

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
entryfunction Function is called when -FI, -FO and -en are entered.
  -  This will split a file into a -en defined number of
     enteries per proceduraly generated files.
     Entries are header and sequence pairs.
  -  Example Input:

     'python trial.py -FI ~Skynet/Desktop/FileOfInterest
     -FO ~Skynet/Desktop/SaveDir -en 100'
-------------------------------------------------------------
chunkfunction Function is called when -FI, -FO and -ch are entered.
  -  This will split a file into -ch defined number of base
     pairs per proceduraly generated file.
  -  Example Input:

     'python trial.py -FI ~Replicator/Desktop/FileOfInterest
     -FO ~Replicator/Desktop/SaveDir -org Asuran -ch 100000'
-------------------------------------------------------------
surgicalfunction Function is called when -FI, -FO, -sc and -ec are
     entered.
  -  This will return the bp between the two user defined
     co-ordinates, -sc and -ec (start and end respectively).
     A file will be produced.
  -  Example Input:

     'python trial.py -FI ~R2D2/Desktop/FileOfInterest
     -FO ~R2D2/Desktop/SaveDir -sc 100000 -ec 150000'
-------------------------------------------------------------
joinerfunction Function is called when only -FI and -FO are entered.
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
  -  entryfunction - Files returned as:
       1.fa, 2.fa, 3.fa, 4.fa, 5.fa... etc
  -  chunkfunction - Files returned as:
       Asuran|1.fa, Asuran|2.fa, Asuran|3.fa
  -  surgicalfunction - Files returned as:
       snipped|100000/150000.fa
  -  joinerfunction - Files returned as:
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
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s Beta 3.0')
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
                        help='Base-pair length of chunk per file',
                        dest='CS')
    parser.add_argument('-org', '--OrgansimOI',
                        type=str,
                        action='store',
                        help='A User defined pre-fix for the save files',
                        dest='ORG')
    parser.add_argument('-sc', '--StartCoord',
                        action='store',
                        type=int,
                        help='The User defined Starting Index for a substring',
                        dest='SC')
    parser.add_argument('-ec', '--EndCoord',
                        action='store',
                        type=int,
                        help='The User defined End index for a substring',
                        dest='EC')
    parser.add_argument('-en', '--EntryNo',
                        action='store',
                        type=int,
                        help='The number of entries required per file',
                        dest='EN')
    parser.add_argument('-j', '--joinerfunction',
                        action='store',
                        help='A non functional that specifies joinerfunction',
                        dest='J')
    options = parser.parse_args(args)
    return options


print(f'You have entered:\n{sys.argv[1:]}')


def main():
    """
    A for loop for argument checking and
    function calling
    """
    options = parse_command_args()
    aFI = sys.argv[2]
    aFO = sys.argv[4]
    for arg in sys.argv:
        if arg == '-FI' and '-FO':

            if arg == '-en':
                entryfunction(aFI, aFO, int(sys.argv[6]))
                if len(sys.argv[1:]) != 6:
                    print('Check the number of args, somethings not right')
                    sys.exit(0)

            elif arg == '-ch':
                chunkfunction(aFI, aFO, sys.argv[6], int(sys.argv[8]))
                if len(sys.argv[1:]) != 8:
                    print('Check your number of args, somethings not right')
                    sys.exit(0)

            elif arg == '-sc':
                surgicalfunction(aFI, aFO, int(sys.argv[6]), int(sys.argv[8]))
                if len(sys.argv[1:]) != 8:
                    print('Check your number of args, somethings not right')
                    sys.exit(0)

            elif arg == '-j':
                joinerfunction(aFI, aFO)
                if len(sys.argv[1:]) != 4:
                    print('Check your number of args, somethings not right')
                    sys.exit(0)

            elif len(arg) == 14:
                entryfunction(aFI, aFO, int(sys.argv[6]))
                chunkfunction(aFI, aFO, sys.argv[8], int(sys.argv[10]))
                surgicalfunction(aFI, aFO, int(sys.argv[12]), int(sys.argv[14]))
                joinerfunction(aFI, aFO)
                if len(sys.argv[1:]) != 14:
                    print('Check your number of args, somethings not right.')
                    print('Calling all funs requires a specific order')
                    sys.exit(0)

        else:
            print('Where are -FI (FileInput) and -FO (FileOutPut) flags')
            print(arg)
            sys.exit(0)


def read_fasta(filetoparse):  # Works as part of entryfunction
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


def entryfunction(FI, FO, EN=1):  # <- Works but needs a more ellegant solution
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

                with open(FO + str(filecounter) + '.fa', 'w') as done:
                    for idss, sequence in entry:
                        done.write(idss + '\n' + sequence + '\n\n')

                    count = 0
                    entry = []

        filecounter += 1
        with open(FO + str(filecounter) + '.fa', 'w') as done:
            for idss, sequence in entry:
                done.write(idss + '\n' + sequence + '\n\n')

            entry = []
            print('Give me a second to load files')


def chunkfunction(FI, FO, CS, ORG='chunk'):  # Works
    """A function to split a file based on user defined bp per file"""
    with open(FI, 'r') as file:
        read = file.readline()
        towrite = []
        length = 0
        counter = 0

        while read:
            towrite.append(read)
            length += len(read)-1
        if length > CS:
            with open(FO + ORG + '|{}'.format(counter) + '.fa', 'w') as opened:
                opened.write(''.join(towrite))
                counter += 1
                towrite = []
                length = 0
        with open(FO + ORG + '|{}'.format(counter) + '.fa', 'w') as opened:
            opened.write(''.join(towrite))


def surgicalfunction(FI, FO, SC, EC):  # Works
    """A function to find a specified index of """
    with open(FI, 'r') as opened:
        openread = opened.read()
        openread2 = openread.strip()
        find = openread2[SC:EC]
        with open(f'{FO}snipped|{SC}:{EC}.fa', 'w') as snipped:
            print(find + f'{FO}snipped|{SC}:{EC}.fa', 'w')
            snipped.write(find)


def joinerfunction(FI, FO):  # Not Working
    """A function to join all singular enteries into one multi-line fasta"""
    total = []
    counter = 0

    for file in os.listdir(FI):
        if file.endswith('.fasta' or '.fa' or '.fna'):
            fullpath = os.path.join(FO, file)
            total.append(fullpath)
            with open(FO + counter, 'w') as outfile:
                for filename in total:
                    with open(filename, 'r') as infile:
                        for line in infile:
                            outfile.write(line)


if __name__ == '__main__':
    main()
