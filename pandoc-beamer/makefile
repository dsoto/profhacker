pdf:
	pandoc -t beamer --template soto-beamer.tex -o presentation.pdf presentation.md

tex:
	pandoc -t beamer --template soto-beamer.tex -o presentation.tex presentation.md
	pdflatex presentation.tex

clean:
	rm presentation.pdf presentation.tex *.log *.aux

# i don't understand how to get the file to compile as a beamer document
# http://jeromyanglim.blogspot.com/2012/07/beamer-pandoc-markdown.html
