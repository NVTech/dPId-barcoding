%.pdf: %.ps
	ps2pdf $<

%.nuera.ps: %.nuera.csv
	(cd ..; python psLabelGenerator.py < samples/$< > samples/$@)

%.nuera_titled.ps: %.nuera_titled.csv
	(cd ..; python psGenerator.py < samples/$< > samples/$@)
