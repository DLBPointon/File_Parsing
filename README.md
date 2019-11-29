# File_Parsing
A FASTA parsing script created for use at Sanger and during the BSc Bioinformatics apprenticeship at ARU

## Instructions
The fastaparsing.py file is the main object of this repository. Due to the location of many peoples python environment being in odd places there is a one time extra bit of work you need to perform unless your ok with using scripts with: '$ python script'.

To use the ./ of script usage then you will be requirefd to insert the path of your python env into the shebang header (#!).

This can be acheived with typing '$ which python' into the commandline. The full path of this one line will then need to replace the /usr/bin/python found after the shebang in the first line of fastaparsing.py script. This is a typical default python env location.

Opening of the script via your usual editor (nano, vim or sublime) is possible via the command line.

## Change-log

### 14/11/19
- arg.parse command structure completely changed from sub-parsers to standard parsers.
- __doc__ has been revamped by adding examples and a more
  in-depth explanation.
- Surgical Function now saves the produced output.
- Each function now has a different saving scheme (temporary
  scheme) to differentiate the results of each function (will add a file system to better organise this).
- Chunks returns non-default errors.
- Joiner does not work.
- Entry will be re-written entirely and read_fasta removed.

### 22/11/19	
- Chunk function fixed
- Arguments with default values (e.g. ch = 1) must be last in required arguments.
- __doc__ updated for correct grammar and more consistency.
- Entry func not yet fixed
- Joiner func not yet fixed
- README updated to include future work needed
- introduced the arg -j to allow for a more efficient selection
  of function

### 23/11/19	
- Entry func works
- __doc__ updated
- Script now follows pycodestyle

### 24/11/19	
- pylint score of 8.53

### 26/11/19	
- functions renamed for better distinction
- pycodestyle compliant and pylint score of 8.25
- Joinerfunction now works
- os module replaced with glob2 module
- __doc__ updated with joiner saving scheme
- small corections to examples and -j calling
- -j made useful
- README updated

### 27/11/19	
- f string standardization across script
- chunkfunction fixed (previously thought working), small files will be chunked into entries
- __doc__ updated to show above
- pycodestyle compliant and pylint score of 8.56 (due to style choices for argument names)
- README updated

### 28/11/19	
- Added clarification to shebang management
- will require the running 'which python' in command line and then Copy Pasting this to replace 
[REPLACE ME WITH THE RESULTS OF WHICH PYTHON] after #! (shebang header)
- Renamed files to make distinction easier:
- trial.py -> fastaparsing.py
- fileparse.py -> originalattempt.py

## FUTURE WORK TO BE IMPLIMENTED
- Each function now has a different saving scheme (temporary
  scheme) to differentiate the results of each function (will add a file system to better organise this).
- Create better Entry
- Reduce false errors
- make script executional - half way there 
