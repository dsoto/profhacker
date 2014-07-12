# this makefile will convert all markdown (.md) documents in a directory
# and convert to DOCX, PDF, and HTML output

EXT = md

SRC = $(wildcard *.$(EXT))
PDFS=$(SRC:.md=.pdf)
DOCX=$(SRC:.md=.docx)
HTML=$(SRC:.md=.html)

all: $(PDFS) $(DOCX) $(HTML)

# generate both the assignment and the solution
# $@ name of target
# $* stem of target
# $< name of first prerequisite

%.pdf: %.$(EXT)
	pandoc -o $*.pdf $<

%.docx: %.$(EXT)
	pandoc -o $*.docx $<

%.html: %.$(EXT)
	pandoc -o $*.html $<

