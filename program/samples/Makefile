# This is a script written in GNU make.
# The next two lines are one command.  The first line indicates two parameters.  
# The first parameter is the result. The second parameter is the input.
# The indented string of characters ps2pdf is the name of the program that will take the input and create the output.
# The $< is the argument for this program telling it to use the second of the two preceding parameters as the input.
%.pdf: %.ps
	ps2pdf $<

# The following is a variation on the earlier "theme".  There are once again two commands, the second being indented.
# To make things even more complicated, the second line is actually a series of convoluted commands.
# "(" signals the beginning of a sub-shell.  "cd ..;" says to change the directory to the parent. 
# Python says to start the Python runtime application which then requires the argument of what it is to run, namely psLabelGenerator.py.
# psLabelGenerator.py will take its input from "standard in" and send it to "standard out"
# "standard in" is specified by < samples/$< (note the use of the "<" has nothing to do with direction.)  
# "standard out" is specified by > samples/$@
# Just to cap the cryptic nature of this command syntax, "standard in" refers to the second parameter above, 
# "%.nuera.csv" and "standard out" refers to the first parameter
%.nuera.ps: %.nuera.csv
	( cd ..; python psLabelGenerator.py < samples/$< > samples/$@ )

%.nuera_titled.ps: %.nuera_titled.csv
	( cd ..; python psGenerator.py < samples/$< > samples/$@ )
