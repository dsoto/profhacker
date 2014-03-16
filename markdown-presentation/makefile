# presentation makefile

HANDLE = presentation

# create slide deck
$(HANDLE).pdf: $(HANDLE).md
	pandoc -t beamer $(HANDLE).md -o $(HANDLE).pdf

# create pdf slide deck with interactive build
slidebuild : $(HANDLE).md
	pandoc -t beamer -i $(HANDLE).md -o $(HANDLE).pdf

# create with build and open adobe with file
lecture:
	make slidebuild
	open -a /Applications/Adobe\ Reader.app/ $(HANDLE).pdf

