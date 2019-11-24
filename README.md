# File_Parsing
A FASTA parsing script created for use at Sanger and during the BSc Bioinformatics apprenticeship at ARU

14/11/19 	- arg.parse command structure completely changed from
			  sub-parsers to standard parsers.
			- __doc__ has been revamped by adding examples and a more
			  in-depth explanation.
			- Surgical Function now saves the produced output.
			- Each function now has a different saving scheme (temporary
			  scheme) to differentiate the results of each function (will add a file system to better organise this).
			- Chunks returns non-default errors.
			- Joiner does not work.
			- Entry will be re-written entirely and read_fasta removed.

22/11/19	- Chunk function fixed
				- Arguments with default values (e.g. ch = 1) must be last in required arguments.
			- __doc__ updated for correct grammar and more consistency.
			- Entry func not yet fixed
			- Joiner func not yet fixed
			- README updated to include future work needed
			- introduced the arg -j to allow for a more efficient selection
			  of function

23/11/19	- Entry func works
			- __doc__ updated
			- Script now follows pycodestyle

24/11/19	- pylint score of 8.53

FUTURE WORK TO BE IMPLIMENTED
			- Each function now has a different saving scheme (temporary
			  scheme) to differentiate the results of each function (will add a file system to better organise this).
			- Fix Joiner Func
			- Create better Entry
			- Reduce false errors