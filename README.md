# File_Parsing
A FASTA parsing script created for use at Sanger and during the BSc Bioinformatics apprenticeship at ARU

14/11/19 	- arg.parse command structure completely changed from sub-parsers to 				standard parsers.
			- __doc__ has been revamped by adding examples and a more in-depth explanation.
			- Surgical Function now saves the produced output.
			- Each function now has a different saving scheme (temporary scheme) to differentiate the results of each function (will add a file system to better organise this).
			- Chunks returns non-default errors.
			- Joiner does not work.
			- Entry will be re-written entirely and read_fasta removed.